# Horizon 每日速递 - 2026-06-24

> 从 81 条内容中筛选出 14 条重要资讯。

---

1. [OpenAI 发布首款与博通合作的定制 AI 推理芯片](#item-1) ⭐️ 9.0/10
2. [《自然》论文质疑微软 Majorana 1 拓扑量子比特声明](#item-2) ⭐️ 8.0/10
3. [谷歌向全球 Play 商店开放替代计费系统](#item-3) ⭐️ 8.0/10
4. [全球终局行动重创主要网络犯罪工具](#item-4) ⭐️ 8.0/10
5. [Mistral 发布 OCR 4，实现企业级文档结构化提取](#item-5) ⭐️ 8.0/10
6. [小米推出 HarnessX，任务中自主优化 AI 智能体脚手架](#item-6) ⭐️ 8.0/10
7. [阿里巴巴发布 Qwen-AgentWorld，创新预测式智能体训练](#item-7) ⭐️ 7.0/10
8. [谷歌再失两名 Gemini 核心骨干转投 Anthropic](#item-8) ⭐️ 6.0/10
9. [数据推翻 AI 取代论：工程师最抗风险](#item-9) ⭐️ 6.0/10
10. [企业实施严格的 Token 配给以控制 AI 预算超支](#item-10) ⭐️ 6.0/10
11. [如何退出谷歌搜索的 AI 数据训练功能](#item-11) ⭐️ 6.0/10
12. [中美顶尖 AI 专家对 AI 军备竞赛表达共同担忧](#item-12) ⭐️ 6.0/10
13. [Mindstone 发布本地优先 AI 智能体编排平台 Rebel](#item-13) ⭐️ 6.0/10
14. [关键 Windows 安全启动证书到期影响数十亿设备](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI 发布首款与博通合作的定制 AI 推理芯片](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 发布了其首款定制 AI 推理芯片（代号 Jalapeno），该芯片由博通联合设计并由台积电在短短九个月内制造完成。据报道，与典型的 AI GPU 相比，这款新芯片可节省约 50%的成本。 这一举措标志着 OpenAI 向垂直整合的重大战略转变，减少了对英伟达主导的 AI 硬件的依赖，并可能颠覆更广泛的 AI 芯片市场。通过掌控自己的定制芯片，OpenAI 可以针对其模型专门优化硬件，从而大幅降低大规模推理成本。 该芯片从设计到生产仅用了九个月时间，OpenAI 声称其 AI 模型被用于加速部分设计和优化过程。博通首席执行官 Hock Tan 强调了 50%的成本节约，而制造工作则由台积电负责。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理芯片是专为高效运行已训练的机器学习模型而设计的专用硬件，这与用于构建模型的训练芯片不同。谷歌和亚马逊等科技巨头已经开发了定制硅片，以减少对通用 GPU 的依赖并降低大规模 AI 部署的运营成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/inferentia/">AI Chip - Amazon Inferentia - AWS</a></li>
<li><a href="https://www.linkedin.com/posts/stuartwesselby_openai-just-made-the-boldest-move-in-ai-activity-7383771944090869762-nZ4y">OpenAI designs custom AI chips with Broadcom, aiming for... | LinkedIn</a></li>
<li><a href="https://www.educative.io/newsletter/system-design/how-ai-hardware-is-redefining-system-design">From chips to chains: How AI hardware is redefining System Design</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 OpenAI 声称其自身模型加速了芯片设计过程表示怀疑，认为这可能是营销噱头。其他人则强调了 50%的成本节约和台积电的制造，同时一些人讨论了将模型权重直接烧录到芯片 ROM 中以实现极致效率的理论概念。

**标签**: `#AI Hardware`, `#Custom Silicon`, `#OpenAI`, `#Semiconductors`, `#LLM Infrastructure`

---

<a id="item-2"></a>
## [《自然》论文质疑微软 Majorana 1 拓扑量子比特声明](https://www.theverge.com/tech/956450/nature-microsoft-quantum-computing-majorana-1-claims) ⭐️ 8.0/10

发表在《自然》杂志上的一篇新评论文章对微软 Majorana 1 量子芯片背后的基础技术提出质疑，反驳了该公司关于实现拓扑量子比特突破的说法。 这一同行评审的反驳直接影响拓扑量子计算研究的轨迹，并可能影响未来的行业投资和微软的战略路线图。它凸显了围绕容错量子硬件声明的激烈科学审查。 微软于 2025 年 2 月发布了 Majorana 1 芯片，声称其利用一种新型拓扑导体材料制造了本质上能抵御局部错误的拓扑量子比特。《自然》杂志的这篇论文专门针对这些底层拓扑超导体声明的有效性提出了质疑。

rss · The Verge · 6月24日 20:54

**背景**: 拓扑量子计算依赖于被称为任意子的奇异准粒子，理论上通过一种称为编织的过程，它们能提供抵御局部噪声和错误的内在保护。微软在这一方法上投入了大量资金，旨在构建容错量子计算机，与其他架构相比，这种计算机进行纠错所需的物理量子比特更少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Majorana_1">Majorana 1 - Wikipedia</a></li>
<li><a href="https://quantumcomputingcourses.com/tutorials/topological-quantum-computing-intro">Topological Quantum Computing: Anyons, Braids, and Inherently...</a></li>

</ul>
</details>

**标签**: `#Quantum Computing`, `#Microsoft`, `#Topological Qubits`, `#Nature`, `#Scientific Peer Review`

---

<a id="item-3"></a>
## [谷歌向全球 Play 商店开放替代计费系统](https://www.theverge.com/policy/956296/google-play-app-store-alternative-billing-fee-antitrust) ⭐️ 8.0/10

谷歌正在全球范围内推出改革，允许在 Play 商店中使用替代计费系统，使开发者能够绕过传统的 30%交易抽成。这一政策转变源于该公司与 Epic Games 就应用商店垄断问题达成的反垄断和解。 这标志着一个改变行业的重大转变，打破了谷歌在 Android 应用计费方面的长期垄断，对移动开发者的收入模式产生了重大影响。这可能会降低消费者的成本，并重塑更广泛的移动应用经济。 即使在法院正式批准 Epic Games 反垄断和解协议之前，这些变化就已经在全球范围内开始实施。开发者现在可以选择使用外部支付系统，而不必被迫使用谷歌专有的计费系统。

rss · The Verge · 6月24日 17:36

**背景**: 历史上，谷歌要求 Play 商店上的所有应用内购买和付费应用必须使用其专有的计费系统，并从中抽取 30%的收入。Epic Games 因这一做法起诉谷歌违反反垄断法，引发了一场具有里程碑意义的法律战，迫使谷歌重新考虑其应用商店政策。

**标签**: `#Android`, `#Mobile Development`, `#Antitrust`, `#Google Play`, `#App Economy`

---

<a id="item-4"></a>
## [全球终局行动重创主要网络犯罪工具](https://arstechnica.com/security/2026/06/one-two-punch-delivered-in-global-operation-disrupts-cybercrime-assembly-line/) ⭐️ 8.0/10

一项名为“终局行动”的全球协调执法行动成功破坏了两个广泛使用的网络犯罪工具。此次同步打击对支持网络犯罪生态系统的基础设施造成了重大影响。 破坏这些工具对“恶意软件即服务”模式和网络犯罪流水线造成了重大打击，增加了犯罪分子发动攻击的难度。这证明了国际合作在打击复杂的跨国网络威胁方面日益显著的有效性。 该行动专门针对网络犯罪生态系统中的赋能者，摧毁了用于促进非法活动的关键基础设施。全球执法机构合作执行了这次同步打击，凸显了执法策略向主动的大规模取缔而非被动应对的转变。

rss · Ars Technica · 6月24日 21:03

**背景**: “终局行动”是一项定期的、协调一致的国际执法行动，旨在瓦解网络犯罪网络及其基础设施。“恶意软件即服务”模式允许技术能力有限的人租用或购买恶意工具，产生了流水线效应，助长了勒索软件和其他网络攻击的激增。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fbi.gov/news/press-releases/operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-of-cybercriminals">Operation Endgame : Coordinated Worldwide Law Enforcement... — FBI</a></li>
<li><a href="https://operation-endgame.com/">Operation Endgame</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#Threat Intelligence`, `#Cybercrime`, `#Malware`

---

<a id="item-5"></a>
## [Mistral 发布 OCR 4，实现企业级文档结构化提取](https://venturebeat.com/data/mistral-launches-ocr-4-turning-document-extraction-into-a-full-enterprise-ai-play) ⭐️ 8.0/10

Mistral AI 发布了 OCR 4，这是一款先进的文档智能模型，能够提取文档的结构化表示，包括边界框、块类型分类和置信度分数。它支持 170 种语言，并可作为单个容器在本地部署，专为受监管行业设计。 此次发布通过提供可追溯的结构化数据而非纯文本，解决了检索增强生成（RAG）管道中的关键瓶颈，这对于企业合规和审计至关重要。其本地部署选项也满足了受监管行业的数据主权需求，这些行业无法使用美国管辖的云 API。 该模型输出用于溯源的局部边界框，对块（如标题、表格、签名）进行分类以便下游路由，并提供置信度分数以自动化“人在回路”的验证。它可通过 Mistral API 和主要云平台获取，定价为每 1000 页 4 美元，批量 API 折扣为 2 美元。

rss · VentureBeat · 6月24日 21:04

**背景**: 传统的光学字符识别（OCR）将扫描文档转换为扁平的、非结构化的文本，这限制了其在复杂 AI 工作流中的效用。检索增强生成（RAG）依赖于准确地分块和检索文档上下文来为大型语言模型提供信息，因此结构化的文档智能对于减少幻觉和确保事实可追溯性至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://anyformat.ai/use-cases/document-intelligence">RAG & Document Intelligence Pipelines | anyformat.ai</a></li>
<li><a href="https://www.spheron.network/blog/self-host-document-intelligence-docling-marker-mineru-rag-guide/">Self-Host Document Intelligence on GPU Cloud... | Spheron Blog</a></li>

</ul>
</details>

**标签**: `#Mistral AI`, `#Document Intelligence`, `#Enterprise AI`, `#OCR`, `#RAG`

---

<a id="item-6"></a>
## [小米推出 HarnessX，任务中自主优化 AI 智能体脚手架](https://venturebeat.com/orchestration/xiaomis-harnessx-rewrites-its-own-ai-scaffolding-mid-task-and-smaller-models-gain-the-most) ⭐️ 8.0/10

小米研究人员推出了 HarnessX 框架，将 AI 智能体脚手架视为一等对象，在任务执行过程中自主重写和优化其代码。这种动态自适应带来了显著的性能提升，尤其是对 Qwen3.5-9B 等较小的语言模型，其在具身规划任务中的性能提升了 44%。 这一进展表明，扩展基础模型并非提升 AI 能力的唯一途径，因为动态、自我改进的脚手架可以显著提升较小模型的性能。它通过用自动化的模块化生成器取代静态、手工制作的脚手架，解决了智能体 AI 开发中的关键工程瓶颈。 HarnessX 通过将模型配置与脚手架配置解耦，在 15 个模型-基准测试组合中实现了平均 14.5%的性能提升。该框架将脚手架视为独立可序列化和可替换的实体，克服了架构纠缠和孤立优化等传统挑战。

rss · VentureBeat · 6月24日 18:45

**背景**: 在 AI 智能体开发中，harness 或 scaffolding（脚手架）是指连接基础模型与环境的操作层，包括提示词、工具集成和内存管理。传统上，这些脚手架是静态且手工编写的，这意味着对模型或操作领域的任何更改都需要手动重写代码，从而为复杂的企业任务制造了巨大的瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/agent-harness">What Is an Agent Harness ? A Beginner's Guide | DataCamp</a></li>
<li><a href="https://zbrain.ai/agent-scaffolding/">Agent Scaffolding : Architecture and Design Patterns for Agentic AI</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#LLM Scaffolding`, `#Machine Learning Research`, `#Autonomous Systems`, `#Agentic AI`

---

<a id="item-7"></a>
## [阿里巴巴发布 Qwen-AgentWorld，创新预测式智能体训练](https://venturebeat.com/technology/alibabas-model-never-trained-as-an-agent-and-improved-agent-performance-across-seven-benchmarks) ⭐️ 7.0/10

阿里巴巴 Qwen 团队发布了 Qwen-AgentWorld，这是一种新颖的方法，训练模型预测环境返回结果而不是在智能体环境中执行动作，从而在七个基准测试中提升了性能。该统一架构涵盖了 MCP、搜索、终端、软件工程、Android、Web 和操作系统等七个领域。 这种范式转变解决了大规模训练智能体时面临的一个主要瓶颈，即允许模型从难以注入到实际生产环境中的模拟边缘情况中学习。通过将世界模型训练作为预热，它显著提升了智能体的性能，并为构建更强大的通用自主智能体铺平了道路。 这些模型采用混合专家（MoE）架构，开源的 35B 版本激活 3B 参数并支持 256K 上下文窗口，同时通过文本可访问性树而非截图来处理 GUI 领域。训练过程使用了超过 1000 万条真实交互轨迹并分为三个阶段，35B 模型权重及 AgentWorldBench 已在 Apache 2.0 许可证下开源。

rss · VentureBeat · 6月24日 19:15

**背景**: 传统的 AI 智能体通常根据环境反馈来训练其下一步动作，但这受到实际生产环境不可预测且难以控制的限制。世界建模逆转了这一过程，通过训练模型根据动作预测下一个环境状态，从而为边缘情况提供了一个受控的模拟器。此外，涵盖 MCP（Model Context Protocol）领域凸显了智能体与标准化外部系统及工具集成的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#machine learning`, `#Alibaba`, `#Qwen`, `#autonomous systems`

---

<a id="item-8"></a>
## [谷歌再失两名 Gemini 核心骨干转投 Anthropic](https://www.ithome.com/0/968/224.htm) ⭐️ 6.0/10

谷歌 Gemini 大模型研发的核心骨干、顶尖 AI 研究员 Jonas Adler 和 Alexander Pritzel 即将离职并加入 Anthropic。此前，Noam Shazeer 和诺贝尔奖得主 John Jumper 也已分别跳槽至 OpenAI 和 Anthropic。 核心研究员的持续流失凸显了谷歌面临的人才流失危机，因为 OpenAI 和 Anthropic 等竞争对手正筹备上市，并利用股权期权积极招募顶尖 AI 人才。这一趋势可能会削弱谷歌在快速发展的 AI 领域的竞争优势，尤其是考虑到谷歌此前曾斥资 27 亿美元来留住 Shazeer 等人才。 值得注意的是，Noam Shazeer 的离职发生在谷歌斥资 27 亿美元收购其创办的 Character.AI 之后不久，此举部分目的是为了请回他牵头 Gemini 的研发。此外，凭借 AlphaFold 蛋白质结构预测系统获得 2024 年诺贝尔化学奖的 John Jumper 近期也从谷歌 DeepMind 跳槽至 Anthropic。

rss · IT之家 · 6月24日 23:10

**背景**: 当前 AI 行业正经历着对顶尖人才的激烈竞争，这主要是由大语言模型和生成式 AI 的快速发展所驱动的。OpenAI 和 Anthropic 等公司正在筹备首次公开募股，这使得它们能够提供丰厚的股权期权，从而将精英研究人员从谷歌等成熟科技巨头那里吸引过来。

**标签**: `#AI industry`, `#talent acquisition`, `#Google`, `#Anthropic`, `#Gemini`

---

<a id="item-9"></a>
## [数据推翻 AI 取代论：工程师最抗风险](https://www.ithome.com/0/968/223.htm) ⭐️ 6.0/10

SignalFire 对超 8000 万名员工的分析显示，工程岗位是科技行业抗风险能力最强的，自 2019 年以来招聘量仅下降 11%，远低于整体 25%的降幅。这一数据直接反驳了 AI 工具正在迅速取代软件工程师的普遍观点。 这挑战了科技行业因 AI 导致大规模失业的普遍担忧，表明 AI 工具目前是在增强而非取代工程人才。它凸显了“杰文斯悖论”的实际应用，即 AI 带来的效率提升反而增加了对工程师的需求，以解决新的复杂问题。 在 12 家头部科技巨头中，2025 年工程师占新员工比例达 55%，高于 2019 年的 46%，而早期初创企业的工程师招聘量增长了 7%。英伟达黄仁勋等行业领袖指出，AI 智能体正倒逼工程师产出更多创新工作，而非让他们变得多余。

rss · IT之家 · 6月24日 23:02

**背景**: “杰文斯悖论”是一个经济学理论，提出当技术提高某种资源的使用效率时，该资源的总消耗量会增加而不是减少。在软件工程领域，AI 编程助手提高了开发者的效率，这降低了软件创建的成本并扩大了项目范围，从而增加了对工程人才的总体需求。

**标签**: `#AI-impact`, `#software-engineering`, `#industry-analysis`, `#employment-trends`, `#tech-layoffs`

---

<a id="item-10"></a>
## [企业实施严格的 Token 配给以控制 AI 预算超支](https://techcrunch.com/2026/06/24/companies-are-scrambling-to-stop-employees-from-maxing-out-ai-budgets-with-small-tasks/) ⭐️ 6.0/10

由于员工在琐碎任务上耗尽了 AI 预算，企业正从无限制使用大语言模型转向严格的 Token 配给和使用政策。这标志着短暂的无节制 Token 消耗时代结束，企业正式进入严格的成本控制时代。 这一趋势凸显了企业 AI 采用中一个关键的运营和财务挑战，迫使工程领导者和 FinOps 团队在创新与严格的成本管理之间取得平衡。它标志着 LLM 运维的成熟，无限制的访问正在被受治理、具备预算意识的工作流所取代。 核心问题源于缺乏监控的员工使用，导致琐碎任务消耗了不成比例的高昂 LLM Token。组织现在正在实施严格的 Token 配给和使用政策，并采用集中式 API 网关来跟踪和限制整个企业的消耗。

rss · TechCrunch · 6月24日 20:09

**背景**: 大语言模型（LLM）通常根据 Token（模型处理的文本块）的数量进行计费。当员工在没有监督的情况下将 AI 工具用于日常任务时，这些 Token 的累积成本可能会迅速升级，这种现象通常与影子 AI 有关。为此，FinOps 和 LLM 运维（LLMOps）等管理实践应运而生，旨在控制 AI 特定的成本，确保企业的 AI 集成在财务上保持可持续。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@yahyahmed007/streamlining-operations-with-large-language-models-a-guide-to-implementation-97cdfea26f10">Streamlining Operations with Large Language Models... | Medium</a></li>
<li><a href="https://tokenpricing.dev/">LLM Token & Cost Calculator — count tokens , estimate cost across...</a></li>

</ul>
</details>

**标签**: `#Enterprise AI`, `#AI Cost Management`, `#LLM Operations`, `#Tech Industry Trends`, `#Shadow AI`

---

<a id="item-11"></a>
## [如何退出谷歌搜索的 AI 数据训练功能](https://www.wired.com/story/how-to-opt-out-of-google-search-new-ai-data-training/) ⭐️ 6.0/10

谷歌更新了其搜索历史功能，将存储用户的交互记录（包括以图搜图等上传的媒体文件）用于训练其 AI 模型，但用户现在可以选择退出此数据收集。 这一更新凸显了大型科技公司扩展 AI 训练数据集与用户日益增长的数据隐私和知情同意担忧之间的持续矛盾。它为用户提供了实用的步骤，以保护其个人搜索和媒体数据不被用于机器学习。 该数据收集专门针对搜索历史和媒体上传（例如用于以图搜图的图片），这些内容现在被保留用于 AI 模型训练。如果用户希望防止其数据被使用，必须主动在账户设置中导航并禁用此新功能。

rss · Wired · 6月24日 22:36

**背景**: 科技公司经常使用用户生成的数据来改进和训练其机器学习模型，这种做法在全球引发了重大的隐私争议。虽然服务条款通常授予数据使用的广泛权限，但最近的法规和用户的反对促使平台引入了更细粒度的 AI 训练退出机制。

**标签**: `#AI Training`, `#Data Privacy`, `#Google Search`, `#Machine Learning`, `#User Consent`

---

<a id="item-12"></a>
## [中美顶尖 AI 专家对 AI 军备竞赛表达共同担忧](https://www.wired.com/story/ai-arms-race-china-us-cooperation/) ⭐️ 6.0/10

《连线》杂志的一篇文章揭示，中美两国顶尖的 AI 研究人员对正在进行的 AI 军备竞赛以及可能发生的灾难性“切尔诺贝利时刻”感到日益焦虑。 这种共同的焦虑标志着一个关键转变，即地缘政治竞争对手认识到不受控制的 AI 发展所带来的共同生存风险。它凸显了在更广泛的技术竞争背景下，国际社会在 AI 安全方面开展合作的紧迫性。 该评论侧重于地缘政治和安全影响而非技术深度，并使用“切尔诺贝利时刻”这一比喻来描述 AI 系统中可能产生全球后果的潜在灾难性故障。

rss · Wired · 6月24日 18:45

**背景**: “切尔诺贝利时刻”指的是 1986 年的核灾难，在此被用作 AI 发展中可能导致广泛危害的突然且灾难性失败的比喻。中美 AI 军备竞赛描述了两国在人工智能领域取得主导地位的激烈竞争，这引发了人们对速度优先于安全的担忧。

**标签**: `#AI Safety`, `#AI Geopolitics`, `#AI Policy`, `#Artificial Intelligence`, `#Tech Industry`

---

<a id="item-13"></a>
## [Mindstone 发布本地优先 AI 智能体编排平台 Rebel](https://venturebeat.com/orchestration/your-enterprise-ai-agents-should-automatically-remember-which-model-is-right-for-which-task-mindstone-built-the-capability-with-rebel) ⭐️ 6.0/10

Mindstone 正式发布了 Rebel，这是一款本地优先的 AI 智能体编排平台，它利用 Markdown 文件和组织记忆层自动将任务路由到最优的 AI 模型。该平台采用 Fair Source 许可证，允许 100 人以下的团队免费使用，而更大的组织则需要购买企业许可证。 通过基于共享的组织记忆在本地和云端模型之间动态切换，Rebel 帮助企业优化 API 成本、维护数据隐私并避免供应商锁定。其本地优先、基于 Markdown 的架构为拥挤市场中复杂的、依赖数据库的智能体框架提供了一种更简单、更透明的替代方案。 Rebel 将智能体指令、状态和记忆层级存储在本地 Markdown 文件（如`agents.md`）中，以最大限度地减少 Token 开销并防止供应商锁定。它还具有用于可重复工作流的“Skills”、用于调整智能体行为的“Operators”以及用于定时后台任务的“Automations”，目前支持 macOS 和 Windows。

rss · VentureBeat · 6月24日 23:02

**背景**: AI 智能体编排平台负责协调多个 AI 模型和工具以完成复杂的工作流，但许多平台需要繁重的云基础设施和数据库管理。本地优先软件将数据主要保存在用户本地设备上，从而增强了隐私性并减少了对远程服务器的依赖。LLM 路由是一种动态将任务分配给最合适 AI 模型的技术，旨在平衡性能与成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Local-first_software">Local - first software - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/llm-routing-ai-costs-optimisation-without-sacrificing-quality-3ypff">LLM Routing : AI Costs Optimisation Without Sacrificing Quality</a></li>
<li><a href="https://fair.io/licenses/">The following licenses fit the Fair Source Definition.</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#AI Orchestration`, `#Enterprise AI`, `#LLM Routing`, `#Developer Tools`

---

<a id="item-14"></a>
## [关键 Windows 安全启动证书到期影响数十亿设备](https://www.zdnet.com/article/secure-boot-certificate-updates-2026/) ⭐️ 6.0/10

对 Windows 安全启动和 Linux shim 引导加载程序至关重要的 Microsoft UEFI CA 2011 安全证书即将到期，并将被新的 Windows UEFI CA 2023 证书取代。这一过渡影响超过 10 亿台 Windows PC 和多个 Linux 发行版，需要验证系统是否准备就绪。 如果在到期前未使用新证书更新系统，设备可能无法启动或拒绝合法的操作系统更新，从而给企业管理员和普通消费者带来重大中断。这凸显了现代操作系统中公钥基础设施维护的关键性质。 新的 Microsoft Windows UEFI CA 2023 证书将用于签署 Windows 启动组件，而 2011 证书的到期特别影响由微软签署的 Linux shim 引导加载程序。用户和管理员可以手动应用数据库更新，或安装包含 2023 证书的 OEM 制造商最新 BIOS 更新。

rss · ZDNet · 6月24日 20:34

**背景**: 安全启动（Secure Boot）是由 PC 行业开发的一项安全标准，旨在确保设备仅使用原始设备制造商信任的软件进行启动。它依赖于存储在系统 UEFI 固件中的加密证书所锚定的信任链，这些证书必须定期轮换以维护安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/perez987/OpenCore-and-UEFI-Secure-Boot/blob/main/guide/Windows+UEFI+CA+2023.md">OpenCore-and- UEFI -Secure-Boot/guide/Windows UEFI CA 2023.md...</a></li>
<li><a href="https://www.linuxteck.com/secure-boot-linux-key-expires/">Secure Boot Linux 2026: Microsoft 's Key Expires June 27</a></li>
<li><a href="https://www.elevenforum.com/t/updating-microsoft-secure-boot-keys.22477/">Updating Microsoft Secure Boot keys | Windows 11 Forum</a></li>

</ul>
</details>

**标签**: `#Windows`, `#Cybersecurity`, `#Systems Administration`, `#Secure Boot`, `#PKI`

---

