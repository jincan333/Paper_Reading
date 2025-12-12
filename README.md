# Safety Alignment Paper Reading

## Overview

This repository tracks and summarizes papers on **safety alignment** for Large Language Models (LLMs). Each entry captures the time, paper link, research question/idea, and the core method—so you can skim the landscape quickly. Contributions via PR are welcome.

## Paper List

| Time | Venue | Paper | Research Question/Idea | Method | Bib |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2025-05 | arxiv2025 | [Lifelong Safety Alignment for Language Models](https://arxiv.org/pdf/2505.20259) | How can LLMs continuously adapt to and defend against unseen and evolving jailbreaking attacks during deployment? | Proposes a **Lifelong Safety Alignment** framework with a competitive **Meta-Attacker** (discovers novel strategies) and **Defender** (resists them), initialized with insights from research papers via GPT-4o. | <details><summary>Bib</summary><pre>@article{wang2025lifelong,<br>  title={Lifelong Safety Alignment for Language Models},<br>  author={Wang, Haoyu and Qin, Zeyu and Zhao, Yifei and Du, Chao and Lin, Min and Wang, Xueqian and Pang, Tianyu},<br>  journal={arXiv preprint arXiv:2505.20259},<br>  year={2025}<br>}</pre></details> |
| 2025-05 | arxiv2025 | [**Does Representation Intervention Really Identify Desired Concepts and Elicit Alignment?**](https://arxiv.org/pdf/2505.18672) | Do representation intervention methods truly localize "harmful" concepts and elicit alignment, particularly when the boundary between harmful and benign is non-linear? | Analyzes limitations of linear erasure; proposes **Concept Concentration (COCA)** to reframe data with explicit reasoning, simplifying the harmful/benign boundary for effective linear erasure and robust defense. | <details><summary>Bib</summary><pre>@article{yang2025does,<br>  title={Does Representation Intervention Really Identify Desired Concepts and Elicit Alignment?},<br>  author={Yang, Hongzheng and Chen, Yongqiang and Qin, Zeyu and Liu, Tongliang and Xiao, Chaowei and Zhang, Kun and Han, Bo},<br>  journal={arXiv preprint arXiv:2505.18672},<br>  year={2025}<br>}</pre></details> |
