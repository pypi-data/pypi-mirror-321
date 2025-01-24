"""Authentication manager for handling external service authentication."""
import logging
import ssl
from base64 import b64encode
from dataclasses import dataclass
from typing import Optional, Dict, Any
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from utils.exceptions import ConfigurationError, TestExecutionError
from utils.config_loader import ConfigLoader
from routes import APIRoutes
from utils.log_manager import setup_logger

logger = setup_logger(__name__)

@dataclass
class AuthCredentials:
    """Container for authentication credentials."""
    client_id: str
    client_secret: str

    def __post_init__(self) -> None:
        if not self.client_id or not self.client_secret:
            raise TestExecutionError("Both client_id and client_secret must be provided")

class AuthManager:
    def __init__(
        self, 
        client: Any,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None
    ) -> None:
        self.client = client
        self.credentials = self._initialize_credentials(client_id, client_secret)
        logger.debug(f"Initialized AuthManager with client type: {type(client)}")

    def _initialize_credentials(self, client_id: Optional[str], client_secret: Optional[str]) -> AuthCredentials:
        if not (client_id and client_secret):
            try:
                config = ConfigLoader().get_config()
                client_id = config['client_id']
                client_secret = config['client_secret']
                logger.debug("Successfully loaded credentials from config")
            except (KeyError, Exception) as e:
                logger.error(f"Failed to load credentials from config: {str(e)}")
                raise TestExecutionError("Failed to initialize credentials") from e

        return AuthCredentials(client_id=client_id, client_secret=client_secret)

    async def authenticate(self) -> None:
        """Authenticate user and set up headers."""
        try:
            logger.info("Starting authentication process...")
            
            auth_header = self._generate_auth_header()
            headers = self._build_headers(auth_header)
            payload = self._build_payload()
            
            # Get token URL
            token_url = APIRoutes.CREATE_TOKEN()
            logger.info(f"Making authentication request to: {token_url}")
            logger.debug(f"Request headers: {headers}")
            logger.debug(f"Request payload: {payload}")

            # Create a session with retry strategy
            session = requests.Session()
            retries = Retry(
                total=3,
                backoff_factor=0.5,
                status_forcelist=[500, 502, 503, 504]
            )
            session.mount('https://', HTTPAdapter(max_retries=retries))
            
            # Make the request
            try:
                response = self.client.post(
                    url=token_url,
                    json=payload,
                    headers=headers,
                    name="create_token",
                    verify=True  # Enable SSL verification
                )
                logger.debug(f"Response status code: {response.status_code}")
                
                if hasattr(response, 'headers'):
                    logger.debug(f"Response headers: {response.headers}")
                
                if response.status_code in {200, 201}:
                    try:
                        data = response.json()
                        token = data.get("access_token")
                        if not token:
                            raise TestExecutionError("No access token in response")
                        
                        self.client.headers.update({
                            "Authorization": f"Bearer {token}",
                            "Content-Type": "application/json"
                        })
                        logger.info("Authentication successful")
                    except Exception as e:
                        logger.error(f"Failed to process authentication response: {str(e)}")
                        raise AuthenticationError("Invalid authentication response") from e
                else:
                    error_msg = response.text if response.text else f"HTTP {response.status_code}"
                    logger.error(f"Authentication failed with status {response.status_code}: {error_msg}")
                    if response.status_code == 0:
                        logger.error("HTTP 0 indicates the request could not be made. Check the URL and network connection.")
                    raise AuthenticationError(f"Authentication failed: {error_msg}")
                    
            except requests.exceptions.SSLError as e:
                logger.error(f"SSL Error occurred: {str(e)}")
                raise AuthenticationError("SSL verification failed") from e
            except requests.exceptions.ConnectionError as e:
                logger.error(f"Connection Error occurred: {str(e)}")
                raise AuthenticationError("Failed to connect to the server") from e
            except Exception as e:
                logger.error(f"Request failed: {str(e)}")
                raise AuthenticationError(f"Request failed: {str(e)}") from e

        except Exception as e:
            logger.error(f"Authentication error: {str(e)}", exc_info=True)
            raise AuthenticationError(f"Authentication failed: {str(e)}") from e

    def _generate_auth_header(self) -> str:
        """Generate base64 encoded authentication header."""
        auth_str = f"{self.credentials.client_id}:{self.credentials.client_secret}"
        encoded = b64encode(auth_str.encode()).decode()
        logger.debug(f"Generated auth header (first 10 chars): {encoded[:10]}...")
        return encoded

    def _build_headers(self, auth_header: str) -> Dict[str, str]:
        """Build headers for authentication request."""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Basic {auth_header}"
        }

    def _build_payload(self) -> Dict[str, str]:
        """Build payload for authentication request."""
        return {
            "clientId": self.credentials.client_id,
            "clientSecret": self.credentials.client_secret
        }

class AuthenticationError(TestExecutionError):
    """Custom exception for authentication-related errors."""
    pass