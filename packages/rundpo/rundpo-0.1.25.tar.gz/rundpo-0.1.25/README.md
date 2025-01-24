# Rundpo Python Client

A modern, async-first Python client for the Rundpo API. This client provides a convenient way to interact with the Rundpo API for running DPO (Direct Preference Optimization) training.

## Installation

```bash
pip install rundpo
```

## Usage

The client provides both async and sync interfaces. Here's how to use them:

### Async Usage

```python
import os
import asyncio
from rundpo import AsyncRundpoClient, DPOConfig, RunConfig, RunStatus, download_and_extract_async

async def main():
    # Initialize the client
    async with AsyncRundpoClient() as client:
        # Check credits
        credits = await client.get_credits()
        print(f"Remaining credits: {credits}")

        # Upload your data file
        file_upload = await client.upload_file("t.jsonl")
        print(f"File uploaded successfully! ID: {file_upload.file_id}")

        # Configure DPO run
        config = DPOConfig(
            file_id=file_upload.file_id,
            run_config=RunConfig(
                base_model="meta-llama/Llama-3.1-8B-Instruct",
                gpus=2,
                dpo_num_train_epochs=5
            )
        )
        
        # Start DPO training
        run_id = await client.run_dpo(config)
        print(f"Started DPO run with ID: {run_id}")
        
        # Poll for completion
        while True:
            result = await client.get_status(run_id)
            status = result["status"]
            print(f"Run status: {status}")
            
            if status == RunStatus.COMPLETED:
                print("✓ Run completed successfully!")
                # Download and extract the model
                if result.get("download_url"):
                    print("Downloading and extracting model...")
                    model_path = await download_and_extract_async(result["download_url"], run_id)
                    print(f"Model downloaded and extracted to: {model_path}")
                break
            elif status == RunStatus.FAILED:
                print("✗ Run failed!")
                break
                
            # Wait 30 seconds before checking again
            await asyncio.sleep(30)

asyncio.run(main())
```

### Sync Usage

```python
from rundpo import RundpoClient, DPOConfig, RunConfig, RunStatus, download_and_extract
import time

# Initialize the client
client = RundpoClient()

# Check credits
credits = client.get_credits()
print(f"Remaining credits: {credits}")

# Upload your data file
file_upload = client.upload_file("t.jsonl")
print(f"File uploaded successfully! ID: {file_upload.file_id}")

# Configure DPO run
config = DPOConfig(
    file_id=file_upload.file_id,
    run_config=RunConfig(
        base_model="meta-llama/Llama-3.1-8B-Instruct",
        gpus=2,
        dpo_num_train_epochs=5
    )
)

# Start DPO training
run_id = client.run_dpo(config)
print(f"Started DPO run with ID: {run_id}")

# Poll for completion
while True:
    result = client.get_status(run_id)
    status = result["status"]
    print(f"Run status: {status}")
    
    if status == RunStatus.COMPLETED:
        print("✓ Run completed successfully!")
        # Download and extract the model
        if result.get("download_url"):
            print("Downloading and extracting model...")
            model_path = download_and_extract(result["download_url"], run_id)
            print(f"Model downloaded and extracted to: {model_path}")
        break
    elif status == RunStatus.FAILED:
        print("✗ Run failed!")
        break
        
    # Wait 30 seconds before checking again
    time.sleep(30)
```

### Using HuggingFace Datasets

Instead of uploading a file, you can use HuggingFace datasets directly:

```python
config = DPOConfig(
    hf_sft_dataset_name="your-sft-dataset",
    hf_dpo_dataset_name="your-dpo-dataset",
    run_config=RunConfig(
        base_model="meta-llama/Llama-3.1-8B-Instruct",
        gpus=2,
        dpo_num_train_epochs=5
    )
)
```

### Available Configuration Options

The `RunConfig` class supports all parameters from the API:

```python
config = RunConfig(
    # Required
    base_model="meta-llama/Llama-3.1-8B-Instruct",  # Base model to use
    
    # SFT (Supervised Fine-Tuning) parameters
    sft_learning_rate=0.0002,                    # Learning rate for SFT (default: 0.0002)
    sft_ratio=0.05,                             # Ratio of data to use for SFT (default: 0.05)
    sft_packing=True,                           # Whether to use packing for SFT (default: True)
    sft_per_device_train_batch_size=2,          # Batch size per device for SFT (default: 2)
    sft_gradient_accumulation_steps=8,          # Gradient accumulation steps for SFT (default: 8)
    sft_gradient_checkpointing=True,            # Whether to use gradient checkpointing (default: True)
    sft_lora_r=32,                             # LoRA r parameter for SFT (default: 32)
    sft_lora_alpha=16,                         # LoRA alpha parameter for SFT (default: 16)
    
    # DPO (Direct Preference Optimization) parameters
    dpo_learning_rate=0.000005,                # Learning rate for DPO (default: 0.000005)
    dpo_num_train_epochs=1,                    # Number of epochs for DPO (default: 1)
    dpo_per_device_train_batch_size=8,         # Batch size per device for DPO (default: 8)
    dpo_gradient_accumulation_steps=2,         # Gradient accumulation steps for DPO (default: 2)
    dpo_gradient_checkpointing=True,           # Whether to use gradient checkpointing (default: True)
    dpo_lora_r=16,                            # LoRA r parameter for DPO (default: 16)
    dpo_lora_alpha=8,                         # LoRA alpha parameter for DPO (default: 8)
    dpo_bf16=True,                            # Whether to use bfloat16 for DPO (default: True)
    dpo_max_length=None,                      # Maximum sequence length for DPO (default: None)
    
    # Infrastructure
    gpus=2                                    # Number of GPUs to use (default: 2)
)
```

## Model Downloads

By default, downloaded models are stored in `~/.cache/rundpo/adapters`. You can customize this location by setting the `RD_HOME` environment variable:

```bash
export RD_HOME="/path/to/your/preferred/cache"
```

## API Reference

### Clients

- `AsyncRundpoClient`: Async-first client for modern Python applications
- `RundpoClient`: Synchronous client for simpler use cases

### Data Classes

- `RunConfig`: Configuration for training runs (see Available Configuration Options above)
- `DPOConfig`: Configuration specific to DPO training
- `FileUpload`: Represents an uploaded file
- `RunStatus`: Enum of possible run statuses:
  - `PENDING`: Initial state
  - `PROVISIONING`: Setting up GPUs
  - `LAUNCHING_SFT`: Starting SFT training
  - `TRAINING_SFT`: Running SFT training
  - `PREPARING_DPO`: Preparing for DPO training
  - `LAUNCHING_DPO`: Starting DPO training
  - `TRAINING_DPO`: Running DPO training
  - `SAVING_MODEL`: Saving the trained model
  - `FREEING_GPUS`: Cleaning up resources
  - `COMPLETED`: Run completed successfully
  - `FAILED`: Run failed

### Utility Functions

- `download_and_extract_async`: Download and extract a model asynchronously
- `download_and_extract`: Download and extract a model synchronously
- `get_cache_dir`: Get the current cache directory path

## License

MIT
