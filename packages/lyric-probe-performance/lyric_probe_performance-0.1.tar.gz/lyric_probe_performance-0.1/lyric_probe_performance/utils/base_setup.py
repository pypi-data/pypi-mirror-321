"""Setup module for test environment initialization."""
import json
import time
from lyric_probe_performance.controllers.external_apps import ExternalApps
from lyric_probe_performance.controllers.external_scenarios import ExternalScenarios
from lyric_probe_performance.controllers.external_token import ExternalToken
from lyric_probe_performance.controllers.external_tables import ExternalTables
from lyric_probe_performance.utils.exceptions import TestExecutionError
from utils import token_manager
from utils.config_loader import ConfigLoader
from utils.download_manager import download_files_with_progress
from controllers.external_actions import ExternalActions
from utils.log_manager import setup_logger
import requests
import os
import pathlib
from typing import List, Dict, Any, Optional

from utils.auth_manager import AuthManager

# Set up logging
logger = setup_logger(__name__)


class BaseSetUp:
    """Handles the setup and authentication for external services."""

    def __init__(self, client, client_id, client_secret, sequence_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.sequence_id = sequence_id
        self.client = client
        self.external_apps = ExternalApps(client)
        self.external_tables = ExternalTables(client)
        self.external_token = ExternalToken(client)
        self.external_scenarios = ExternalScenarios(client)
        self.external_actions = ExternalActions(client)
        self.auth_manager = AuthManager(client, client_id, client_secret)
        self.app_slug = None
        self.actions_details = []
        self.signature_scenario_id = None
        self.signature_scenario_name = None
        self.table_ids = []
        self.downloaded_files = []
        self.groups = {}

    async def authenticate(self):
        """Authenticate using the auth manager with token reuse."""
        try:
            # If the client already has Authorization header, skip authentication
            if self.client.headers.get('Authorization'):
                logger.debug("Using existing authentication token")
                return
                
            # If token exists in token manager but not in headers, set it
            if token_manager.token:
                self.client.headers.update({
                    "Authorization": f"Bearer {token_manager.token}",
                    "Content-Type": "application/json"
                })
                logger.debug("Using cached authentication token")
                return
                
            # If no token exists, authenticate and store the token
            await self.auth_manager.authenticate()
            
            # Cache the new token
            if 'Authorization' in self.client.headers:
                auth_header = self.client.headers['Authorization']
                if auth_header.startswith('Bearer '):
                    token = auth_header.split(' ')[1]
                    token_manager.token = token
                    logger.debug("Cached new authentication token")
                    
        except Exception as e:
            logger.error(f"Authentication error: {str(e)}")
            raise TestExecutionError(f"Authentication failed: {str(e)}")

    async def get_app_details(self):
        try:
            self.app_response = self.external_apps.get_app(self.sequence_id)
            
            if not self.app_response:
                logger.error("No app response received")
                return None, None, None, None

            self.app_slug = self.app_response.get('slug')
            self.signature_scenario_name = self.app_response.get('displayName')
            self.actions_details = self.get_action_details()
            logger.debug("Actions details: %s", self.actions_details)         
            self.table_details = self.get_table_details()
            logger.debug("Table_details: %s", self.table_details)
            if not self.app_slug:
                logger.error("No app slug found in response")
                return None, None, None, None

            signature_scenario_response = self.external_scenarios.get_scenarios(self.app_slug, 'active', 'signature')
            if signature_scenario_response.ok:
                signature_scenario_data = signature_scenario_response.json()
                if signature_scenario_data and isinstance(signature_scenario_data, list):
                    self.signature_scenario_id = signature_scenario_data[0].get('id')
            else:
                logger.error(f"Failed to get signature scenario. Status: {signature_scenario_response.status_code}")
                self.signature_scenario_id = None
                self.signature_scenario_name = None

            return self.app_slug, self.actions_details, self.signature_scenario_id, self.signature_scenario_name
        except Exception as e:
            logger.error(f"Error getting app details: {str(e)}")
            raise TestExecutionError(f"Error getting app details: {str(e)}")
        finally:
            logger.info("GetAppDetails Completed")

    def download_tables(self) -> Dict[str, Dict[str, Any]]:
        """
        Download tables group by group and return download information.
        Returns a dictionary with group names as keys and download details as values.
        """
        try:
            logger.info("Starting table download process...")
            download_results = {}
            
            # Process each group separately
            for table_detail in self.table_details.get("table_details", []):
                group_name = table_detail["group"]
                tables = table_detail.get("tables", [])
                
                if not tables:
                    logger.warning(f"No tables found for group {group_name}")
                    continue
                    
                # Get table IDs for this group
                table_ids = [table["id"] for table in tables]
                logger.info(f"Downloading tables for group {group_name} with {len(table_ids)} tables")
                
                # Initiate download process for this group
                response = self.external_tables.download_tables(
                    self.app_slug,
                    table_ids,
                    download_format='csv'
                )
                
                if "error" in response:
                    logger.error(f"Failed to download tables for group {group_name}: {response.get('error')}")
                    if "response" in response:
                        logger.error(f"Response details: {response.get('response')}")
                    continue
                
                downloads = response.get('downloads', {})
                urls = downloads.get('urls', [])
                
                if not urls:
                    logger.error(f"No download URLs found for group {group_name}")
                    continue
                    
                logger.info(f"Received {len(urls)} download URLs for group {group_name}")
                
                # Define subdirectory for this group
                sequence_id = self.sequence_id or 'default'
                subdir = f"{sequence_id}/{group_name}"
                
                # Initialize download progress tracking for this group
                total_downloaded = 0
                last_log_time = time.time()
                
                def progress_callback(chunk_size: int, total_size: int, filename: str):
                    nonlocal total_downloaded, last_log_time
                    total_downloaded += chunk_size
                    
                    current_time = time.time()
                    if current_time - last_log_time >= 30:  # Log every 30 seconds
                        elapsed_time = current_time - last_log_time
                        downloaded_mb = total_downloaded / (1024 * 1024)
                        speed = downloaded_mb / elapsed_time if elapsed_time > 0 else 0
                        
                        logger.info(f"Download in progress for group {group_name}...")
                        logger.info(f"Total downloaded: {downloaded_mb:.2f} MB")
                        logger.info(f"Average speed: {speed:.2f} MB/s")
                        logger.info(f"Currently downloading: {filename}")
                        
                        last_log_time = current_time
                
                # Download files for this group
                downloaded_files = download_files_with_progress(
                    urls=urls,
                    base_dir='./downloads',
                    subdir=subdir,
                    file_filters=None,
                    progress_callback=progress_callback
                )
                
                if not downloaded_files:
                    logger.error(f"No files were downloaded for group {group_name}")
                    continue
                
                # Store results for this group
                download_dir = f'./downloads/{subdir}'
                download_results[group_name] = {
                    'download_directory': download_dir,
                    'files': downloaded_files,
                    'total_files': len(downloaded_files),
                    'download_time': time.strftime('%Y-%m-%d %H:%M:%S')
                }
                
                logger.info(f"Successfully downloaded {len(downloaded_files)} files for group {group_name}")
                
            return download_results
            
        except Exception as e:
            logger.error(f"Error downloading tables: {str(e)}")
            return {}
        
    def get_action_details(self) -> Dict[str, Any]:
        """
        Get filtered action details (name, type, parameters) for visible actions only.
        Returns a dictionary with filtered action details.
        """
        try:
            logger.info("Getting action details...")
            
            # Filter only visible actions
            filtered_actions = [
                {
                    "name": action["name"],
                    "type": action["type"],
                    "referenceId": action["referenceId"],  # Added referenceId
                    "parameters": action.get("parameters", []),
                    "isVisible": action.get("isVisible")
                }
                for action in self.app_response.get('actionsSettings', [])
                if action.get('isVisible', False)  # Only include if isVisible is True
            ]
            
            if filtered_actions:
                logger.info(f"Found {len(filtered_actions)} visible actions")
            else:
                logger.warning("No visible actions found")
            
            return {
                "actions": filtered_actions
            }
            
        except Exception as e:
            logger.error(f"Error getting action details: {str(e)}")
            return {"actions": []}
    
    def get_table_details(self) -> Dict[str, Any]:
        """
        Get table details for a given table ID.
        Returns a dictionary with table details grouped by their respective groups.
        Only includes groups that have tables and skips maps/dashboards.
        """
        try:
            tables_response = self.external_tables.get_tables(self.app_slug)
            table_details = []
            # Create a lookup dictionary for table info from get-tables endpoint
            table_lookup = {}
            for table in tables_response:  # Assuming tables_response contains the get-tables response
                table_id = table.get('id')
                if table_id:
                    table_lookup[table_id] = {
                        'name': table.get('name'),
                    }
            
            # Process each group in groups_details
            groups_details = self.app_response.get('groups', [])
            for group in groups_details:
                # Skip if group is not visible
                if not group.get("isVisible", False):
                    continue
                
                # Get table members for the current group
                # Filter out maps and dashboards
                tables = []
                for member in group.get("members", []):
                    if member.get("type") != "table":  # Skip non-table items
                        continue
                        
                    table_id = member.get("id")
                    if table_id and table_id in table_lookup:
                        table_info = table_lookup[table_id]
                        tables.append({
                            "id": table_id,
                            "name": table_info.get('name', table_id),
                        })
                
                # Only add groups that have tables
                if tables:
                    group_detail = {
                        "group": group["displayName"],
                        "tables": tables
                    }
                    table_details.append(group_detail)
            
            return {"table_details": table_details}
        
        except Exception as e:
            logger.error("Error getting table details: %s", str(e))
            return {"table_details": []}
        
    def prepare_upload_data(self) -> List[Dict[str, Any]]:
        """Prepare file paths and payload for uploads."""
        self.upload_data = []
        table_details = self.table_details.get('table_details', [])
        
        for group_detail in table_details:
            group_name = group_detail.get('group')
            tables = group_detail.get('tables', [])
            
            if not tables:
                logger.warning(f"No tables found for group {group_name}")
                continue
            
            files_info = []
            for table in tables:
                table_id = table.get('id')
                table_name = table.get('name')
                
                if not table_id or not table_name:
                    logger.warning(f"Invalid table data in group {group_name}: {table}")
                    continue
                
                file_name = f"{table_name}.csv"
                sequence_id = self.sequence_id or 'default'
                file_path = f"./downloads/{sequence_id}/{group_name}/{file_name}"
                
                # Assert file exists
                assert os.path.exists(file_path), f"File not found: {file_path}. Ensure the file is downloaded or generated before upload."
                
                files_info.append({
                    'table_id': table_id,
                    'filename': file_name,
                    'path': file_path
                })
            
            if files_info:
                self.upload_data.append({
                    "group_name": group_name,
                    "files_info": files_info
                })
        
        return self.upload_data
        
    async def setup(self) -> Dict[str, Any]:
        """Execute all setup functions in sequence."""
        try:
            # Authenticate first
            await self.authenticate()
            
            # Get app details
            app_details = await self.get_app_details()
            if not app_details or not app_details[0]:
                raise TestExecutionError("Failed to get app details")
            
            # Download tables synchronously (no await needed)
            self.download_tables()
            self.prepare_upload_data()
            logger.info(f"Upload data: {self.upload_data}")
            setup_data = {
                'app_slug': self.app_slug,
                'signature_scenario_id': self.signature_scenario_id,
                'actions_details': self.actions_details,
                'signature_scenario_name': self.signature_scenario_name,
                'sequence_id': self.sequence_id,
                'table_details': self.table_details,
                'upload_data': self.upload_data
            }
            return setup_data
        except Exception as e:
            logger.error(f"Error in setup: {str(e)}")
            raise TestExecutionError(f"Error in setup: {str(e)}")