from locust import SequentialTaskSet
from typing import Dict, Any, Optional
from utils.log_manager import setup_logger

logger = setup_logger(__name__)

class BaseTask(SequentialTaskSet):
    """Base task class with common functionality."""
    
    POLL_INTERVAL = 30  # seconds
    TIMEOUT = 30 * 60  # 30 minutes
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_data = getattr(self.user, 'setup_data', {})
        self.config = getattr(self.user, 'config', {})
        
    def _get_app_slug(self) -> str:
        """Get app slug from setup data."""
        return self.setup_data.get('app_slug', '')
        
    async def complete_task(self):
        """Mark task as completed."""
        self.user.task_completed = True
        self.interrupt(False)