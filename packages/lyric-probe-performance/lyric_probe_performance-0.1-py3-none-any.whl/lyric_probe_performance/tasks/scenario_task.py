import asyncio
import random
import time
from locust import task, between
from typing import Optional
from locust.exception import StopUser

from .base_task import BaseTask
from utils.log_manager import setup_logger
from controllers.external_scenarios import ExternalScenarios
from runner import TestExecutionError

logger = setup_logger(__name__)

class ScenarioCreationTask(BaseTask):
    """
    Enhanced Scenario Creation Task with improved error handling and robustness.
    
    Key improvements:
    - More detailed error logging
    - Improved error handling
    - Better state management
    """
    
    wait_time = between(1, 2)
    
    def __init__(self, user):
        super().__init__(user)
        self.external_scenarios = ExternalScenarios(self.user.client)
        self.scenario_id = None
        self.max_retries = 3
        self.retry_delay = 10  # seconds

    def _create_scenario(self):
        """
        Create a scenario with multiple retry mechanism.
        
        Returns:
            str: Created scenario ID
        
        Raises:
            StopUser: If scenario creation fails after max retries
        """
        try:
                unique_id = f"{int(time.time()) % 1000}{random.randint(0, 9)}"
                scenario_name = self.setup_data['signature_scenario_name']
                app_slug = self.setup_data['app_slug']
                scenario_payload = {
                    "displayName": f"{scenario_name} - {unique_id}",
                    "description": "Performance test scenario creation"
                }
                
                # Get the response synchronously
                create_scenario_response = self.external_scenarios.create_scenario(app_slug, scenario_payload)
                
                # Log response for debugging
                response_data = create_scenario_response.json()
                logger.info(f"Create scenario response: {response_data}")
                
                if create_scenario_response.status_code == 201:
                    # Handle both list and single object responses
                    data = response_data[0] if isinstance(response_data, list) else response_data
                    scenario_id = data.get('id')
                    self.scenario_id = scenario_id
                    logger.info(f"Scenario created with ID: {scenario_id}")
                    return self.scenario_id
                else:
                    logger.error(f"Failed to create scenario. Status: {create_scenario_response.status_code}, Response: {create_scenario_response.text}")
                    raise StopUser(f"Failed to create scenario)")
            
        except Exception as e:
                raise StopUser(f"Scenario creation failed: {str(e)}")

    async def _poll_scenario_status(self, scenario_id, timeout=1200): # 20mins
        """
        Asynchronously poll the scenario status with improved error handling and retry mechanism.
        
        Args:
            scenario_id: The ID of the scenario to poll
            timeout: Maximum time to wait (in seconds)
            
        Raises:
            StopUser: If polling fails or times out
        """
        POLL_INTERVAL = 30  # seconds
        MAX_POLLING_ATTEMPTS = int(timeout / POLL_INTERVAL) + 1
        
        # Define state categories
        SUCCESS_STATES = {'active'}
        INTERMEDIATE_STATES = {'copying', 'updating', 'frozen'}
        FAILURE_STATES = {'copyFailed', 'updateFailed'}
        
        start_time = time.time()
        polling_attempt = 1
        logger.info(f"Starting to poll for scenario {scenario_id} status")
        
        try:
            while polling_attempt <= MAX_POLLING_ATTEMPTS:
                elapsed_time = int(time.time() - start_time)
                app_slug = self.setup_data['app_slug']
                
                # Get scenarios response
                try:
                    response = self.external_scenarios.get_scenarios(app_slug, None, 'user')
                    scenarios = response.json()
                except Exception as e:
                    logger.error(f"Error fetching scenarios (Attempt {polling_attempt}): {str(e)}")
                    if polling_attempt < MAX_POLLING_ATTEMPTS:
                        await asyncio.sleep(POLL_INTERVAL)
                        polling_attempt += 1
                        continue
                    raise StopUser(f"Failed to fetch scenarios after {MAX_POLLING_ATTEMPTS} attempts")

                current_scenario = next((s for s in scenarios if s.get('id') == scenario_id), None)

                if not current_scenario:
                    if polling_attempt < MAX_POLLING_ATTEMPTS:
                        logger.warning(f"Scenario {scenario_id} not found. Retrying.")
                        await asyncio.sleep(POLL_INTERVAL)
                        polling_attempt += 1
                        continue
                    raise StopUser(f"Scenario {scenario_id} not found after {MAX_POLLING_ATTEMPTS} attempts")

                current_state = current_scenario.get('state', 'Unknown')

                if current_state in SUCCESS_STATES:
                    logger.info(f"Scenario {scenario_id} is active after {elapsed_time:.2f} seconds.")
                    return

                if current_state in FAILURE_STATES:
                    raise StopUser(f"Scenario {scenario_id} failed with state: {current_state}.")

                if elapsed_time > timeout:
                    raise StopUser(f"Polling timed out for scenario {scenario_id}. Current state: {current_state}.")

                logger.info(f"Scenario {scenario_id} is in state '{current_state}'. Attempt {polling_attempt}. Retrying in {POLL_INTERVAL}s.")
                
                # Async sleep to prevent blocking
                time.sleep(POLL_INTERVAL) 
                polling_attempt += 1

            # If we exit the loop without returning, it means we've exhausted all attempts
            raise StopUser(f"Polling failed for scenario {scenario_id} after {MAX_POLLING_ATTEMPTS} attempts")

        except StopUser:
            # Re-raise StopUser to halt the user's execution
            raise
        except Exception as e:
            logger.error(f"Unexpected error during polling: {str(e)}")
            raise StopUser(f"Polling error: {str(e)}")

    @task
    async def execute_scenario(self):
        """
        Create and monitor a scenario with comprehensive error handling.
        
        Responsibilities:
        - Create scenario
        - Poll scenario status
        - Handle errors gracefully
        """
        try:
            logger.info(f"User {id(self)} starting scenario creation")
            
            # Create scenario with retry mechanism
            self.scenario_id = self._create_scenario()
            
            # Poll scenario status
            await self._poll_scenario_status(self.scenario_id)
            # Store the scenario ID in the user object
            self.user.scenario_id = self.scenario_id
            # Logging for successful scenario creation and activation
            logger.info(f"Scenario {self.scenario_id} created and activated successfully")
        
        except StopUser as e:
            # Log and re-raise StopUser exceptions
            logger.warning(f"User execution stopped: {str(e)}")
            raise
        except Exception as e:
            # Catch and log any unexpected errors
            logger.error(f"Unexpected error in scenario execution: {str(e)}")
            raise StopUser(f"Scenario execution failed: {str(e)}")