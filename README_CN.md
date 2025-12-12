# 安全对齐论文阅读

## 概览

本仓库追踪并总结关于大语言模型（LLMs）**安全对齐**的论文。每个条目包含时间、论文链接、研究问题/思路以及核心方法——以便您快速浏览该领域动态。欢迎提交 PR 贡献。

## 论文列表

| 时间 | 发表处 | 论文 | 研究问题/思路 | 方法 | 引用 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2025-05 | arxiv2025 | [Lifelong Safety Alignment for Language Models](https://arxiv.org/pdf/2505.20259) | 如何使大语言模型（LLMs）能够持续适应并防御在部署过程中出现的未知和不断演变的越狱攻击？ | 提出了一个 **Lifelong Safety Alignment（终身安全对齐）** 框架，包含两个竞争组件：**Meta-Attacker**（元攻击者，用于主动发现新的越狱策略）和 **Defender**（防御者，用于抵御这些攻击），并利用 GPT-4o 从研究论文中提取见解来初始化攻击者。 | <details><summary>Bib</summary><pre>@article{wang2025lifelong,<br>  title={Lifelong Safety Alignment for Language Models},<br>  author={Wang, Haoyu and Qin, Zeyu and Zhao, Yifei and Du, Chao and Lin, Min and Wang, Xueqian and Pang, Tianyu},<br>  journal={arXiv preprint arXiv:2505.20259},<br>  year={2025}<br>}</pre></details> |
| 2025-05 | arxiv2025 | [Does Representation Intervention Really Identify Desired Concepts and Elicit Alignment?](https://arxiv.org/pdf/2505.18672) | 表征干预（Representation Intervention）方法是否真的定位了“有害”概念并引出对齐行为，尤其是在有害与无害的边界是非线性的情况下？ | 分析了线性擦除的局限性；提出了 **Concept Concentration (COCA)**，通过显式推理重构数据，简化有害/无害边界，从而实现有效的线性擦除和稳健的防御。 | <details><summary>Bib</summary><pre>@article{yang2025does,<br>  title={Does Representation Intervention Really Identify Desired Concepts and Elicit Alignment?},<br>  author={Yang, Hongzheng and Chen, Yongqiang and Qin, Zeyu and Liu, Tongliang and Xiao, Chaowei and Zhang, Kun and Han, Bo},<br>  journal={arXiv preprint arXiv:2505.18672},<br>  year={2025}<br>}</pre></details> |
