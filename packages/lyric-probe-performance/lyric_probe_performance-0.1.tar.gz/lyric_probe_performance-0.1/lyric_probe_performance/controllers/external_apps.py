"""Controller for external apps."""
from typing import Dict, Any, Optional
import logging

from routes import APIRoutes
from .base_controller import BaseController
from utils.log_manager import setup_logger

logger = setup_logger(__name__)

class ExternalApps(BaseController):
    """Controller for managing external apps."""

    def get_app(self, sequence_id: str) -> Dict[str, Any]:
        """
        Fetch application details using the sequence ID.

        Args:
            sequence_id (str): The unique identifier for the application.

        Returns:
            Dict[str, Any]: Application details, or an empty dictionary if not found.
        """
        logger.info(f"Fetching app details for sequence ID: {sequence_id}")
        try:
            response = self.client.get(APIRoutes.GET_APP(sequence_id))
            if response.ok:
                return response.json()
            else:
                logger.error(f"Failed to get app details. Status: {response.status_code}, Response: {response.text}")
                return {}
        except Exception as e:
            logger.error(f"Error getting app details: {str(e)}")
            return {}