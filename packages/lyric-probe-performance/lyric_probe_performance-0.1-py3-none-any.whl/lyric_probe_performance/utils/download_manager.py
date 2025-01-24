# downloadManager.py

import logging
import requests
from typing import List, Dict, Optional
from pathlib import Path

from utils.log_manager import setup_logger

logger = setup_logger(__name__)

class DownloadManager:
    """Manages file downloads."""

    def __init__(self, base_download_dir: str = './downloads'):
        """Initialize DownloadManager."""
        self.base_download_dir = Path(base_download_dir)

    def ensure_download_directory(self, subdir: Optional[str] = None) -> Path:
        """Ensure the download directory exists."""
        download_dir = self.base_download_dir
        if subdir:
            download_dir = download_dir / subdir
        download_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Download directory created: {download_dir}")
        return download_dir

    @staticmethod
    def extract_filename_from_url(url: str) -> Optional[str]:
        """Extract filename from a URL's content-disposition."""
        try:
            if 'filename%20%3D%20' in url:
                filename = url.split('filename%20%3D%20')[1].split('&')[0]
                return filename
            return None
        except Exception as e:
            logger.error(f"Error extracting filename from URL: {str(e)}")
            return None

    def _download_file(self, url: str, file_path: Path, progress_callback=None) -> bool:
        """Download a file from a URL to a specified path."""
        try:
            with requests.get(url, stream=True, verify=False) as response:
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))
                downloaded_size = 0

                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            file.write(chunk)
                            downloaded_size += len(chunk)
                            if progress_callback:
                                progress_callback(len(chunk), total_size, file_path.name)

            logger.info(f"Successfully downloaded file to {file_path}")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to download from {url}. Error: {str(e)}")
            return False

    def download_single_file(self, url: str, download_dir: Path, progress_callback=None) -> Optional[Dict[str, str]]:
        """Download a single file and return its details."""
        try:
            filename = self.extract_filename_from_url(url)
            if not filename:
                logger.error(f"Could not extract filename from URL: {url}")
                return None
                
            file_path = download_dir / filename
            
            if self._download_file(url, file_path, progress_callback):
                return {
                    'filename': filename,
                    'path': str(file_path)
                }
            return None
                
        except Exception as e:
            logger.error(f"Error in download process: {str(e)}")
            return None

    def download_files(
        self, 
        urls: List[str], 
        subdir: Optional[str] = None, 
        file_filters: Optional[List[str]] = None,
        progress_callback = None
    ) -> List[Dict[str, str]]:
        """
        Download multiple files with optional filtering.
        
        Args:
            urls: List of URLs to download from
            subdir: Optional subdirectory for downloads
            file_filters: Optional list of filenames to download
            progress_callback: Optional callback for download progress
            
        Returns:
            List[Dict[str, str]]: List of downloaded file information
        """
        if not urls:
            logger.warning("No URLs provided for download")
            return []

        download_dir = self.ensure_download_directory(subdir)
        downloaded_files = []
        
        try:
            for url in urls:
                filename = self.extract_filename_from_url(url)
                
                # Skip if filename not in filters (if filters are provided)
                if file_filters and filename not in file_filters:
                    logger.info(f"Skipping {filename} as it's not in the download filters")
                    continue
                    
                result = self.download_single_file(url, download_dir, progress_callback)
                if result is not None:
                    downloaded_files.append(result)
                        
        except Exception as e:
            logger.error(f"Error during file downloads: {str(e)}")
        
        logger.info(f"Successfully downloaded {len(downloaded_files)} files")
        return downloaded_files


def download_files_with_progress(
    urls: List[str],
    base_dir: str = './downloads',
    subdir: Optional[str] = None,
    file_filters: Optional[List[str]] = None,
    progress_callback = None
) -> List[Dict[str, str]]:
    """Download files with a download manager."""
    download_manager = DownloadManager(base_dir)
    return download_manager.download_files(
        urls=urls,
        subdir=subdir,
        file_filters=file_filters,
        progress_callback=progress_callback
    )