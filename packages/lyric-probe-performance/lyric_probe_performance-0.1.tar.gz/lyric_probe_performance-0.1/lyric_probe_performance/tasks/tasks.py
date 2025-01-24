import json
import os
import time
import random
from typing import Dict, Any
import logging
import asyncio
from controllers.external_actions import ExternalActions
from controllers.external_scenarios import ExternalScenarios
from controllers.external_tables import ExternalTables
from utils.config_loader import ConfigLoader
from utils.log_manager import setup_logger
from runner import TestExecutionError

logger = setup_logger(__name__)

class CreateAndRunScenarioTask:
    """Task for creating a scenario, uploading files, and running the scenario."""

    POLL_INTERVAL = 30  # seconds
    TIMEOUT = 10 * 60  # 10 minutes in seconds

    def __init__(self, user, setup_data: Dict[str, Any]):
        self.user = user
        self.setup_data = setup_data
        self.external_tables = ExternalTables(user.client)
        self.external_scenarios = ExternalScenarios(user.client)
        self.external_actions = ExternalActions(user.client)
        self.consecutive_failures = 0  # Add failure tracking
        self.max_retries = 3  # Maximum number of retries

    async def execute(self):
        """Execute the task."""
        try:
            task_id = f"Task_{random.randint(1000, 9999)}"
            logger.info("Starting scenario creation task...")

            # Create scenario 
            scenario_id = self._create_scenario()
            if not scenario_id:
                raise TestExecutionError("Failed to create scenario - no ID returned")
            
            # Poll status
            await self._poll_scenario_status(scenario_id)
            
            # Upload files
            await self._upload_files(scenario_id)

            # Run actions if action settings exist
            actions_details = self.setup_data.get('actions_details', {})
            if actions_details and actions_details.get('actions'):
                logger.info("Running actions for scenario")
                execution_id = await self._run_actions(scenario_id)
                if execution_id:
                    await self._poll_actions(execution_id)
            else:
                logger.info("No actions configured to run")

            self.user.environment.stats.log_success("scenario_task", "CreateAndRunScenarioTask")
            logger.info(f"Task {task_id} completed successfully")
            return True
        except Exception as e:
            logger.error(f"Task {task_id} failed: {str(e)}")
            return False
    
        
    
    
                
    async def _upload_files(self, scenario_id):
        """Upload files for the scenario."""
        try:
            start_time = time.time()
            app_slug = self.setup_data['app_slug']
            logger.info("Starting file upload process...")
            
            # Get table details and prepare group-wise payloads
            table_details = self.setup_data.get('table_details', {}).get('table_details', [])
            if not table_details:
                raise ValueError("Table details not found in setup data")
                
            # Process each group sequentially
            for group_detail in table_details:
                group_name = group_detail.get('group')
                tables = group_detail.get('tables', [])
                
                if not tables:
                    logger.warning(f"No tables found for group {group_name}")
                    continue
                    
                logger.info(f"Processing group: {group_name} with {len(tables)} tables")
                
                # Prepare table data for this group
                table_data_payload = []
                files_info = []
                total_size = 0
                
                for table in tables:
                    table_id = table.get('id')
                    table_name = table.get('name')
                    
                    if not table_id or not table_name:
                        logger.warning(f"Invalid table data in group {group_name}: {table}")
                        continue
                        
                    # Construct file path based on group structure
                    file_name = f"{table_name}.csv"
                    sequence_id = self.setup_data['sequence_id'] or 'default'
                    file_path = f"./downloads/{sequence_id}/{group_name}/{file_name}"
                    
                    # Check if file exists
                    if os.path.exists(file_path):
                        file_size = os.path.getsize(file_path)
                        total_size += file_size
                        
                        # Add to payload and files info
                        table_data_payload.append({
                            "tableId": str(table_id),
                            "filename": file_name
                        })
                        
                        files_info.append({
                            'filename': file_name,
                            'path': file_path
                        })
                        
                        logger.info(f"Prepared {file_name} for upload (Size: {file_size/1024/1024:.2f} MB)")
                    else:
                        logger.warning(f"File not found: {file_path}")
                
                if not table_data_payload or not files_info:
                    logger.warning(f"No files available for upload in group {group_name}")
                    continue
                
                # Prepare upload payload for this group
                upload_payload = {
                    "tableData": table_data_payload,
                    "uploadFormat": "csv"
                }
                
                # Add scenario ID if provided
                if scenario_id:
                    upload_payload["scenarioId"] = scenario_id
                
                logger.info(f"Uploading {len(files_info)} files for group {group_name}")
                logger.info(f"Total upload size: {total_size/1024/1024:.2f} MB")
                
                # Perform upload for this group
                response = self.external_tables.upload_tables(
                    app_slug=app_slug,
                    files_info=files_info,
                    payload=upload_payload
                )
                
                if response.status_code == 200:
                    response_data = response.json()
                    logger.info(f"✓ Upload completed successfully for group {group_name}")
                    
                    # Check for partial failures
                    if isinstance(response_data, dict) and 'response' in response_data:
                        failures = [
                            f"{k}: {v['message']}" 
                            for k, v in response_data['response'].items() 
                            if v.get('error')
                        ]
                        if failures:
                            logger.warning(f"Some files failed to upload in group {group_name}:\n" + "\n".join(failures))
                        
                    logger.debug(f"Response for group {group_name}: {response_data}")
                else:
                    logger.error(f"❌ Upload failed for group {group_name}. Status: {response.status_code}")
                    logger.error(f"Response: {response.text}")
                    raise ValueError(f"Failed to upload files for group {group_name}")
                
                # Brief pause between group uploads
                await asyncio.sleep(2)

        except Exception as e:
            elapsed_time = time.time() - start_time
            logger.error(f"Error in _upload_files after {int(elapsed_time)}s: {str(e)}")
            raise
    
    async def _run_actions(self, scenario_id):
        """Run actions for the scenario based on configuration."""
        try:
            logger.info("Running actions...")
            app_slug = self.setup_data['app_slug']
            
            # Get configured actions from config
            config = ConfigLoader().get_config()
            configured_actions = config.get('actions', [])
            
            if not configured_actions:
                logger.warning("No actions configured in config file")
                return None
            
            # Get action details from setup data and handle the format
            actions_details = self.setup_data.get('actions_details', {})
            # Check if it's a dict with 'actions' key
            if isinstance(actions_details, dict):
                action_details = actions_details.get('actions', [])
            # If it's already a list
            elif isinstance(actions_details, list):
                action_details = actions_details
            else:
                logger.error(f"Invalid action details format: {type(actions_details)}")
                raise TestExecutionError("Invalid action details format")

            if not action_details:
                logger.error("No action details found in setup data")
                raise TestExecutionError("No action details available")
                
            # Create a lookup dictionary for action details
            action_lookup = {}
            for action in action_details:
                if isinstance(action, dict) and action.get('isVisible', False):
                    name = action.get('name')
                    ref_id = action.get('referenceId')
                    if name and ref_id:
                        action_lookup[name] = ref_id

            logger.debug(f"Available actions: {json.dumps(action_lookup, indent=2)}")
            
            # Process each configured action
            execution_ids = []
            for config_action in configured_actions:
                if isinstance(config_action, dict):
                    action_name = config_action.get('name')
                    if not action_name:
                        logger.warning("Action name not found in config")
                        continue
                        
                    # Find the matching action ID
                    action_id = action_lookup.get(action_name)
                    if not action_id:
                        logger.warning(f"No matching action found for: {action_name}")
                        continue
                        
                    logger.info(f"Running action: {action_name} (ID: {action_id})")
                    
                    # Run the action
                    response = self.external_actions.run_actions(
                        app_slug=app_slug,
                        action_id=action_id,
                        scenario_id=scenario_id
                    )
                    
                    if response.status_code == 201:
                        response_data = response.json()
                        execution_id = response_data.get('executionId')
                        if execution_id:
                            execution_ids.append(execution_id)
                            logger.info(f"✓ Action {action_name} started successfully")
                            logger.info(f"Execution ID: {execution_id}")
                            logger.debug(f"Response: {json.dumps(response_data, indent=2)}")
                    else:
                        error_msg = f"Failed to run action {action_name}. Status: {response.status_code}"
                        logger.error(f"❌ {error_msg}")
                        logger.error(f"Response: {response.text}")
                        raise TestExecutionError(error_msg)
                        
            if not execution_ids:
                logger.warning("No actions were executed successfully")
                return None
                
            return execution_ids[-1]
            
        except Exception as e:
            logger.error(f"Error running actions: {str(e)}")
            # Log more details about the data structure
            logger.error(f"Setup data structure: {json.dumps(self.setup_data, indent=2)}")
            logger.error(f"Actions details type: {type(self.setup_data.get('actions_details'))}")
            raise TestExecutionError(f"Error running actions: {str(e)}")
        
    async def _poll_actions(self, execution_id) -> None:
        """
        Poll the actions status until it becomes succeeded or timeout is reached.
        
        Args:
            app_slug: The application slug
            action_id: The ID of the action to poll
            scenario_id: The scenario ID associated with the action
            
        Raises:
            TestExecutionError: If polling times out or encounters an error
        """
        POLL_INTERVAL = 10  # seconds
        TIMEOUT = 10 * 60  # 10 minutes in seconds
        
        start_time = time.time()
        polling_attempt = 1
        app_slug = self.setup_data['app_slug']  
        logger.info(f"Starting to poll action status for execution {execution_id}")
        
        while True:
            try:
                response = self.external_actions.get_action_status(app_slug, execution_id)
                elapsed_time = int(time.time() - start_time)
                
                if response.status_code == 200:
                    status_data = response.json()
                    current_status = status_data.get('status', 'unknown')
                    
                    logger.info(f"Polling attempt {polling_attempt}: Action {execution_id} status is '{current_status}' "
                            f"(Elapsed time: {elapsed_time}s)")
                    logger.debug(f"Full status response: {status_data}")
                    
                    if current_status == 'succeeded':
                        logger.info(f"✓ Action {execution_id} completed successfully after {polling_attempt} polling attempts")
                        break
                    elif current_status in ['failed', 'cancelled', 'error']:
                        error_msg = f"Action failed with status '{current_status}' after {polling_attempt} attempts"
                        logger.error(f"❌ {error_msg}")
                        raise TestExecutionError(error_msg)
                    elif time.time() - start_time > TIMEOUT:
                        error_msg = (f"Polling timed out after {polling_attempt} attempts: "
                                f"Action {execution_id} did not complete within {TIMEOUT/60} minutes")
                        logger.error(f"❌ {error_msg}")
                        raise TestExecutionError(error_msg)
                    else:
                        # Action is still in progress, wait and continue polling
                        await asyncio.sleep(POLL_INTERVAL)
                        polling_attempt += 1
                else:
                    error_msg = (f"Failed to get action status. "
                            f"Status code: {response.status_code}, Response: {response.text}")
                    logger.error(f"❌ {error_msg}")
                    raise TestExecutionError(error_msg)
                    
            except TestExecutionError:
                raise
            except Exception as e:
                error_msg = f"Error during action status polling: {str(e)}"
                logger.error(f"❌ {error_msg}")
                raise TestExecutionError(error_msg)
