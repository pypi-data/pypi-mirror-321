from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class RunConfig:
    """Configuration for a training run."""
    model_name: str
    num_gpus: Optional[int] = None
    num_epochs: Optional[int] = None
    learning_rate: Optional[float] = None
    batch_size: Optional[int] = None
    gradient_accumulation_steps: Optional[int] = None
    warmup_steps: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        return {
            "model_name": self.model_name,
            "num_gpus": self.num_gpus,
            "num_epochs": self.num_epochs,
            "learning_rate": self.learning_rate,
            "batch_size": self.batch_size,
            "gradient_accumulation_steps": self.gradient_accumulation_steps,
            "warmup_steps": self.warmup_steps
        }

@dataclass
class FileUpload:
    """Represents an uploaded file."""
    file_id: str
    uploaded: bool
    line_count: Optional[int] = None

@dataclass
class DPOConfig:
    """Configuration for a DPO training run."""
    run_config: RunConfig
    file_id: Optional[str] = None
    hf_sft_dataset_name: Optional[str] = None
    hf_dpo_dataset_name: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        data = {
            **self.run_config.to_dict(),
            "file_id": self.file_id,
            "hf_sft_dataset_name": self.hf_sft_dataset_name,
            "hf_dpo_dataset_name": self.hf_dpo_dataset_name
        }
        return {k: v for k, v in data.items() if v is not None}

from enum import Enum

class RunStatus(str, Enum):
    """Status of a training run."""
    PENDING = "Pending"
    PROVISIONING = "Provisioning GPUs"
    LAUNCHING_SFT = "Launching SFT"
    TRAINING_SFT = "Training SFT"
    PREPARING_DPO = "Preparing DPO"
    LAUNCHING_DPO = "Launching DPO"
    TRAINING_DPO = "Training DPO"
    SAVING_MODEL = "Saving Model"
    FREEING_GPUS = "Freeing GPUs"
    COMPLETED = "Complete"
    FAILED = "Failed" 