from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, List
from enum import Enum


class RunStatus(str, Enum):
    PENDING = "Pending"
    PROVISIONING = "Provisioning GPUs"
    LAUNCHING_SFT = "Launching SFT"
    TRAINING_SFT = "Training SFT"
    PREPARING_DPO = "Preparing for DPO"
    LAUNCHING_DPO = "Launching DPO"
    TRAINING_DPO = "Training DPO"
    SAVING_MODEL = "Saving model"
    FREEING_GPUS = "Freeing GPUs"
    COMPLETED = "Complete"
    FAILED = "Failed"


@dataclass
class FileUpload:
    file_id: str
    uploaded: bool
    line_count: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


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

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class DPOConfig:
    file_id: Optional[str] = None
    hf_sft_dataset_name: Optional[str] = None
    hf_dpo_dataset_name: Optional[str] = None
    run_config: Optional[RunConfig] = None
    beta: float = 0.1
    reference_free: bool = False
    additional_config: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        d = {}
        for k, v in asdict(self).items():
            if v is not None:
                if isinstance(v, RunConfig):
                    d[k] = v.to_dict()
                else:
                    d[k] = v
        return d 