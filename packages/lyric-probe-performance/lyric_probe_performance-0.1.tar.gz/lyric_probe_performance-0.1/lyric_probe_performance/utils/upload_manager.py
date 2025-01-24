import asyncio
import json
import time
from contextlib import asynccontextmanager
from typing import List, Dict, Any, Optional
from pathlib import Path
import requests
from requests_toolbelt import MultipartEncoder
from tenacity import retry, stop_after_attempt, wait_exponential
from locust import events

from utils.log_manager import setup_logger

logger = setup_logger(__name__)

class RateLimiter:
    """Rate limits operations to a maximum number per second."""
    
    def __init__(self, max_per_second: float):
        self.max_per_second = max_per_second
        self.min_interval = 1.0 / max_per_second
        self._last_check = time.monotonic()
        self._lock = asyncio.Lock()

    @asynccontextmanager
    async def __call__(self):
        """Use as async context manager to rate limit operations."""
        async with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_check
            wait_time = self.min_interval - elapsed
            
            if wait_time > 0:
                await asyncio.sleep(wait_time)
                
            self._last_check = time.monotonic()
            yield

class FileUploader:
    """Handles file uploads with retries and proper error handling."""
    
    def __init__(self, client, app_slug: str):
        self.client = client
        self.app_slug = app_slug
        
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        reraise=True
    )
    def upload_files(self, files_info: List[Dict], scenario_id: str) -> Dict[str, Any]:
        """
        Upload files with retry logic and proper multipart handling.
        
        Args:
            files_info: List of dicts containing file info (table_id, filename, path)
            scenario_id: ID of the scenario to upload to
            
        Returns:
            Dict with upload results
            
        Raises:
            ValueError: If files are too large or partial upload failures occur
            requests.exceptions.RequestException: For request-related errors
        """
        file_objects = []
        start_time = time.time()
        
        try:
            # Prepare the fields for multipart upload
            fields = {}
            
            # Add JSON payload
            payload = {
                "tableData": [
                    {"tableId": file_info["table_id"], "filename": file_info["filename"]} 
                    for file_info in files_info
                ],
                "uploadFormat": "csv",
                "scenarioId": scenario_id
            }
            fields["data"] = (None, json.dumps(payload), "application/json")
            
            # Add each file to the multipart encoder
            total_size = 0
            for file_info in files_info:
                file_path = Path(file_info["path"])
                if not file_path.exists():
                    raise FileNotFoundError(f"File not found: {file_path}")
                
                file_size = file_path.stat().st_size
                total_size += file_size
                
                file_obj = open(file_path, "rb")
                file_objects.append(file_obj)
                fields[file_info["filename"]] = (
                    file_info["filename"],
                    file_obj,
                    "text/csv"
                )
                logger.debug(f"Added file {file_info['filename']} ({file_size / 1024 / 1024:.2f} MB)")
            
            logger.info(f"Total upload size: {total_size / 1024 / 1024:.2f} MB")
            
            # Create multipart encoder
            encoder = MultipartEncoder(fields=fields)
            
            # Prepare headers
            headers = {
                "Content-Type": encoder.content_type
            }
            if "Authorization" in self.client.headers:
                headers["Authorization"] = self.client.headers["Authorization"]
                
            # Make request with increased timeout
            url = f"{self.client.base_url}/lyapi/table/upload-csv/{self.app_slug}"
            response = requests.put(
                url=url,
                data=encoder,
                headers=headers,
                timeout=600  # 10 minute timeout
            )
            
            response_time = int((time.time() - start_time) * 1000)
            
            # Record the request
            events.request.fire(
                request_type="PUT",
                name=f"Upload {len(files_info)} files",
                response_time=response_time,
                response_length=total_size,
                response=response,
                context={
                    "scenario_id": scenario_id,
                    "files": [f["filename"] for f in files_info]
                }
            )
            
            # Check response
            if response.status_code == 413:
                raise ValueError("File too large - consider splitting into smaller chunks")
            response.raise_for_status()
            
            result = response.json()
            
            # Check for partial failures
            failures = []
            if isinstance(result, dict) and "response" in result:
                for table_id, details in result["response"].items():
                    if details.get("error"):
                        failures.append(f"{table_id}: {details.get('message')}")
            
            if failures:
                raise ValueError(f"Partial upload failure: {', '.join(failures)}")
                
            return result
            
        except Exception as e:
            logger.error(f"Upload error: {str(e)}")
            # Record failure
            events.request_failure.fire(
                request_type="PUT",
                name=f"Upload {len(files_info)} files",
                response_time=int((time.time() - start_time) * 1000),
                exception=e
            )
            raise
            
        finally:
            # Clean up file objects
            for file_obj in file_objects:
                try:
                    file_obj.close()
                except Exception as e:
                    logger.warning(f"Error closing file: {str(e)}")

class UploadManager:
    """Manages file uploads with batching and rate limiting."""
    
    def __init__(self, uploader: FileUploader, batch_size: int = 3):
        self.uploader = uploader
        self.batch_size = batch_size
        self._rate_limiter = RateLimiter(max_per_second=2)
        
    async def upload_in_batches(
        self, 
        all_files: List[Dict], 
        scenario_id: str,
        batch_size: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Upload files in batches to avoid overwhelming the server.
        
        Args:
            all_files: List of file information dictionaries
            scenario_id: ID of the scenario to upload to
            batch_size: Optional override for batch size
            
        Returns:
            List of upload results for each batch
        """
        results = []
        batch_size = batch_size or self.batch_size
        
        # Split files into batches
        for i in range(0, len(all_files), batch_size):
            batch = all_files[i:i + batch_size]
            
            # Rate limit the uploads
            async with self._rate_limiter:
                try:
                    result = self.uploader.upload_files(batch, scenario_id)
                    results.append(result)
                    logger.info(f"Successfully uploaded batch {i//batch_size + 1}")
                except Exception as e:
                    logger.error(f"Batch upload failed: {str(e)}")
                    raise
                    
        return results