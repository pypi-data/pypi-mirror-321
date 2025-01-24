import asyncio
import json
import time
from locust import task, between
from typing import Dict, Any, Optional
from locust.exception import StopUser

from utils.config_loader import ConfigLoader
from utils.log_manager import setup_logger
from controllers.external_actions import ExternalActions
from .base_task import BaseTask

logger = setup_logger(__name__)


class ActionExecutionTask(BaseTask):
    """Task for running and monitoring actions."""

    wait_time = between(1, 2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.external_actions = ExternalActions(self.user.client)
    
    @task
    async def execute_actions(self):
        """Main task to execute actions."""
        try:
            logger.info(f"User {id(self)} entered execute_actions")

            if not self.user.scenario_id:
                logger.error("No scenario ID provided for actions.")
                raise StopUser("Scenario ID is required to execute actions.")
             # Run actions if action settings exist
            actions_details = self.setup_data.get('actions_details', {})
            if actions_details and actions_details.get('actions'):
                logger.info("Running actions for scenario")
                execution_id = await self._run_actions(self.user.scenario_id)
                if execution_id:
                    await self._poll_actions(execution_id)
                    self.complete_task()
                    logger.info(f"User {id(self)} action execution completed successfully.")
            else:
                logger.info("No actions configured to run")
        except StopUser as stop_exception:
            logger.error(f"Critical error: {stop_exception}")
            raise StopUser(f"Critical error: {stop_exception}")

        except Exception as e:
            logger.error(f"Action execution failed: {str(e)}")
            raise StopUser(f"Stopping user due to error: {str(e)}")

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
        TIMEOUT = 20 * 60 # 20 mins
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

