"""Controller for external actions."""
import logging
from typing import Any, Dict, List, Optional

from routes import APIRoutes
from .base_controller import BaseController
from utils.log_manager import setup_logger

logger = setup_logger(__name__)

class ExternalActions(BaseController):
    """Controller for managing external actions."""

    def get_actions(self, app_slug: str) -> Any:
        """
        Fetch all actions for a given application.

        Args:
            app_slug (str): The unique identifier for the application.

        Returns:
            Any: The HTTP response object containing the actions.
        """
        logger.info("Fetching actions for app slug: %s", app_slug)
        response = self.client.get(APIRoutes.GET_ACTIONS(app_slug))
        return response

    def run_action(
        self, 
        app_slug: str, 
        action_id: str, 
        scenario_id: str, 
        parameters: Optional[Dict] = None
    ) -> Any:
        """
        Execute a specified action.

        Args:
            app_slug (str): The unique identifier for the application.
            action_id (str): The ID of the action to be executed.
            scenario_id (str): The ID of the scenario associated with the action.
            parameters (Optional[Dict]): Additional parameters for the action.

        Returns:
            Any: The HTTP response object from the action execution.
        """
        payload = {
            "actionId": action_id,
            "scenarioId": scenario_id,
            **({"parameters": parameters} if parameters else {})
        }
        logger.info("Running action: %s with payload: %s", action_id, payload)
        return self.client.post(APIRoutes.RUN_ACTION(app_slug), json=payload)

    def get_action_status(self, app_slug: str, execution_id: str) -> Any:
        """
        Get the status of an executed action.

        Args:
            app_slug (str): The unique identifier for the application.
            execution_id (str): The execution ID of the action.

        Returns:
            Any: The HTTP response object containing the status.
        """
        logger.info("Fetching status for action execution ID: %s", execution_id)
        return self.client.get(APIRoutes.GET_ACTION_STATUS(app_slug, execution_id))

    def cancel_action(self, app_slug: str, execution_id: str) -> Any:
        """
        Cancel an ongoing action.

        Args:
            app_slug (str): The unique identifier for the application.
            execution_id (str): The execution ID of the action.

        Returns:
            Any: The HTTP response object after cancellation.
        """
        logger.info("Cancelling action execution ID: %s", execution_id)
        return self.client.get(APIRoutes.CANCEL_ACTION(app_slug, execution_id))

    def run_actions(
        self,
        app_slug: str,
        action_id: str,
        scenario_id: str,
        parameters: Optional[List[Dict[str, Any]]] = None,
    ) -> Any:
        """
        Execute an action for a specific scenario with optional parameters.

        Args:
            app_slug (str): The slug of the app.
            action_id (str): The ID of the action to run.
            scenario_id (str): The ID of the scenario to associate the action with.
            parameters (Optional[List[Dict[str, Any]]]): Additional parameters for the action.

        Returns:
            Any: The API response.
        """
        payload = {
            "actionId": action_id,
            "scenarioId": scenario_id,
        }

        if parameters:
            payload["parameters"] = parameters

        logger.info("Running action %s for scenario %s in app %s", action_id, scenario_id, app_slug)
        logger.debug("Payload: %s", payload)
        # Changed from self.api_client to self.client to match BaseController
        return self.client.post(
            APIRoutes.RUN_ACTION(app_slug),
            json=payload,
        )