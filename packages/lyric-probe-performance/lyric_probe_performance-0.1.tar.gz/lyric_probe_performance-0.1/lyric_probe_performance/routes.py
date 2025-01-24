"""API route definitions for API performance testing."""

import logging
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import urljoin
from utils.config_loader import ConfigLoader
from utils.log_manager import setup_logger

logger = setup_logger(__name__)

@dataclass
class BaseURLConfig:
    """Configuration for API base URLs."""
    base_url: str = ''
    
    def __init__(self) -> None:
        config_loader = ConfigLoader()
        config = config_loader.get_config()
        self.base_url = config.get('base_url', '').rstrip('/')
        if not self.base_url:
            raise ValueError("base_url is not set in config.yaml")
        logger.debug(f"Initialized BaseURLConfig with base_url: {self.base_url}")

@dataclass
class APIRoutes:
    """Centralized API route definitions."""
    
    config: BaseURLConfig = field(default_factory=BaseURLConfig)
    API_PREFIX: str = '/lyapi'
    
    @classmethod
    def _build_url(cls, path: str) -> str:
        """Build full URL from base URL and path."""
        config = BaseURLConfig()
        url = urljoin(config.base_url, path.lstrip('/'))
        logger.debug(f"Built URL '{url}' from path '{path}'")
        return url
    
    @classmethod
    def CREATE_TOKEN(cls) -> str:
        url = cls._build_url('/lyapi/tokens/create-token')
        logger.debug(f"Generated CREATE_TOKEN URL: {url}")
        return url

    @classmethod
    def GET_APP(cls, sequence_id: str) -> str:
        return cls._build_url(f'/lyapi/apps/get-app/{sequence_id}')
    
    @classmethod
    def GET_TABLES(cls, app_slug: str) -> str:
        return cls._build_url(f'/lyapi/table/{app_slug}')
    
    @classmethod
    def UPLOAD_TABLE_DATA(cls, app_slug: str) -> str:
        return cls._build_url(f'/lyapi/table/upload-csv/{app_slug}')
    
    @classmethod
    def DOWNLOAD_TABLE_DATA(cls, app_slug: str) -> str:
        return cls._build_url(f'/lyapi/table/download/{app_slug}')
    
    @classmethod
    def GET_TABLE_DETAILS(cls, app_slug: str, table_id: str) -> str:
        return cls._build_url(f'/lyapi/table/{app_slug}/{table_id}')
    
    @classmethod
    def GET_SCENARIOS(cls, app_slug: str) -> str:
        return cls._build_url(f'/lyapi/scenarios/get-scenarios/{app_slug}')
    
    @classmethod
    def CREATE_SCENARIO(cls, app_slug: str) -> str:
        return cls._build_url(f'/lyapi/scenarios/create-scenario/{app_slug}')
    
    @classmethod
    def DELETE_SCENARIOS(cls, app_slug: str) -> str:
        return cls._build_url(f'/lyapi/scenarios/delete-scenarios/{app_slug}')
    
    @classmethod
    def GET_ACTIONS(cls, app_slug: str) -> str:
        return cls._build_url(f'/lyapi/actions/get-actions/{app_slug}')
    
    @classmethod
    def RUN_ACTION(cls, app_slug: str) -> str:
        return cls._build_url(f'/lyapi/actions/run-action/{app_slug}')
    
    @classmethod
    def GET_ACTION_STATUS(cls, app_slug: str, execution_id: str) -> str:
        return cls._build_url(f'/lyapi/actions/get-action-status/{app_slug}/{execution_id}')
    
    @classmethod
    def CANCEL_ACTION(cls, app_slug: str, execution_id: str) -> str:
        return cls._build_url(f'/lyapi/actions/cancel-action/{app_slug}/{execution_id}')