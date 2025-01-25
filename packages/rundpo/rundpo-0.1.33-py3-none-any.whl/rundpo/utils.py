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

def download_and_extract(url: str, run_id: str, cache_dir: Optional[Path] = None) -> Path:
    """Download and extract a model synchronously."""
    if cache_dir is None:
        cache_dir = get_cache_dir()
        
    cache_dir.mkdir(parents=True, exist_ok=True)
    target_dir = cache_dir / run_id
    
    # Create a temporary directory for downloading
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / f"{run_id}.zip"
        
        # Download the file
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))
            
            with open(temp_path, 'wb') as f:
                with tqdm(total=total_size, unit='iB', unit_scale=True, desc="Downloading") as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        
        # Extract to target directory, removing any common prefix
        with zipfile.ZipFile(temp_path) as zip_ref:
            # Get the common prefix of all files in the zip
            all_paths = zip_ref.namelist()
            if not all_paths:
                return target_dir
                
            common_prefix = os.path.commonpath(all_paths)
            target_dir.mkdir(parents=True, exist_ok=True)
            
            for member in zip_ref.namelist():
                # Skip if this is just the root directory
                if member == common_prefix or member.rstrip('/') == common_prefix:
                    continue
                    
                # Remove the common prefix to extract directly to target
                relative_path = os.path.relpath(member, common_prefix)
                source = zip_ref.open(member)
                target_path = target_dir / relative_path
                
                try:
                    if member.endswith('/'):  # It's a directory
                        target_path.mkdir(parents=True, exist_ok=True)
                    else:  # It's a file
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        with open(target_path, 'wb') as target:
                            shutil.copyfileobj(source, target)
                finally:
                    source.close()

    return target_dir

async def download_and_extract_async(url: str, run_id: str, cache_dir: Optional[Path] = None) -> Path:
    """Download and extract a model asynchronously."""
    if cache_dir is None:
        cache_dir = get_cache_dir()
        
    cache_dir.mkdir(parents=True, exist_ok=True)
    target_dir = cache_dir / run_id
    
    # Create a temporary directory for downloading
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / f"{run_id}.zip"
        
        # Download the file
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))
                
                with open(temp_path, 'wb') as f:
                    with tqdm(total=total_size, unit='iB', unit_scale=True, desc="Downloading") as pbar:
                        async for chunk in response.content.iter_chunked(8192):
                            f.write(chunk)
                            pbar.update(len(chunk))
            
        # Extract to target directory, removing any common prefix
        with zipfile.ZipFile(temp_path) as zip_ref:
            # Get the common prefix of all files in the zip
            all_paths = zip_ref.namelist()
            if not all_paths:
                return target_dir
                
            common_prefix = os.path.commonpath(all_paths)
            target_dir.mkdir(parents=True, exist_ok=True)
            
            for member in zip_ref.namelist():
                # Skip if this is just the root directory
                if member == common_prefix or member.rstrip('/') == common_prefix:
                    continue
                    
                # Remove the common prefix to extract directly to target
                relative_path = os.path.relpath(member, common_prefix)
                source = zip_ref.open(member)
                target_path = target_dir / relative_path
                
                try:
                    if member.endswith('/'):  # It's a directory
                        target_path.mkdir(parents=True, exist_ok=True)
                    else:  # It's a file
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        with open(target_path, 'wb') as target:
                            shutil.copyfileobj(source, target)
                finally:
                    source.close()

    return target_dir 