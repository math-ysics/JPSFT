# JPSFT

This repository contains the code for the data processing and training of the open-weights model Llama-JPSFT. Supervised fine-tuning is performed on a generative pre-trained transformer on a select ~150,000 query-response pairs from a diverse corpus of anonymized, scraped chat data, with a priority on casual conversation. BF16 mixed precision training was executed on NVIDIA A100 Tensor Core GPUs. Precision reduction/quantization from safetensors to GGUF was then completed for FP16, q8_0, q6_k, and q4_k_m models. This project focuses on standard SFT as well as instruction-tuning for GPT-based architectures to generate significantly improved coherent and context-aware responses in multi-speaker conversations in Japanese.

Instruct Model: https://huggingface.co/ai-net/llama-JPSFT

Precision Reduction and Quantization: https://huggingface.co/ai-net/llama-JPSFT-GGUF
