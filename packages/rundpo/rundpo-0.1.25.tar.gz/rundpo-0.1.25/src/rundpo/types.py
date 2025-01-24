from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class RunConfig:
    """Configuration for a training run.
    
    All parameters match exactly what the API supports:
    - base_model: Base model to use (default: "Qwen/Qwen2-0.5B")
    - sft_learning_rate: Learning rate for SFT training (default: 0.0002)
    - sft_ratio: Ratio of data to use for SFT (default: 0.05)
    - sft_packing: Whether to use packing for SFT (default: True)
    - sft_per_device_train_batch_size: Batch size per device for SFT (default: 2)
    - sft_gradient_accumulation_steps: Gradient accumulation steps for SFT (default: 8)
    - sft_gradient_checkpointing: Whether to use gradient checkpointing for SFT (default: True)
    - sft_lora_r: LoRA r parameter for SFT (default: 32)
    - sft_lora_alpha: LoRA alpha parameter for SFT (default: 16)
    - dpo_learning_rate: Learning rate for DPO training (default: 0.000005)
    - dpo_num_train_epochs: Number of epochs for DPO training (default: 1)
    - dpo_per_device_train_batch_size: Batch size per device for DPO (default: 8)
    - dpo_gradient_accumulation_steps: Gradient accumulation steps for DPO (default: 2)
    - dpo_gradient_checkpointing: Whether to use gradient checkpointing for DPO (default: True)
    - dpo_lora_r: LoRA r parameter for DPO (default: 16)
    - dpo_lora_alpha: LoRA alpha parameter for DPO (default: 8)
    - dpo_bf16: Whether to use bfloat16 for DPO (default: True)
    - dpo_max_length: Maximum sequence length for DPO (default: None)
    - gpus: Number of GPUs to use (default: 2)
    """
    base_model: str = "Qwen/Qwen2-0.5B"
    sft_learning_rate: float = 0.0002
    sft_ratio: float = 0.05
    sft_packing: bool = True
    sft_per_device_train_batch_size: int = 2
    sft_gradient_accumulation_steps: int = 8
    sft_gradient_checkpointing: bool = True
    sft_lora_r: int = 32
    sft_lora_alpha: int = 16
    dpo_learning_rate: float = 0.000005
    dpo_num_train_epochs: int = 1
    dpo_per_device_train_batch_size: int = 8
    dpo_gradient_accumulation_steps: int = 2
    dpo_gradient_checkpointing: bool = True
    dpo_lora_r: int = 16
    dpo_lora_alpha: int = 8
    dpo_bf16: bool = True
    dpo_max_length: Optional[int] = None
    gpus: int = 2

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        data = {
            "base_model": self.base_model,
            "sft_learning_rate": self.sft_learning_rate,
            "sft_ratio": self.sft_ratio,
            "sft_packing": self.sft_packing,
            "sft_per_device_train_batch_size": self.sft_per_device_train_batch_size,
            "sft_gradient_accumulation_steps": self.sft_gradient_accumulation_steps,
            "sft_gradient_checkpointing": self.sft_gradient_checkpointing,
            "sft_lora_r": self.sft_lora_r,
            "sft_lora_alpha": self.sft_lora_alpha,
            "dpo_learning_rate": self.dpo_learning_rate,
            "dpo_num_train_epochs": self.dpo_num_train_epochs,
            "dpo_per_device_train_batch_size": self.dpo_per_device_train_batch_size,
            "dpo_gradient_accumulation_steps": self.dpo_gradient_accumulation_steps,
            "dpo_gradient_checkpointing": self.dpo_gradient_checkpointing,
            "dpo_lora_r": self.dpo_lora_r,
            "dpo_lora_alpha": self.dpo_lora_alpha,
            "dpo_bf16": self.dpo_bf16,
            "gpus": self.gpus
        }
        if self.dpo_max_length is not None:
            data["dpo_max_length"] = self.dpo_max_length
        return data

@dataclass
class FileUpload:
    """Represents an uploaded file."""
    file_id: str
    uploaded: bool
    line_count: Optional[int] = None

@dataclass
class DPOConfig:
    """Configuration for a DPO training run.
    
    Args:
        run_config: The training configuration
        file_id: ID of the uploaded file to use (mutually exclusive with HF datasets)
        hf_sft_dataset_name: HuggingFace dataset name for SFT (mutually exclusive with file_id)
        hf_dpo_dataset_name: HuggingFace dataset name for DPO (mutually exclusive with file_id)
    """
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
    PREPARING_DPO = "Preparing for DPO"
    LAUNCHING_DPO = "Launching DPO"
    TRAINING_DPO = "Training DPO"
    SAVING_MODEL = "Saving Model"
    FREEING_GPUS = "Freeing GPUs"
    COMPLETED = "Complete"
    FAILED = "Failed" 