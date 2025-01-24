"""Utility for generating and managing performance test reports."""

import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, NamedTuple, Optional
from dataclasses import dataclass
from utils.log_manager import setup_logger

# Initialize logger using our custom setup
logger = setup_logger(__name__)

@dataclass
class ReportConfig:
    """Configuration for report generation."""
    base_dir: str = 'reports'
    html_dir: str = 'html'
    csv_dir: str = 'csv'
    max_reports: int = 10

class ReportPaths(NamedTuple):
    """Container for report file paths."""
    html: Path
    stats_csv: Path
    history_csv: Path

class ReportManager:
    """Manager for generating and handling performance test reports."""
    
    def __init__(self, config: Optional[ReportConfig] = None):
        """
        Initialize the report manager.
        
        Args:
            config: Optional configuration for report generation
        """
        self.config = config or ReportConfig()
        self.setup_directories()
        
    def setup_directories(self) -> None:
        """Create necessary directory structure for reports."""
        try:
            # Create main reports directory
            reports_dir = Path(self.config.base_dir)
            reports_dir.mkdir(exist_ok=True)
            
            # Create subdirectories
            (reports_dir / self.config.html_dir).mkdir(exist_ok=True)
            (reports_dir / self.config.csv_dir).mkdir(exist_ok=True)
            
            logger.info(f"Report directories created in {reports_dir}")
            
        except Exception as e:
            logger.error(f"Failed to create report directories: {str(e)}")
            raise Exception(f"Failed to create report directories: {str(e)}")
            
    def generate_report_paths(self, test_name: Optional[str] = None) -> ReportPaths:
        """
        Generate paths for report files with timestamps.
        
        Args:
            test_name: Optional name to include in report files
            
        Returns:
            ReportPaths: Named tuple containing paths for different report files
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        base_name = f"{test_name}_{timestamp}" if test_name else timestamp
        
        reports_dir = Path(self.config.base_dir)
        
        return ReportPaths(
            html=reports_dir / self.config.html_dir / f"report_{base_name}.html",
            stats_csv=reports_dir / self.config.csv_dir / f"stats_{base_name}",  # Base name for CSV files
            history_csv=reports_dir / self.config.csv_dir / f"history_{base_name}"
        )
        
    def clean_old_reports(self) -> None:
        """Remove old reports keeping only the most recent ones based on config."""
        try:
            reports_dir = Path(self.config.base_dir)
            
            # Clean HTML reports
            self._clean_directory(reports_dir / self.config.html_dir, "*.html")
            
            # Clean CSV reports
            self._clean_directory(reports_dir / self.config.csv_dir, "*.csv")
            
            logger.info(f"Cleaned old reports, keeping {self.config.max_reports} most recent reports")
            
        except Exception as e:
            logger.error(f"Failed to clean old reports: {str(e)}")
            
    def _clean_directory(self, directory: Path, pattern: str) -> None:
        """
        Clean old files in a directory keeping only the most recent ones.
        
        Args:
            directory: Directory to clean
            pattern: File pattern to match
        """
        if not directory.exists():
            return
            
        files = list(directory.glob(pattern))
        if len(files) <= self.config.max_reports:
            return
            
        # Sort files by creation time (oldest first)
        files.sort(key=lambda x: x.stat().st_ctime)
        
        # Remove oldest files
        for file in files[:-self.config.max_reports]:
            file.unlink()
            logger.debug(f"Removed old report: {file}")
            
    def get_locust_command_args(self, report_paths: ReportPaths) -> Dict[str, str]:
        """Get Locust command line arguments for report generation."""
        return {
            "--html": str(report_paths.html),
            "--csv": str(report_paths.stats_csv.parent / report_paths.stats_csv.stem)
        }
        
    def get_latest_report(self, report_type: str = 'html') -> Optional[Path]:
        """
        Get the path to the most recent report of specified type.
        
        Args:
            report_type: Type of report ('html' or 'csv')
            
        Returns:
            Optional[Path]: Path to the most recent report or None if not found
        """
        reports_dir = Path(self.config.base_dir)
        
        if report_type == 'html':
            pattern = f"{self.config.html_dir}/*.html"
        elif report_type == 'csv':
            pattern = f"{self.config.csv_dir}/*.csv"
        else:
            raise Exception(f"Invalid report type: {report_type}")
            
        files = list(reports_dir.glob(pattern))
        return max(files, key=lambda x: x.stat().st_ctime) if files else None