"""Controller for external token operations."""
from typing import Dict, Any
import logging

from routes import APIRoutes
from .base_controller import BaseController

from utils.log_manager import setup_logger

logger = setup_logger(__name__)

class ExternalToken(BaseController):
    """External token controller."""

    def create_token(self, client_id: str, client_secret: str) -> Dict[str, Any]:
        """
        Create a new token.

        Args:
            client_id: Client ID for authentication.
            client_secret: Client secret for authentication.

        Returns:
            A dictionary containing the token details or an error message.
        """
        payload = {
            'clientId': client_id,
            'clientSecret': client_secret
        }
        try:
            logger.debug(f"Creating token with payload: {payload}")
            
            response = self.client.post(
                APIRoutes.CREATE_TOKEN,
                json=payload,
                name="create_token"
            )
            
            if response.ok:
                logger.info("Token created successfully.")
                return response.json()
            else:
                logger.error(f"Failed to create token. Status: {response.status_code}, Response: {response.text}")
                return {
                    "error": "Failed to create token",
                    "status": response.status_code,
                    "details": response.text
                }
        except Exception as e:
            logger.error(f"Error during token creation: {str(e)}")
            return {"error": str(e)}
