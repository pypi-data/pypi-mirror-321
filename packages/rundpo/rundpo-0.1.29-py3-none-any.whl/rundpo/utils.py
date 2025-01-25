import os
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import Optional
import aiohttp
import requests
from tqdm import tqdm

def get_cache_dir() -> Path:
    """Get the cache directory for storing downloaded models.
    
    Uses RD_HOME environment variable if set, otherwise defaults to ~/.cache/rundpo/adapters
    """
    cache_dir = os.environ.get("RD_HOME")
    if cache_dir:
        return Path(cache_dir)
    return Path.home() / ".cache" / "rundpo" / "adapters"

async def download_and_extract_async(url: str, run_id: str, cache_dir: Optional[Path] = None) -> Path:
    """Download and extract a model asynchronously.
    
    Args:
        url: The download URL for the model
        run_id: The run ID to use for the directory name
        cache_dir: Optional override for the cache directory
        
    Returns:
        Path to the extracted model directory
    """
    if cache_dir is None:
        cache_dir = get_cache_dir()
        
    # Create cache directory if it doesn't exist
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a temporary directory for downloading
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / f"{run_id}.zip"
        
        # Download the file with progress bar
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))
                
                with open(temp_path, 'wb') as f:
                    with tqdm(total=total_size, unit='iB', unit_scale=True, desc="Downloading") as pbar:
                        async for chunk in response.content.iter_chunked(8192):
                            f.write(chunk)
                            pbar.update(len(chunk))
        
        # Extract to cache directory
        target_dir = cache_dir / run_id
        if target_dir.exists():
            shutil.rmtree(target_dir)
            
        target_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(temp_path) as zip_ref:
            # Get the common prefix of all files in the zip (if any)
            all_paths = zip_ref.namelist()
            if all_paths:
                common_prefix = os.path.commonpath(all_paths)
                for member in zip_ref.namelist():
                    # Remove the common prefix when extracting
                    if common_prefix:
                        relative_path = os.path.relpath(member, common_prefix)
                    else:
                        relative_path = member
                    # Skip if this is the root directory
                    if relative_path == '.' or relative_path == '':
                        continue
                    source = zip_ref.open(member)
                    target_path = target_dir / relative_path
                    # Create parent directories if they don't exist
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    # Extract the file
                    with open(target_path, 'wb') as target:
                        shutil.copyfileobj(source, target)
            
    return target_dir

def download_and_extract(url: str, run_id: str, cache_dir: Optional[Path] = None) -> Path:
    """Download and extract a model synchronously.
    
    Args:
        url: The download URL for the model
        run_id: The run ID to use for the directory name
        cache_dir: Optional override for the cache directory
        
    Returns:
        Path to the extracted model directory
    """
    if cache_dir is None:
        cache_dir = get_cache_dir()
        
    # Create cache directory if it doesn't exist
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a temporary directory for downloading
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / f"{run_id}.zip"
        
        # Download the file with progress bar
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))
            
            with open(temp_path, 'wb') as f:
                with tqdm(total=total_size, unit='iB', unit_scale=True, desc="Downloading") as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        
        # Extract to cache directory
        target_dir = cache_dir / run_id
        if target_dir.exists():
            shutil.rmtree(target_dir)
            
        target_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(temp_path) as zip_ref:
            # Get the common prefix of all files in the zip (if any)
            all_paths = zip_ref.namelist()
            if all_paths:
                common_prefix = os.path.commonpath(all_paths)
                for member in zip_ref.namelist():
                    # Remove the common prefix when extracting
                    if common_prefix:
                        relative_path = os.path.relpath(member, common_prefix)
                    else:
                        relative_path = member
                    # Skip if this is the root directory
                    if relative_path == '.' or relative_path == '':
                        continue
                    source = zip_ref.open(member)
                    target_path = target_dir / relative_path
                    # Create parent directories if they don't exist
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    # Extract the file
                    with open(target_path, 'wb') as target:
                        shutil.copyfileobj(source, target)
            
    return target_dir 