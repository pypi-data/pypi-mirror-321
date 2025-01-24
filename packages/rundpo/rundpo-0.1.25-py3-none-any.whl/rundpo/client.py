import os
import json
import aiohttp
import requests
from typing import Optional, Dict, Any, List, Union
from .types import RunConfig, RunStatus, FileUpload, DPOConfig


class RundpoError(Exception):
    """Base exception for Rundpo API errors."""
    pass


class AsyncRundpoClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://rundpo.com/api/v2",
    ):
        self.api_key = api_key or os.environ.get("RUNDPO_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set in RUNDPO_API_KEY environment variable")
        self.base_url = base_url.rstrip("/")
        self._session = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession(
            headers={"X-API-Key": self.api_key}
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            await self._session.close()
            self._session = None

    @property
    def session(self) -> aiohttp.ClientSession:
        if not self._session:
            self._session = aiohttp.ClientSession(
                headers={"X-API-Key": self.api_key}
            )
        return self._session

    async def _get_json(self, response: aiohttp.ClientResponse) -> Any:
        """Helper method to handle JSON responses that might be sent as text/html."""
        try:
            return await response.json()
        except aiohttp.ContentTypeError:
            # If server sends JSON with wrong content-type, try parsing the text
            text = await response.text()
            try:
                return json.loads(text)
            except json.JSONDecodeError as e:
                raise ValueError(f"Failed to parse response as JSON: {text}") from e

    async def get_credits(self) -> float:
        """Get remaining credits for the account."""
        async with self.session.get(f"{self.base_url}/get_credits.php") as response:
            response.raise_for_status()
            data = await self._get_json(response)
            return float(data["credits"])

    async def run_dpo(self, config: DPOConfig) -> str:
        """Start a DPO training run."""
        if not config.file_id and not (config.hf_sft_dataset_name and config.hf_dpo_dataset_name):
            raise ValueError("Either file_id or both HF dataset names must be provided")

        payload = config.to_dict()
        async with self.session.post(f"{self.base_url}/run_dpo.php", json=payload) as response:
            response.raise_for_status()
            data = await self._get_json(response)
            if "error" in data:
                raise RundpoError(data["error"])
            return data["run_name"]

    async def get_status(self, run_id: str) -> Dict[str, Any]:
        """Get the status of a run.
        
        Returns:
            Dict containing:
            - status: RunStatus - Current status of the run
            - download_url: Optional[str] - URL to download the model (only present when status is COMPLETED)
        """
        async with self.session.get(
            f"{self.base_url}/get_status.php", params={"run_name": run_id}
        ) as response:
            response.raise_for_status()
            data = await self._get_json(response)
            if "error" in data:
                raise RundpoError(data["error"])
            return {
                "status": RunStatus(data["status"]),
                "download_url": data.get("download_url")
            }

    async def cancel_run(self, run_id: str) -> bool:
        """Cancel a running job."""
        async with self.session.post(
            f"{self.base_url}/cancel_run.php", json={"run_id": run_id}
        ) as response:
            response.raise_for_status()
            data = await self._get_json(response)
            if "error" in data:
                raise RundpoError(data["error"])
            return data["success"]

    async def upload_file(self, file_path: str) -> FileUpload:
        """Upload a file for processing."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        with open(file_path, 'rb') as f:
            data = aiohttp.FormData()
            data.add_field('jsonl_file',
                          f,
                          filename=os.path.basename(file_path),
                          content_type='application/octet-stream')
            
            async with self.session.post(
                f"{self.base_url}/upload_file.php",
                data=data
            ) as response:
                response.raise_for_status()
                data = await self._get_json(response)
                if "error" in data:
                    raise RundpoError(data["error"])
                return FileUpload(
                    file_id=data["file_id"],
                    uploaded=data["uploaded"],
                    line_count=data.get("lineCount")
                )

    async def list_files(self) -> List[FileUpload]:
        """List all uploaded files."""
        async with self.session.get(f"{self.base_url}/list_files.php") as response:
            response.raise_for_status()
            data = await self._get_json(response)
            if "error" in data:
                raise RundpoError(data["error"])
            return [FileUpload(**file) for file in data["files"]]


class RundpoClient:
    """Synchronous client for those who prefer not to use async/await."""
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://rundpo.com/api/v2",
    ):
        self.api_key = api_key or os.environ.get("RUNDPO_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set in RUNDPO_API_KEY environment variable")
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"X-API-Key": self.api_key})

    def _get_json(self, response: requests.Response) -> Any:
        """Helper method to handle JSON responses that might be sent as text/html."""
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            # If server sends invalid JSON, try parsing the text
            try:
                return json.loads(response.text)
            except json.JSONDecodeError as e:
                raise ValueError(f"Failed to parse response as JSON: {response.text}") from e

    def get_credits(self) -> float:
        """Get remaining credits for the account."""
        response = self.session.get(f"{self.base_url}/get_credits.php")
        response.raise_for_status()
        data = self._get_json(response)
        return float(data["credits"])

    def run_dpo(self, config: DPOConfig) -> str:
        """Start a DPO training run."""
        if not config.file_id and not (config.hf_sft_dataset_name and config.hf_dpo_dataset_name):
            raise ValueError("Either file_id or both HF dataset names must be provided")

        payload = config.to_dict()
        response = self.session.post(f"{self.base_url}/run_dpo.php", json=payload)
        response.raise_for_status()
        data = self._get_json(response)
        if "error" in data:
            raise RundpoError(data["error"])
        return data["run_name"]

    def get_status(self, run_id: str) -> Dict[str, Any]:
        """Get the status of a run.
        
        Returns:
            Dict containing:
            - status: RunStatus - Current status of the run
            - download_url: Optional[str] - URL to download the model (only present when status is COMPLETED)
        """
        response = self.session.get(
            f"{self.base_url}/get_status.php", params={"run_name": run_id}
        )
        response.raise_for_status()
        data = self._get_json(response)
        if "error" in data:
            raise RundpoError(data["error"])
        return {
            "status": RunStatus(data["status"]),
            "download_url": data.get("download_url")
        }

    def cancel_run(self, run_id: str) -> bool:
        """Cancel a running job."""
        response = self.session.post(
            f"{self.base_url}/cancel_run.php", json={"run_id": run_id}
        )
        response.raise_for_status()
        data = self._get_json(response)
        if "error" in data:
            raise RundpoError(data["error"])
        return data["success"]

    def upload_file(self, file_path: str) -> FileUpload:
        """Upload a file for processing."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        with open(file_path, 'rb') as f:
            files = {'jsonl_file': (os.path.basename(file_path), f, 'application/octet-stream')}
            response = self.session.post(f"{self.base_url}/upload_file.php", files=files)
            response.raise_for_status()
            data = self._get_json(response)
            if "error" in data:
                raise RundpoError(data["error"])
            return FileUpload(
                file_id=data["file_id"],
                uploaded=data["uploaded"],
                line_count=data.get("lineCount")
            )

    def list_files(self) -> List[FileUpload]:
        """List all uploaded files."""
        response = self.session.get(f"{self.base_url}/list_files.php")
        response.raise_for_status()
        data = self._get_json(response)
        if "error" in data:
            raise RundpoError(data["error"])
        return [FileUpload(**file) for file in data["files"]]