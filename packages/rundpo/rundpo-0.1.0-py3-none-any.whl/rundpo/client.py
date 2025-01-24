import os
import aiohttp
import requests
from typing import Optional, Dict, Any, List, Union
from .types import RunConfig, RunStatus, FileUpload, DPOConfig


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
            headers={"Authorization": f"Bearer {self.api_key}"}
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
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
        return self._session

    async def get_credits(self) -> float:
        """Get remaining credits for the account."""
        async with self.session.get(f"{self.base_url}/get_credits.php") as response:
            response.raise_for_status()
            data = await response.json()
            return float(data["credits"])

    async def run_dpo(self, config: DPOConfig) -> str:
        """Start a DPO training run."""
        if not config.file_id and not (config.hf_sft_dataset_name and config.hf_dpo_dataset_name):
            raise ValueError("Either file_id or both HF dataset names must be provided")

        payload = config.__dict__
        async with self.session.post(f"{self.base_url}/run_dpo.php", json=payload) as response:
            response.raise_for_status()
            data = await response.json()
            return data["run_id"]

    async def get_status(self, run_id: str) -> RunStatus:
        """Get the status of a run."""
        async with self.session.get(
            f"{self.base_url}/get_status.php", params={"run_id": run_id}
        ) as response:
            response.raise_for_status()
            data = await response.json()
            return RunStatus(data["status"])

    async def cancel_run(self, run_id: str) -> bool:
        """Cancel a running job."""
        async with self.session.post(
            f"{self.base_url}/cancel_run.php", json={"run_id": run_id}
        ) as response:
            response.raise_for_status()
            data = await response.json()
            return data["success"]

    async def upload_file(self, file_path: str) -> FileUpload:
        """Upload a file for processing."""
        with open(file_path, "rb") as f:
            files = {"file": f}
            async with self.session.post(
                f"{self.base_url}/upload_file.php", data=files
            ) as response:
                response.raise_for_status()
                data = await response.json()
                return FileUpload(**data)

    async def list_files(self) -> List[FileUpload]:
        """List all uploaded files."""
        async with self.session.get(f"{self.base_url}/list_files.php") as response:
            response.raise_for_status()
            data = await response.json()
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
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def get_credits(self) -> float:
        """Get remaining credits for the account."""
        response = self.session.get(f"{self.base_url}/get_credits.php")
        response.raise_for_status()
        return float(response.json()["credits"])

    def run_dpo(self, config: DPOConfig) -> str:
        """Start a DPO training run."""
        if not config.file_id and not (config.hf_sft_dataset_name and config.hf_dpo_dataset_name):
            raise ValueError("Either file_id or both HF dataset names must be provided")

        payload = config.__dict__
        response = self.session.post(f"{self.base_url}/run_dpo.php", json=payload)
        response.raise_for_status()
        return response.json()["run_id"]

    def get_status(self, run_id: str) -> RunStatus:
        """Get the status of a run."""
        response = self.session.get(
            f"{self.base_url}/get_status.php", params={"run_id": run_id}
        )
        response.raise_for_status()
        return RunStatus(response.json()["status"])

    def cancel_run(self, run_id: str) -> bool:
        """Cancel a running job."""
        response = self.session.post(
            f"{self.base_url}/cancel_run.php", json={"run_id": run_id}
        )
        response.raise_for_status()
        return response.json()["success"]

    def upload_file(self, file_path: str) -> FileUpload:
        """Upload a file for processing."""
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = self.session.post(f"{self.base_url}/upload_file.php", files=files)
            response.raise_for_status()
            return FileUpload(**response.json())

    def list_files(self) -> List[FileUpload]:
        """List all uploaded files."""
        response = self.session.get(f"{self.base_url}/list_files.php")
        response.raise_for_status()
        return [FileUpload(**file) for file in response.json()["files"]] 