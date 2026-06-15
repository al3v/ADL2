# ADL2

Applied Deep Learning project on LLM factual failures and tokenization effects using pretrained Sparse Autoencoders.

## Current goal

The main goal is to investigate whether factual mistakes made by a language model are mostly caused by tokenization artifacts, rather than true retrieval or knowledge failures.

We focus on factual QA prompts where the same fact is asked in different ways. If one prompt variant gives the correct answer and another gives a wrong answer, this may indicate prompt or tokenization sensitivity rather than missing knowledge.

## Current project direction

The project focuses on:

- factual QA prompts
- same fact asked with different phrasings
- Gemma model outputs
- correctness checking
- activation extraction from early/mid layers
- pretrained SAE feature analysis

The main comparison is not only correct vs wrong answers globally, but correct vs wrong prompt variants within the same fact.

## Current cluster setup

GPU access was tested on the LRZ cluster.

Working GPU test:

- GPU node: gpu-003
- GPU: Tesla V100-PCIE-16GB
- CUDA available: True
- PyTorch: 2.5.1+cu121
- Model tested: google/gemma-2-2b-it

## Useful commands

Start GPU job:

    srun --partition=lrz-hgx-h100-94x4,lrz-hgx-a100-80x4,lrz-dgx-a100-80x8,lrz-v100x2 --gres=gpu:1 --time=02:00:00 --pty bash

Activate environment:

    source ~/venvs/adl-sae/bin/activate

Set Hugging Face cache:

    export HF_HOME=~/hf_cache
    export TRANSFORMERS_CACHE=~/hf_cache

Run Gemma GPU test:

    python tests/test_gemma_gpu.py

Check current jobs:

    squeue -u $USER

Check estimated start time:

    squeue --start -j <JOBID>

## Current status

The cluster environment is working. Gemma can be loaded on GPU and can generate answers.

Next steps:

1. Create a small prompt-variant dataset.
2. Run Gemma on multiple variants of the same fact.
3. Save generated answers and correctness labels.
4. Identify facts where one variant is correct and another is wrong.
5. Extract activations for those switching facts.
6. Run pretrained SAE analysis on the activations.
