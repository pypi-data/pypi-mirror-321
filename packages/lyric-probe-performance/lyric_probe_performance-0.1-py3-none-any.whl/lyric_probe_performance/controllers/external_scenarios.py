"""Controller for managing external scenarios."""
from typing import Any, Dict, Optional, List
import logging
from urllib.parse import urljoin
import aiohttp

from routes import APIRoutes
from utils.log_manager import setup_logger
from utils.exceptions import TestExecutionError

logger = setup_logger(__name__)

class ExternalScenarios:
    """Controller for managing external scenarios."""

    def __init__(self, api_client):
        """
        Initialize ExternalScenarios with an API client.

        Args:
            api_client: The client to make API requests.
        """
        self.api_client = api_client
        
    def get_scenarios(
        self,
        app_slug: str,
        state: Optional[str] = None,
        type: Optional[str] = None
    ) -> Any:
        """
        Retrieve scenarios for a given app with optional filters.

        Args:
            app_slug (str): The slug of the app.
            state (Optional[str]): Filter scenarios by state.
            type (Optional[str]): Filter scenarios by type.

        Returns:
            Any: The API response.
        """
        logger.info("Fetching scenarios for app: %s", app_slug)
        params = {}
        if state:
            params["state"] = state
        if type:
            params["type"] = type

        logger.debug("Request parameters: %s", params)
        return self.api_client.get(
            APIRoutes.GET_SCENARIOS(app_slug),
            params=params,
            name="get_scenarios"
        )

    def create_scenario(
        self,
        app_slug: str,
        scenario_payload: Dict[str, Any]
    ) -> Any:
        """
        Create a new scenario for a given app.

        Args:
            app_slug (str): The slug of the app.
            scenario_payload (Dict[str, Any]): The payload for the scenario.

        Returns:
            Any: The API response.
        """
        logger.info("Creating scenario for app: %s", app_slug)
        logger.debug("Scenario payload: %s", scenario_payload)
        
        return self.api_client.post(
            APIRoutes.CREATE_SCENARIO(app_slug),
            json=scenario_payload,
            name="create_scenario"
        )