from locust import between, task
from pathlib import Path
import asyncio
import time
from locust.exception import StopUser
from utils.log_manager import setup_logger
from utils.upload_manager import FileUploader, UploadManager
from controllers.external_tables import ExternalTables

logger = setup_logger(__name__)

class FileUploadTask:
    """Task for handling file uploads."""
    
    wait_time = between(1, 2)

    def __init__(self, user):
        self.user = user
        self.external_tables = ExternalTables(self.user.client)
        self.uploader = FileUploader(self.user.client, self.user.setup_data['app_slug'])
        self.upload_manager = UploadManager(self.uploader)
        self._is_interrupted = False  # Track if the task is interrupted

    @task
    async def run_upload_files(self):
        logger.info("Upload file task started")
        """Wrapper to run the async upload method."""
        await self._upload_files(self.user.scenario_id)  

    async def _upload_files(self, scenario_id: str):
        """Upload files for the given scenario, stopping the current user on any failures."""
        try:
            start_time = time.time()
            app_slug = self.user.setup_data.get('app_slug')
            logger.info(f"Starting file upload process for scenario {scenario_id}")
            
            upload_data = self.user.setup_data.get('upload_data', [])
            if not upload_data:
                logger.error("No upload data found in setup_data. Stopping execution for the current user.")
                raise StopUser("Missing upload data in setup_data.")
            
            for data in upload_data:
                if self._is_interrupted:
                    logger.info("Upload task was interrupted.")
                    return

                group_name = data.get("group_name")
                files_info = data.get("files_info", [])
                
                if not files_info:
                    logger.warning(f"No files found for group {group_name}. Skipping.")
                    continue
                
                logger.info(f"Uploading {len(files_info)} files for group {group_name}")
                
                upload_payload = {
                    "tableData": [
                        {"tableId": file_info["table_id"], "filename": file_info["filename"]}
                        for file_info in files_info
                    ],
                    "uploadFormat": "csv",
                    "scenarioId": scenario_id,
                }

                try:
                    # Perform the upload
                    response = self.external_tables.upload_tables(
                        app_slug=app_slug,
                        files_info=files_info,
                        payload=upload_payload,
                    )
                    
                    if response.status_code == 200:
                        response_data = response.json()
                        logger.info(f"Response data: {response_data}")
                        logger.info(f"✓ Upload completed successfully for group {group_name} (Scenario: {scenario_id})")
                        
                        # Handle partial failures
                        failures = self._validate_partial_failures(response_data, group_name)
                        if failures:
                            logger.error(f"Failures detected for group {group_name}. Stopping execution for the current user.")
                            raise StopUser(f"Upload failures in group {group_name}: {', '.join(failures)}")
                    else:
                        logger.error(f"❌ Upload failed for group {group_name}. Status: {response.status_code}")
                        raise StopUser(f"Critical upload failure for group {group_name}. Stopping execution for the current user.")
                except Exception as upload_error:
                    logger.error(f"Error during upload for group {group_name}: {str(upload_error)}")
                    raise StopUser("Critical error during file upload. Stopping execution for the current user.")
                
                # Delay between uploads
                await asyncio.sleep(2)
            
            logger.info(f"File upload process completed for scenario {scenario_id} in {time.time() - start_time:.2f} seconds.")
        except StopUser as stop_user_exception:
            logger.warning(f"Execution stopped for the current user due to: {str(stop_user_exception)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in _upload_files: {str(e)}")
            raise StopUser("Unexpected error. Stopping execution for the current user.")

    def _validate_partial_failures(self, response_data, group_name):
        """Validate and log partial failures in the response."""
        failures = [
            f"{k}: {v['message']}" 
            for k, v in response_data.get('response', {}).items()
            if v.get('error')
        ]
        if failures:
            logger.debug(f"Partial failures detected in group {group_name}: {failures}")
        return failures

    def interrupt(self):
        """Interrupt the upload task."""
        logger.info("Interrupting the upload task.")
        self._is_interrupted = True