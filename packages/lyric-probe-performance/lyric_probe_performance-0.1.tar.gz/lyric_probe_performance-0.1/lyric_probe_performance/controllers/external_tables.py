"""Controller for external tables."""
import json
import os
from pathlib import Path
import time
from typing import Dict, Any, List, Optional, Union
import logging
import threading

from requests import Response
import requests
from requests_toolbelt import MultipartEncoder

from routes import APIRoutes
from utils.exceptions import ConfigurationError, TestExecutionError
from .base_controller import BaseController

from utils.log_manager import setup_logger

logger = setup_logger(__name__)

class ExternalTables(BaseController):
    """External tables controller."""

    def get_tables(self, app_slug: str) -> Union[List[Dict], Dict]:
        """Get all tables for the app."""
        try:
            response = self.client.get(
                APIRoutes.GET_TABLES(app_slug),
                name="get_tables"
            )
            if response.ok:
                return response.json()
            logger.error(f"Failed to get tables. Status: {response.status_code}, Response: {response.text}")
            return {"error": "Failed to fetch tables"}
        except Exception as e:
            logger.error(f"Error getting tables: {str(e)}")
            return {"error": str(e)}

    def get_table_details(self, app_slug: str, table_id: str) -> Dict[str, Any]:
        """Get table details for the app."""
        try:
            response = self.client.get(
                APIRoutes.GET_TABLE_DETAILS(app_slug, table_id),
                name="get_table_details"
            )
            if response.ok:
                return response.json()
            logger.error(f"Failed to get table details. Status: {response.status_code}, Response: {response.text}")
            return {"error": "Failed to fetch table details"}
        except Exception as e:
            logger.error(f"Error getting table details: {str(e)}")
            return {"error": str(e)}

    def download_tables(self, app_slug: str, table_ids: List[str], download_format: str = 'csv') -> Dict[str, Any]:
        """
        Download tables data.
        
        Args:
            app_slug: Application slug name
            table_ids: List of table IDs to download
            download_format: Format of the download (e.g., 'csv')
            
        Returns:
            Dict[str, Any]: Response containing download URLs or error details
        """
        try:
            payload = {
                "tableIds": table_ids,
                "downloadFormat": download_format
            }
            
            logger.debug(f"Download payload: {payload}")
            
            response = self.client.post(
                APIRoutes.DOWNLOAD_TABLE_DATA(app_slug),
                json=payload,
                name="download_tables"
            )
            
            # Check if response has status_code (Response object)
            if hasattr(response, 'status_code'):
                if response.status_code == 201:
                    return response.json()
                logger.error(f"Failed to download tables. Status: {response.status_code}, Response: {response.text}")
                return {"error": f"Download failed with status {response.status_code}"}
            
            # If response is already parsed JSON (dict)
            if isinstance(response, dict):
                if "downloads" in response and "errors" in response:
                    if not response["errors"]:  # No errors
                        return response
                    logger.error(f"Download response contains errors: {response['errors']}")
                    return {"error": "Download response contains errors", "details": response["errors"]}
                return response
            
            logger.error(f"Unexpected response format: {response}")
            return {"error": "Unexpected response format"}
            
        except Exception as e:
            logger.error(f"Error downloading tables: {str(e)}")
            return {"error": str(e)}
     
    def upload_tables(self, app_slug: str, files_info: List[Dict], payload: Dict) -> requests.Response:
        """Upload multiple tables using MultipartEncoder for streaming."""
        try:
            url = APIRoutes.UPLOAD_TABLE_DATA(app_slug)
            logger.info(f"Upload URL: {url}")
            logger.info(f"Payload: {payload}")
            logger.info(f"Files info: {files_info}")
            
            headers = {
                'accept': '*/*'
            }
            if hasattr(self.client, 'headers'):
                auth_header = self.client.headers.get('Authorization')
                if auth_header:
                    headers['Authorization'] = auth_header

            fields = {}
            fields['data'] = (None, json.dumps(payload), 'application/json')

            file_objects = []
            try:
                for file_info in files_info:
                    file_path = Path(file_info['path'])
                    file_name = file_info['filename']
                    
                    if not file_path.exists():
                        logger.error(f"File not found: {file_path}")
                        continue

                    file_obj = open(file_path, 'rb')
                    file_objects.append(file_obj)
                    fields[file_name] = (file_name, file_obj, 'text/csv')

                encoder = MultipartEncoder(fields=fields)
                headers['Content-Type'] = encoder.content_type

                start_time = time.time()
                response = None

                # Start the upload request in a separate thread
                def upload_request():
                    nonlocal response
                    response = requests.put(
                        url=url,
                        data=encoder,
                        headers=headers,
                        stream=True,
                        timeout=600
                    )

                upload_thread = threading.Thread(target=upload_request)
                upload_thread.start()

                # Log elapsed time every 30 seconds
                while upload_thread.is_alive():
                    elapsed_time = time.time() - start_time
                    logger.info(f"Elapsed time since upload request sent: {elapsed_time:.2f} seconds")
                    time.sleep(30)

                upload_thread.join()

                total_time = time.time() - start_time
                logger.info(f"Total time taken for upload request to complete: {total_time:.2f} seconds")

                return response

            finally:
                for file_obj in file_objects:
                    try:
                        file_obj.close()
                    except Exception as e:
                        logger.warning(f"Error closing file: {str(e)}")

        except Exception as e:
            logger.error(f"Error in upload_tables: {str(e)}")
            raise TestExecutionError(f"Error in upload_tables: {str(e)}")