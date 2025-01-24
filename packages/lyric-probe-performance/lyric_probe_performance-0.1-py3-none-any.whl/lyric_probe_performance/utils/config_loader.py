# lyric_probe_performance/utils/config_loader.py

import os
from pathlib import Path
from typing import Dict, Any, Optional, Union
from functools import lru_cache

import yaml
from yaml.error import YAMLError
from utils.exceptions import ConfigurationError, TestExecutionError
from utils.log_manager import setup_logger

logger = setup_logger(__name__)

class ConfigLoader:
    """Handles loading and validation of YAML configuration files."""
    
    DEFAULT_CONFIG_PATH = 'config.yaml'
    REQUIRED_FIELDS = {'client_id', 'client_secret'}

    def __init__(
        self, 
        config_path: Optional[Union[str, Path]] = None,
        validate: bool = True
    ) -> None:
        try:
            self.config_path = Path(config_path or self.DEFAULT_CONFIG_PATH)
            self.config = self._load_config()
            
            if validate:
                self._validate_config()
                
        except Exception as e:
            logger.error(f"Failed to initialize configuration: {str(e)}")
            raise ConfigurationError("Configuration initialization failed") from e
            

    def _load_config(self) -> Dict[str, Any]:
        """Load the configuration from a YAML file."""
        try:
            if not self.config_path.exists():
                raise TestExecutionError(
                    f"Configuration file not found: {self.config_path}"
                )

            with self.config_path.open('r', encoding='utf-8') as file:
                config = yaml.safe_load(file)

            if not isinstance(config, dict):
                raise ConfigurationError("Configuration must be a dictionary")

            return self._process_config(config)

        except YAMLError as e:
            logger.error(f"YAML parsing error: {str(e)}")
            raise ConfigurationError("Failed to parse YAML configuration") from e
        except Exception as e:
            logger.error(f"Failed to load configuration: {str(e)}")
            raise ConfigurationError("Configuration loading failed") from e

    def _process_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Process and enhance the loaded configuration."""
        try:
            # Environment variable overrides
            for key in config:
                env_value = os.getenv(f"APP_{key.upper()}")
                if env_value is not None:
                    config[key] = env_value

            return config

        except Exception as e:
            logger.error(f"Failed to process configuration: {str(e)}")
            raise ConfigurationError("Configuration processing failed") from e

    def _validate_config(self) -> None:
        """Validate the loaded configuration."""
        missing_fields = self.REQUIRED_FIELDS - set(self.config.keys())
        if missing_fields:
            raise ConfigurationError(
                f"Missing required configuration fields: {missing_fields}"
            )

        self._validate_credentials()

    def _validate_credentials(self) -> None:
        """Validate credential-related configuration values."""
        for field in ('client_id', 'client_secret'):
            value = self.config.get(field)
            if not value or not isinstance(value, str):
                raise ConfigurationError(
                    f"Invalid {field} configuration: must be non-empty string"
                )

    @lru_cache(maxsize=1)
    def get_config(self) -> Dict[str, Any]:
        """Get the loaded configuration."""
        return self.config.copy()

    def get_value(self, key: str, default: Any = None) -> Any:
        """Get a specific configuration value."""
        return self.config.get(key, default)

    def reload(self) -> None:
        """Reload the configuration from file."""
        try:
            self.config = self._load_config()
            self._validate_config()
            self.get_config.cache_clear()  # Clear the cache
            logger.info("Configuration reloaded successfully")
        except Exception as e:
            logger.error(f"Failed to reload configuration: {str(e)}")
            raise ConfigurationError("Configuration reload failed") from e