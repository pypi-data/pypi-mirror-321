from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from enum import Enum


class RunStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class FileUpload:
    file_id: str
    name: str
    size: int
    upload_date: str


@dataclass
class RunConfig:
    model_name: str
    learning_rate: float
    num_epochs: int
    batch_size: int
    gradient_accumulation_steps: int
    warmup_steps: int
    max_steps: Optional[int] = None
    fp16: bool = True
    bf16: bool = False
    additional_config: Optional[Dict[str, Any]] = None


@dataclass
class DPOConfig:
    file_id: Optional[str] = None
    hf_sft_dataset_name: Optional[str] = None
    hf_dpo_dataset_name: Optional[str] = None
    run_config: Optional[RunConfig] = None
    beta: float = 0.1
    reference_free: bool = False
    additional_config: Optional[Dict[str, Any]] = None 