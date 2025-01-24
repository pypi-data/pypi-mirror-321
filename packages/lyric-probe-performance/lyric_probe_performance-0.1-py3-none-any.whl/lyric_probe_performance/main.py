import logging
import sys
from locust import events
import asyncio
import nest_asyncio
from datetime import datetime

from tasks.user_task import UserFlow
from utils.log_manager import setup_logger
from utils.config_loader import ConfigLoader

nest_asyncio.apply()
logger = setup_logger(__name__)

# Set async mode for the environment
from locust.env import Environment
Environment.async_mode = True

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Handle test start event."""
    try:
        # Load and validate config at startup
        config = ConfigLoader().get_config()
        logger.info("Test configuration loaded successfully")
        
        # Ensure async mode is set
        environment.async_mode = True
        
        # Log the target number of users from config
        target_users = config.get('test_config', {}).get('users', 0)
        target_spawn_rate = config.get('test_config', {}).get('spawn_rate', 1)
        logger.info(f"Starting performance test (Target: {target_users} users, Spawn rate: {target_spawn_rate}/s)")
        
    except Exception as e:
        logger.error(f"Test startup failed: {str(e)}")
        environment.runner.quit()

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    """Called when the locust environment is initialized."""
    logger.info("Locust environment initialized")

@events.spawning_complete.add_listener
def on_spawning_complete(user_count, **kwargs):
    """Called when all users have been spawned."""
    logger.info(f"Spawning complete - All {user_count} users started")
# Export test class
__all__ = ['UserFlow']
