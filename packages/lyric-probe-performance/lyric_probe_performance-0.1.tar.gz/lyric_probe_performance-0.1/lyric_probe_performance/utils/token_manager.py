# utils/token_manager.py

import threading
from typing import Optional
import requests
from base64 import b64encode
from utils.log_manager import setup_logger
from utils.exceptions import ConfigurationError, TestExecutionError
from routes import APIRoutes

logger = setup_logger(__name__)

class TokenManager:
    _instance = None
    _lock = threading.Lock()
    _token: Optional[str] = None
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    @property
    def token(self) -> Optional[str]:
        return self._token
    
    @token.setter 
    def token(self, value: str):
        """Thread-safe token setter."""
        with self._lock:
            self._token = value
            
    def create_token(self, client_id: str, client_secret: str, base_url: str) -> str:
        """Create a new token if one doesn't exist."""
        if self._token is None:
            with self._lock:
                if self._token is None:
                    try:
                        auth_str = f"{client_id}:{client_secret}"
                        encoded = b64encode(auth_str.encode()).decode()
                        headers = {
                            "Content-Type": "application/json",
                            "Authorization": f"Basic {encoded}"
                        }
                        payload = {
                            "clientId": client_id,
                            "clientSecret": client_secret
                        }
                        
                        logger.info("Creating new authentication token")
                        # Correctly use APIRoutes to get the token creation URL
                        token_url = APIRoutes.CREATE_TOKEN()
                        logger.debug(f"Token creation URL: {token_url}")
                        
                        response = requests.post(
                            token_url,
                            json=payload,
                            headers=headers
                        )
                        response.raise_for_status()
                        
                        token_data = response.json()
                        self._token = token_data.get("access_token")
                        if not self._token:
                            raise TestExecutionError("No access token in response")
                            
                        logger.info("Successfully created authentication token")
                        
                    except requests.exceptions.RequestException as e:
                        logger.error(f"Failed to create token: {str(e)}")
                        raise TestExecutionError(f"Token creation failed: {str(e)}")
                    except Exception as e:
                        logger.error(f"Unexpected error creating token: {str(e)}")
                        raise TestExecutionError(f"Token creation failed: {str(e)}")
                        
        return self._token

# Global token manager instance
token_manager = TokenManager()