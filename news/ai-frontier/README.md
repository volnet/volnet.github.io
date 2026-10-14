# AI 前沿日报

> 不追逐所有 AI 新闻，只追踪那些**改变能力边界、改变系统构建方法、改变产业组织方式**的进展。
>
> 既看宏观突破：模型、算力、世界模型与产业路线；也看微观信号：一次失败的 Agent 实验、一种更可靠的上下文管理方式、一个降低成本的工具接口。后者往往能更快转化为真实产品与团队实践。

## 日报归档

每月一篇，**新日期在前**；每条保留真实发布日期、精炼摘要、推荐理由与一手末级链接。

- [2026 年 10 月](202610.md)
- [2026 年 9 月](202609.md)
- [2026 年 8 月](202608.md)

## 六个研究问题

这不是以公司排名为轴的信息流，而是围绕六个问题建立的观察体系。不同公司的消息只有真正回答这些问题时才值得收录。

### 01｜智能的边界如何移动？——模型、训练与推理

关注新的基础模型和模型范式、推理能力、长上下文、多模态、训练与推理范式；尤其留意**不是单纯扩大参数规模**却改变能力/成本曲线的技术。

**优先信源**
- [OpenAI · Research](https://openai.com/research/) / [News](https://openai.com/news/)
- [Google DeepMind · Research](https://deepmind.google/research/) / [Blog](https://deepmind.google/discover/blog/)
- [Google Research · Blog](https://research.google/blog/)
- [Anthropic · Research](https://www.anthropic.com/research) / [News](https://www.anthropic.com/news)
- [DeepSeek · GitHub](https://github.com/deepseek-ai) / [Meta FAIR](https://ai.meta.com/research/)

### 02｜Agent 如何从演示走向可靠生产？——Harness、上下文与工程实践

重点不是「模型会不会做」，而是**能否长时间、低成本、可恢复、可审计地把事情做完**。持续追踪 context engineering、memory、tool use、evals、computer use、multi-agent、sandbox、coding agent、故障案例、生产延迟与成本。

**优先信源**
- [OpenAI Developers · Blog](https://developers.openai.com/blog/) / [Codex](https://github.com/openai/codex) / [API Changelog](https://platform.openai.com/docs/changelog)
- [Anthropic · Engineering](https://www.anthropic.com/engineering) / [Claude Code Releases](https://github.com/anthropics/claude-code/releases)
- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) / [Model Context Protocol](https://modelcontextprotocol.io/)
- [Google Agent Development Kit](https://github.com/google/adk-python/releases)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

**微观信号筛选**：一条工程实践必须说清楚原来卡在哪里、团队验证了什么、适用边界是什么、我们能借鉴什么；普通教程不构成新闻。

### 03｜AI 能否理解并作用于真实世界？——空间智能与 Physical AI

从「识别图片、生成视频」走向**可导航、可交互、可模拟、可执行的世界模型**：3D/4D 表征、World Models、Spatial Intelligence、具身智能、VLA、robotics、simulation、synthetic data、real-to-sim-to-real。

**优先信源**
- [World Labs · Blog](https://www.worldlabs.ai/blog) / [官网](https://www.worldlabs.ai/)
- [Stanford Vision and Learning Lab](https://svl.stanford.edu/)
- [NVIDIA Research](https://research.nvidia.com/) / [NVIDIA Developer Blog](https://developer.nvidia.com/blog/)
- [Google DeepMind · Robotics](https://deepmind.google/discover/)

**特别关注**：World Labs 的 Marble、Atlas、World API 等世界模型与平台能力；重要的新一代空间基础模型应优先进入「核心突破与模型发布」。

### 04｜是否出现了不同于 LLM 的新智能路径？——小实验室与异构模型

避免只在头部实验室里寻找答案。关注**结构化决策、概率预测、专用模型、神经符号、非生成式 AI**，以及用更少成本完成某类高频任务的新范式。

**优先信源**
- [TypeSafe AI](https://typesafe.ai/)：Jev / System One Models、RLCD、结构化决策
- [TypeSafe AI · Jev 介绍](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- [arXiv · Artificial Intelligence](https://arxiv.org/list/cs.AI/recent) / [Machine Learning](https://arxiv.org/list/cs.LG/recent)
- [GitHub Trending](https://github.com/trending)

**判断标准**：看独立评测、概率校准、准确率、延迟、单位调用成本和真实 Agent routing/审核/评分应用，而非只看厂商口径。

### 05｜算力与基础设施如何重塑 AI 的经济性？——芯片、推理和部署

观察 AI Infra、GPU/NPU、推理引擎、模型部署、分布式训练、缓存与调度。真正重要的问题是：**什么技术让同样预算能完成更多可靠任务？**

**优先信源**
- [NVIDIA Research](https://research.nvidia.com/) / [NVIDIA Developer Blog](https://developer.nvidia.com/blog/)
- [NVIDIA 开源项目](https://github.com/NVIDIA)
- [DeepSeek 开源项目](https://github.com/deepseek-ai)
- [OpenAI Developers](https://developers.openai.com/) / [Google AI for Developers](https://ai.google.dev/)

### 06｜AI 将怎样改变科研、组织与社会？——战略与长期判断

追踪 AI 自主研发 AI、可解释性、安全与治理、劳动力与经济、开源/闭源格局、研究机构判断。将**可验证事实**与**作者推演**分开，不因为观点声量大就将其当作技术突破。

**优先信源**
- [Dario Amodei · 个人文章](https://darioamodei.com/)（独立于 Anthropic News 检查，引用时使用具体文章页）
- [Stanford HAI](https://hai.stanford.edu/) / [Stanford CRFM](https://crfm.stanford.edu/)
- [Anthropic · Research](https://www.anthropic.com/research)
- [OpenAI · Research](https://openai.com/research/)
- [Google DeepMind · Responsibility & Safety](https://deepmind.google/responsibility-and-safety/)

## 编辑标准

**A｜宏观前沿**：真正改变模型能力、Agent 架构、Physical AI、AI 基础设施或产业路线的进展。  
**B｜微观信号**：开发者/工程团队刚验证的技术细节、新实践、新工具、失败教训，能够直接启发「如何用好 AI、产品怎么设计、研发下一步做什么」。

每期精选 **4–7 条**，有合适内容时保留 **1–3 条微观信号**。优先过去 24 小时，必要时回溯并注明**实际发布日期**。同一事件只出现一次；没有足够价值的更新，宁缺毋滥。

每条坚持四项：**机构/作者＋标题＋日期；摘要；推荐理由；具体一手末级 URL**。论文优先 arXiv abs，工程变更优先官方 changelog / GitHub Release。排除普通教程、招聘、活动预告、纯营销和无法核实的二手传闻。

日报按【核心突破与模型发布】【前沿论文与技术路线】【行业战略与重要动态】组织；分类用于阅读，六个研究问题用于决定**什么值得研究**。
