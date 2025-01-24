from typing import Any
import logging
from urllib.parse import urljoin

from utils.exceptions import ConfigurationError, TestExecutionError
from utils.log_manager import setup_logger

logger = setup_logger(__name__)

class BaseController:
    """A base controller for HTTP operations, providing reusable functionality."""

    def __init__(self, client: Any):
        """
        Initialize the controller with an HTTP client.

        Args:
            client (Any): An HTTP client instance with a `base_url` attribute.

        Raises:
            ValueError: If the client lacks a valid `base_url` attribute.
        """
        if not isinstance(getattr(client, "base_url", None), str):
            raise TestExecutionError("Base URL is missing in the configuration.")
        self.client = client
        logger.debug("Controller initialized with base URL: %s", self.client.base_url)

    def _build_url(self, path: str) -> str:
        """
        Construct a full URL by appending the given path to the client's base URL.

        Args:
            path (str): The endpoint path to append to the base URL.

        Returns:
            str: The constructed full URL.
        """
        if not isinstance(path, str):
           raise TestExecutionError("Path must be a string.")

        # Construct the URL using urljoin for safety and robustness
        base_url = self.client.base_url.rstrip('/') + '/'
        full_url = urljoin(base_url, path.lstrip('/'))
        logger.debug("Constructed URL: %s", full_url)
        return full_url
