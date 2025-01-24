import asyncio
from locust import HttpUser, between, task, events
from lyric_probe_performance.tasks.action_task import ActionExecutionTask
from lyric_probe_performance.tasks.scenario_task import ScenarioCreationTask
from lyric_probe_performance.tasks.upload_task import FileUploadTask
from utils.log_manager import setup_logger
from utils.config_loader import ConfigLoader
from utils.setup_manager import setup_manager
from utils.token_manager import token_manager
from locust.exception import StopUser

logger = setup_logger(__name__)

class UserFlow(HttpUser):
    """Main user class that orchestrates tasks."""
    
    wait_time = between(1, 2)
    tasks = []  # Disable automatic task selection

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scenario_id = None
        self.setup_data = None
        self.config = None
        self.task_completed = False
        self.current_task = None
        self.scenario_task_completed = False
        self.upload_task_completed = False
        self.action_task_completed = False
        self.loop = asyncio.new_event_loop()  # Initialize a new event loop
        asyncio.set_event_loop(self.loop)

    def on_start(self):
        """Initialize the user session."""
        try:
            # Load config
            config_loader = ConfigLoader()
            self.config = config_loader.get_config()
            
            # Set base URL
            self.host = self.config.get('base_url', '').rstrip('/')
            
            # Get token
            token = token_manager.create_token(
                self.config['client_id'],
                self.config['client_secret'],
                self.host
            )
            if token:
                self.client.headers.update({
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                })

            # Perform initial setup
            self.setup_data = self.perform_setup()
            logger.info("User session initialized successfully")
            
        except Exception as e:
            logger.error(f"User initialization failed: {str(e)}")
            self.environment.runner.quit()

    def perform_setup(self):
        """Setup method."""
        return setup_manager.perform_setup(
            self.client,
            self.config['client_id'],
            self.config['client_secret'],
            self.config['sequence_id']
        )

    @task
    def execute_user_task(self):
        """Main task that orchestrates the workflow."""
        logger.info(f"User {id(self)} starting task")
        try:
            # Run tasks in the user's event loop
            self.loop.run_until_complete(self._execute_tasks())
        except Exception as e:
            logger.error(f"Error during task execution: {e}")
            raise StopUser(f"Stopping user due to error: {e}")

    async def _execute_tasks(self):
        """Async implementation of task execution."""
        if not self.scenario_task_completed:
            logger.info(f"User {id(self)} starting scenario creation")
            self.current_task = ScenarioCreationTask(self)
            await self.current_task.execute_scenario()
            self.scenario_task_completed = True
            logger.info(f"User {id(self)} scenario creation completed successfully.")

        if self.scenario_task_completed and not self.upload_task_completed:
            logger.info(f"User {id(self)} starting file upload")
            self.current_task = FileUploadTask(self)
            await self.current_task.run_upload_files()
            self.upload_task_completed = True
            logger.info(f"User {id(self)} upload completed successfully.")

        if self.upload_task_completed and not self.action_task_completed:
            logger.info(f"User {id(self)} starting action execution")
            self.current_task = ActionExecutionTask(self)
            await self.current_task.execute_actions()
            self.action_task_completed = True
            logger.info(f"User {id(self)} action execution completed successfully.")

    def on_stop(self):
        """Clean up after the user session ends."""
        try:
            if self.current_task:
                logger.info(f"Attempting to interrupt task: {type(self.current_task).__name__}")
                self.current_task.interrupt()
                logger.info(f"Task {type(self.current_task).__name__} interrupted successfully.")
            else:
                logger.info("No current task to interrupt.")
            
            # Clean up the event loop
            if self.loop and not self.loop.is_closed():
                self.loop.close()
                
        except Exception as e:
            logger.error(f"Error during user cleanup: {str(e)}")