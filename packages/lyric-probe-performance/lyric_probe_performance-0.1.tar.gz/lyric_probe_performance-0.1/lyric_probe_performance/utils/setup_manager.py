# utils/setup_manager.py

import threading
from typing import Optional, Dict, Any
import asyncio
import logging

from lyric_probe_performance.utils.exceptions import TestExecutionError
from utils.log_manager import setup_logger
from utils.base_setup import BaseSetUp

logger = setup_logger(__name__)

class SetupManager:
    """
    Manages the setup process for the performance test.
    Ensures setup is performed only once and cached for subsequent users.
    """
    
    def __init__(self):
        """Initialize the SetupManager with thread-safe mechanisms."""
        self._lock = threading.Lock()
        self._setup_data: Optional[Dict[str, Any]] = None
        self._setup_error: Optional[str] = None
        self._setup_in_progress = threading.Event()
        self._setup_completed = threading.Event()
        
    @property
    def setup_data(self) -> Optional[Dict[str, Any]]:
        """Thread-safe access to setup data."""
        with self._lock:
            return self._setup_data

    def get_setup_data(self) -> Optional[Dict[str, Any]]:
        """Alternative method to get setup data for backward compatibility."""
        return self.setup_data

    def perform_setup(
        self, 
        client, 
        client_id: str, 
        client_secret: str, 
        sequence_id: str
    ) -> Dict[str, Any]:
        """
        Synchronous wrapper for async setup.
        """
        # If setup already completed, return cached data
        if self._setup_completed.is_set():
            return self._setup_data

        # If setup already failed, don't retry
        if self._setup_error:
            raise TestExecutionError(f"Cannot proceed - Base Setup failed: {self._setup_error}")

        # Create event loop for async setup if needed
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        try:
            return loop.run_until_complete(self._async_perform_setup(
                client, 
                client_id, 
                client_secret, 
                sequence_id
            ))
        finally:
            if not loop.is_running():
                loop.close()

    async def _async_perform_setup(
        self,
        client,
        client_id: str,
        client_secret: str,
        sequence_id: str
    ) -> Dict[str, Any]:
        """
        Async implementation of setup process.
        """
        # Try to acquire setup lock
        if not self._setup_in_progress.is_set():
            with self._lock:
                if not self._setup_in_progress.is_set():
                    self._setup_in_progress.set()
                    try:
                        logger.info("Starting initial setup process...")
                        setup = BaseSetUp(client, client_id, client_secret, sequence_id)
                        self._setup_data = await setup.setup()
                        logger.info("Initial setup completed successfully")
                        self._setup_completed.set()
                        return self._setup_data
                    except Exception as e:
                        self._setup_error = str(e)
                        logger.error(f"Failed to perform base setup: {str(e)}")
                        raise TestExecutionError(f"Base Setup failed: {str(e)}")
                    finally:
                        self._setup_in_progress.clear()

        # Wait for setup to complete if another thread is performing it
        while not self._setup_completed.wait(timeout=60):
            logger.info("Waiting for setup to complete...")
            if self._setup_error:
                raise TestExecutionError(f"Setup failed while waiting: {self._setup_error}")

        return self._setup_data

    async def reset(self) -> None:
        """Reset the setup manager state for fresh setup."""
        with self._lock:
            self._setup_data = None
            self._setup_error = None
            self._setup_in_progress.clear()
            self._setup_completed.clear()
            logger.info("Setup manager state reset")
            
    async def check_setup_status(self) -> Dict[str, Any]:
        """
        Check the current status of setup.
        
        Returns:
            Dict containing setup status information
        """
        with self._lock:
            return {
                'setup_completed': self._setup_completed.is_set(),
                'setup_in_progress': self._setup_in_progress.is_set(),
                'has_error': bool(self._setup_error),
                'error_message': self._setup_error,
                'has_data': bool(self._setup_data)
            }

    async def cleanup(self) -> None:
        """Clean up any resources used during setup."""
        try:
            if self._setup_data:
                # Add any cleanup logic here
                logger.info("Cleanup completed")
                
        except Exception as e:
            logger.error(f"Cleanup failed: {str(e)}")
        finally:
            await self.reset()

# Global setup manager instance
setup_manager = SetupManager()