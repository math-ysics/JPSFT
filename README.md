# Llama-JPSFT

This repository contains the code for the data processing and training of the open-weights model Llama-JPSFT. Supervised fine-tuning was performed on a generative pre-trained transformer on a select ~130,000 query-response pairs from a diverse corpus of anonymized, scraped chat data, with a priority on casual conversation. BF16 mixed precision training was executed on NVIDIA A100 Tensor Core GPUs and precision reduction/quantization from safetensors to GGUF was then completed for q8_0, q6_k, and q4_k_m models. This project targets standard SFT as well as instruction-tuning for GPT-based architectures to generate significantly improved coherent and context-aware responses in multi-speaker conversations in casual Japanese.

約13万件の多様な匿名化されたチャットデータを基に、教師あり学習による微調整が実施されました。

Repository: https://github.com/math-ysics/JPSFT

Instruct Model: https://huggingface.co/ai-net/Llama-JPSFT

Precision Reduction and Quantization: https://huggingface.co/ai-net/Llama-JPSFT-GGUF

例えば:

{{user}}\
よろしく！

llama-JPSFT-GGUF/llama-jpsft-q8_0.gguf\
お、よろしくなぁ

--

{{user}}\
寂しいなー

llama-JPSFT-GGUF/llama-jpsft-q8_0.gguf\
そりゃそうだよ
