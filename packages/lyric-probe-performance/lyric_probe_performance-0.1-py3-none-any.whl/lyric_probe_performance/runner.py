"""Runner script for executing Locust performance tests."""

import logging
import yaml
import subprocess
from pathlib import Path
from typing import Dict, Any
from utils.log_manager import setup_logger
from utils.report_manager import ReportManager, ReportConfig

class TestExecutionError(Exception):
    """Custom exception for test execution errors"""
    pass

# Initialize logger
logger = setup_logger(__name__)

def load_config(config_path: str = "config.yaml") -> Dict[str, Any]:
    """
    Load test configuration from YAML file.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Dict[str, Any]: Configuration dictionary
    """
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def build_locust_command(
    config: Dict[str, Any],
    report_args: Dict[str, str]
) -> list[str]:
    """
    Build the Locust command with all necessary arguments.
    """
    command = [
        "locust",
        "-f", "lyric_probe_performance/main.py",
        "--headless",
        "--users", str(config['test_config']['users']),
        "--spawn-rate", str(config['test_config']['spawn_rate']),
        "--host", config['base_url']
    ]
    
    # Add only the report args from report_manager, don't duplicate
    for arg, value in report_args.items():
        command.append(arg)
        if value is not None:
            command.append(value)
            
    return command

def main() -> None:
    """Main function to run Locust tests and generate reports."""
    try:
        # Initialize report manager
        report_manager = ReportManager(ReportConfig(max_reports=10))
        
        # Clean old reports before starting new test
        report_manager.clean_old_reports()
        
        # Load configuration
        config = load_config()
        
        # Generate report paths
        report_paths = report_manager.generate_report_paths(
            test_name=config.get('test_name', 'performance_test')
        )
        
        # Get report-related command arguments
        report_args = report_manager.get_locust_command_args(report_paths)
        
        # Build full command
        locust_command = build_locust_command(config, report_args)
        
        # Log the command for debugging
        logger.info(f"Running Locust command: {' '.join(locust_command)}")
        
        # Run the locust command
        result = subprocess.run(
            locust_command,
            check=True,
            capture_output=True,
            text=True,
            timeout=1800  # 30 minutes in seconds
        )
        
        # Log the completion and report locations
        logger.info("Locust test completed successfully")
        logger.info(f"Reports generated:")
        logger.info(f"- HTML Report: {report_paths.html}")
        logger.info(f"- Stats CSV: {report_paths.stats_csv}")
        logger.info(f"- History CSV: {report_paths.history_csv}")
        
        # Log any output from Locust
        if result.stdout:
            logger.debug(f"Locust stdout:\n{result.stdout}")
        if result.stderr:
            logging.warning(f"Locust stderr:\n{result.stderr}")
            
    except subprocess.CalledProcessError as e:
        logger.error(f"Locust command failed with exit code {e.returncode}")
        if e.stdout:
            logger.error(f"stdout:\n{e.stdout}")
        if e.stderr:
            logger.error(f"stderr:\n{e.stderr}")
        raise
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()