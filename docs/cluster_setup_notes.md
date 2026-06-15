# ADL SAE Cluster Setup Notes

Start GPU job:
srun --partition=lrz-hgx-h100-94x4,lrz-hgx-a100-80x4,lrz-dgx-a100-80x8,lrz-v100x2 --gres=gpu:1 --time=02:00:00 --pty bash

Activate environment:
source ~/venvs/adl-sae/bin/activate

Set Hugging Face cache:
export HF_HOME=~/hf_cache
export TRANSFORMERS_CACHE=~/hf_cache

Check GPU:
nvidia-smi

Check PyTorch:
python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"

Check current jobs:
squeue -u $USER
