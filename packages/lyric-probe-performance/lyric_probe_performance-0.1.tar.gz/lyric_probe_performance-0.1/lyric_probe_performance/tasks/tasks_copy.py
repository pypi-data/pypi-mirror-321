import json
import os
import time
import random
from typing import Dict, Any, Optional
import logging
import asyncio
from controllers.external_actions import ExternalActions
from controllers.external_scenarios import ExternalScenarios
from controllers.external_tables import ExternalTables
from utils.config_loader import ConfigLoader
from utils.log_manager import setup_logger
from runner import TestExecutionError
from locust.exception import StopUser
from utils.setup_manager import setup_manager
from utils.token_manager import token_manager

logger = setup_logger(__name__)

class CreateAndRunScenarioTask1:
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

    def on_start(self):
        """Initialize the user session."""
        try:
            # Load config
            config_loader = ConfigLoader()
            self.config = config_loader.get_config()
            
            # Set base URL
            self.host = self.config.get('base_url', '').rstrip('/')
            
            # Get token
            token = token_manager.create_token(
                self.config['client_id'],
                self.config['client_secret'],
                self.host
            )
            if token:
                self.client.headers.update({
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                })

            # Perform initial setup
            self.setup_data = self.perform_setup()
            logger.info("User session initialized successfully")
            
        except Exception as e:
            logger.error(f"User initialization failed: {str(e)}")
            self.environment.runner.quit()

    def perform_setup(self):
        """Setup method."""
        return setup_manager.perform_setup(
            self.client,
            self.config['client_id'],
            self.config['client_secret'],
            self.config['sequence_id']
        )
    
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
    
    def _create_scenario(self):
        """Create a scenario and return its ID."""
        try:
            unique_id = f"{int(time.time()) % 1000}{random.randint(0, 9)}"
            scenario_name = self.setup_data['signature_scenario_name']
            app_slug = self.setup_data['app_slug']
            scenario_payload = {
                "displayName": f"{scenario_name} - {unique_id}",
                "description": "Performance test scenario creation"
            }
            
            create_scenario_response = self.external_scenarios.create_scenario(app_slug, scenario_payload)
            response_data = create_scenario_response.json()
            logger.info(f"Create scenario response: {response_data}")
            
            if create_scenario_response.status_code == 201:
                data = response_data[0] if isinstance(response_data, list) else response_data
                scenario_id = data.get('id')
                if not scenario_id:
                    raise StopUser("Scenario creation failed: ID not found in response.")
                logger.info(f"Scenario created with ID: {scenario_id}")
                return scenario_id
            else:
                logger.error(f"Failed to create scenario. Status: {create_scenario_response.status_code}, Response: {create_scenario_response.text}")
                raise StopUser(f"Failed to create scenario. Status code: {create_scenario_response.status_code}")
        except StopUser as e:
            logger.error(f"Stopping user: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during scenario creation: {str(e)}")
            raise StopUser("Unexpected error during scenario creation.")

    async def _poll_scenario_status(self, scenario_id) -> None:
        """
        Poll the scenario status until it reaches a final state (active/failed) or timeout is reached.
        
        Args:
            external_scenarios: ExternalScenarios instance
            app_slug: The application slug
            scenario_id: The ID of the scenario to poll
            
        Raises:
            TestExecutionError: If polling times out or encounters an error
        """
        POLL_INTERVAL = 30  # seconds
        TIMEOUT = 10 * 60  # 10 minutes in seconds
        
        # Define state categories
        SUCCESS_STATES = {'active'}
        INTERMEDIATE_STATES = {'copying', 'updating', 'frozen'}
        FAILURE_STATES = {'copyFailed', 'updateFailed'}
        
        start_time = time.time()
        polling_attempt = 1
        logger.info(f"Starting to poll for scenario {scenario_id} status")
        
        while True:
            try:
                elapsed_time = int(time.time() - start_time)
                app_slug = self.setup_data['app_slug']
                # Get scenarios response - try both with and without state filter
                response = self.external_scenarios.get_scenarios(app_slug, None, 'user')
                scenarios = response.json()
                
                current_scenario = next((s for s in scenarios if s.get('id') == scenario_id), None)

                if not current_scenario:
                    raise StopUser(f"Scenario {scenario_id} not found.")

                current_state = current_scenario.get('state', 'Unknown')

                if current_state in SUCCESS_STATES:
                    logger.info(f"Scenario {scenario_id} is active after {elapsed_time:.2f} seconds.")
                    break
                elif current_state in FAILURE_STATES:
                        raise StopUser(f"Scenario {scenario_id} failed with state: {current_state}.")
                elif elapsed_time > TIMEOUT:
                        raise StopUser(f"Polling timed out for scenario {scenario_id}. Current state: {current_state}.")
                else:
                        logger.info(f"Scenario {scenario_id} is in state '{current_state}'. Retrying in {POLL_INTERVAL}s.")
                        await asyncio.sleep(POLL_INTERVAL)
            except StopUser as e:
                    logger.error(f"Stopping user: {str(e)}")
                    raise
            except Exception as e:
                    logger.error(f"Unexpected error during polling: {str(e)}")
                    raise StopUser("Unexpected error during polling.")

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

    async def _run_actions(self, scenario_id: str) -> Optional[str]:
        """Run actions for the scenario based on configuration."""
        logger.info("Starting to run actions...")
        try:
            app_slug = self.setup_data['app_slug']
            config = ConfigLoader().get_config()
            configured_actions = config.get('actions', [])
            if not configured_actions:
                logger.warning("No actions configured in the config file.")
                return None

            actions_details = self.setup_data.get('actions_details', {})
            action_lookup = {
                action['name']: action['referenceId']
                for action in actions_details.get('actions', [])
                if action.get('isVisible', False) and action.get('name') and action.get('referenceId')
            }

            logger.debug(f"Available actions: {json.dumps(action_lookup, indent=2)}")
            execution_ids = []

            for config_action in configured_actions:
                action_name = config_action.get('name')
                if not action_name:
                    logger.warning("Action name missing in configuration.")
                    continue

                action_id = action_lookup.get(action_name)
                if not action_id:
                    logger.warning(f"No matching action found for: {action_name}")
                    continue

                response = self.external_actions.run_actions(app_slug, action_id, scenario_id)
                if response.status_code == 201:
                    execution_id = response.json().get('executionId')
                    if execution_id:
                        execution_ids.append(execution_id)
                        logger.info(f"Action {action_name} started successfully with Execution ID: {execution_id}")
                else:
                    raise StopUser(f"Failed to execute action {action_name}: {response.status_code} - {response.text}")

            return execution_ids[-1] if execution_ids else None

        except Exception as e:
            logger.error(f"Error running actions: {str(e)}")
            raise StopUser(f"Error running actions: {str(e)}")

    async def _poll_actions(self, execution_id: str) -> None:
        """Poll the action status until it completes or times out."""
        POLL_INTERVAL = 10
        TIMEOUT = 10 * 60
        start_time = time.time()
        app_slug = self.setup_data['app_slug']

        logger.info(f"Starting to poll status for execution ID: {execution_id}")
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > TIMEOUT:
                raise StopUser(f"Action polling timed out after {TIMEOUT / 60:.1f} minutes.")

            response = self.external_actions.get_action_status(app_slug, execution_id)
            if response.status_code == 200:
                status = response.json().get('status', 'unknown')
                logger.info(f"Polling status for execution ID {execution_id}: {status} (Elapsed: {elapsed_time:.2f}s)")

                if status == 'succeeded':
                    logger.info(f"Action {execution_id} succeeded.")
                    break
                elif status in {'failed', 'cancelled', 'error'}:
                    raise StopUser(f"Action {execution_id} failed with status: {status}.")
            else:
                raise StopUser(f"Failed to poll action status: {response.status_code} - {response.text}")

            await asyncio.sleep(POLL_INTERVAL)

