# Horizon 每日速递 - 2026-07-12

> 从 120 条内容中筛选出 20 条重要资讯。

---

1. [ClickHouse 实现 PgBouncer 吞吐量 4 倍提升](#item-1) ⭐️ 8.0/10
2. [天津大学研发毫秒级热脉冲技术实现铂族催化剂超快精准制备](#item-2) ⭐️ 8.0/10
3. [中国科学家发现植物根系“避腐性”以规避腐烂物质](#item-3) ⭐️ 8.0/10
4. [潜伏 13 年的 U-Boot 高危漏洞曝光，威胁数百万设备](#item-4) ⭐️ 8.0/10
5. [人工智能发现 Linux 内核中存在 15 年的 Root 级漏洞](#item-5) ⭐️ 8.0/10
6. [强化学习实现了量子处理器的实时重新校准。](#item-6) ⭐️ 8.0/10
7. [英伟达、CoreWeave 与 Nebius 的 GPU 循环融资](#item-7) ⭐️ 7.0/10
8. [智谱 AI 启动“摸高”计划，全面聚焦 AGI 研究](#item-8) ⭐️ 7.0/10
9. [黑客借 GitHub 和 Go 模块发起“Muck and Load”投毒攻击](#item-9) ⭐️ 7.0/10
10. [美国国防部启动低成本可消耗无人机蜂群招标以替代“死神”](#item-10) ⭐️ 7.0/10
11. [CISA 在密码泄露时临时制定响应预案](#item-11) ⭐️ 7.0/10
12. [OpenAI 安全主管 Johannes Heidecke 离职](#item-12) ⭐️ 7.0/10
13. [“Slopsquatting”：一种由 AI 引发的新型软件供应链威胁](#item-13) ⭐️ 7.0/10
14. [监管重组后腾讯将仅持有 AI 初创公司 Manus 少数股份](#item-14) ⭐️ 6.0/10
15. [欧几里得望远镜发现破纪录的古老类星体](#item-15) ⭐️ 6.0/10
16. [AMD 发布 PEPS 技术：纹理参数减少 25%](#item-16) ⭐️ 6.0/10
17. [Armada OS 让骁龙掌机变身 Steam Deck 运行 3A 游戏](#item-17) ⭐️ 6.0/10
18. [英伟达 RTX 50 显卡隐藏热点传感器被解锁，揭示严重局部过热问题](#item-18) ⭐️ 6.0/10
19. [AI 对音乐版权及训练成本的影响](#item-19) ⭐️ 6.0/10
20. [微软报告碳排放量激增 25%](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [ClickHouse 实现 PgBouncer 吞吐量 4 倍提升](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres) ⭐️ 8.0/10

ClickHouse 工程师通过利用 SO_REUSEPORT 套接字选项并实现自定义的 peering 机制来处理跨进程的查询取消，成功将 PgBouncer 的吞吐量提升了 4 倍。 这项重大的性能优化解决了 PostgreSQL 连接池中的一个主要瓶颈，直接造福于管理高并发环境的系统和数据库工程师。它也凸显了数据库代理工具为了应对现代云基础设施需求而不断演进的趋势。 peering 机制确保了当查询取消请求落入不拥有该会话的进程时，它会被正确转发给拥有该会话的进程。该实现依赖于 SO_REUSEPORT，允许多个工作进程监听同一端口，并由内核对传入连接进行负载均衡。

hackernews · saisrirampur · 7月11日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=48872874)

**背景**: PgBouncer 是一个轻量级的 PostgreSQL 连接池，用于限制到数据库的并发连接数。SO_REUSEPORT 套接字选项允许多个进程或线程绑定到同一个端口，使内核能够将传入的网络连接直接分配给各个工作进程，从而减少锁争用并提高吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://man7.org/linux/man-pages/man7/socket.7.html">socket (7) - Linux manual page</a></li>
<li><a href="https://www.f5.com/company/blog/nginx/socket-sharding-nginx-release-1-9-1">Socket Sharding in NGINX Release 1.9.1 | F5</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 peering 机制和 SO_REUSEPORT 的技术细节表现出浓厚兴趣，有人询问这些功能是否为 PgBouncer 内置。其他人则分享了使用 Yandex 的 Odyssey 和 pgdog 等替代的可扩展连接池的积极经验，或者讨论了在 Kubernetes 中部署多个 PgBouncer 实例以应对云提供商停机的方案。

**标签**: `#PostgreSQL`, `#PgBouncer`, `#Performance Optimization`, `#Systems Engineering`, `#Database Proxy`

---

<a id="item-2"></a>
## [天津大学研发毫秒级热脉冲技术实现铂族催化剂超快精准制备](https://www.ithome.com/0/975/564.htm) ⭐️ 8.0/10

天津大学研究团队提出“瞬态组装”策略，利用毫秒级周期热脉冲技术实现了铂族金属核壳结构催化剂的超快、原子级精准合成。该成果发表于《科学》杂志，将制备时间从数小时缩短至数分钟，并降低了 90%的能耗。 这一催化剂制造范式的转变显著降低了高性能铂族催化剂的生产成本和能源消耗。所得催化剂在氢燃料电池中实现了高达 15.2 千瓦/克铂的额定功率，将加速清洁能源技术的商业化进程。 该技术将铂壳厚度精准控制在三个原子层，优化了几何与电子效应以释放最大催化活性。它通过驱动纳米晶在非平衡高能瞬态演变中完成组装，克服了传统依赖热力学平衡态方法的局限性。

rss · IT之家 · 7月11日 10:43

**背景**: 铂族金属是现代能源和化工产业的关键催化材料。构建与非贵金属的核壳结构是兼顾高催化活性与低贵金属用量的关键，其利用核壳界面的晶格应变和配体效应来提升性能。传统合成方法依赖于复杂、高能耗且缓慢的高温热力学平衡过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/42424468/">Transient assembly of precision-tuned platinum-skin intermetallic...</a></li>
<li><a href="https://en.tju.edu.cn/info/1010/13416.htm">Chinese Researchers Develop Fast, Precise Method for...</a></li>

</ul>
</details>

**标签**: `#materials-science`, `#catalyst-technology`, `#hydrogen-fuel-cells`, `#clean-energy`, `#scientific-breakthrough`

---

<a id="item-3"></a>
## [中国科学家发现植物根系“避腐性”以规避腐烂物质](https://www.ithome.com/0/975/545.htm) ⭐️ 8.0/10

西北农林科技大学的研究团队在《科学》杂志上发表论文，首次发现并定义了一种名为“避腐性”的根系全新向性运动。研究揭示，植物根系能够主动感知腐烂植物形成的酸性微环境，并通过弯曲生长来避开富含病原体的区域。 这一突破填补了关于不可移动植物如何躲避土传病原体的重大认知空白，将植物向性调控网络的认知拓展到了经典生长素模型之外。它还为精准农业提供了新的理论指导，例如优化秸秆还田实践以及培育具有更强避腐能力的“智慧型”作物。 该机制依赖于“RGF-RGFR 肽-受体 pH 感应模块”，将不对称的酸化信号转化为脱落酸（ABA）的不均匀分布，从而在不依赖生长素的情况下驱动根系弯曲。有趣的是，这种回避反应对腐烂的植物组织具有高度特异性，而对腐烂的动物组织则没有反应。

rss · IT之家 · 7月11日 10:01

**背景**: 向性运动是植物由外部刺激（如重力）引发的定向生长反应。传统上，这些生长决策被认为主要由植物激素生长素调控。理解替代信号通路（如 pH 值感应和脱落酸分布），为植物如何与复杂的土壤环境相互作用提供了更全面的视角。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://phys.org/news/2026-07-newly-saprotropism-roots-decaying-animal.html">Newly identified 'saprotropism' helps roots avoid decaying plant...</a></li>
<li><a href="https://bioengineer.org/plant-roots-avoid-rot-by-steering-clear-of-infected-areas/">Plant Roots Avoid Rot by Steering Clear of Infected Areas</a></li>

</ul>
</details>

**标签**: `#Biology`, `#Plant Science`, `#Scientific Breakthrough`, `#Academic Research`, `#Science Journal`

---

<a id="item-4"></a>
## [潜伏 13 年的 U-Boot 高危漏洞曝光，威胁数百万设备](https://www.ithome.com/0/975/531.htm) ⭐️ 8.0/10

固件安全公司 Binarly 披露了 U-Boot 引导程序中的六个高危漏洞，其中包括两个自 2013 年起潜伏的、可导致任意代码执行的关键缺陷。这些漏洞存在于用于安全启动的 FIT 镜像格式的核心签名验证代码中。 由于 U-Boot 是使用最广泛的开源引导程序，这些漏洞可能影响从路由器到服务器的数百万台嵌入式设备。利用这些漏洞可使攻击者在操作系统启动前获得控制权，从而绕过安全功能或植入持久的固件后门。 最关键的漏洞源于 fdt_get_name 函数返回值未经验证，攻击者可利用畸形的 FIT 镜像触发栈缓冲区溢出或覆盖返回地址。虽然补丁已合并至 U-Boot 主分支，但硬件厂商仍需进行适配和分发，这意味着许多老旧设备可能永远无法获得修复。

rss · IT之家 · 7月11日 08:54

**背景**: U-Boot 是一款广泛使用的开源引导程序，负责在操作系统启动前初始化 CPU 和内存等硬件组件。它使用扁平镜像树（FIT）格式来打包并通过加密签名验证固件镜像，确保在安全启动过程中仅执行受信任的代码。扁平设备树（FDT）是该过程中使用的一种数据结构，用于向操作系统描述系统的硬件配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.u-boot-project.org/en/latest/usage/fit/index.html">Flat Image Tree ( FIT ) — Das U - Boot unknown version documentation</a></li>
<li><a href="https://blog.csdn.net/ermuzhi/article/details/9299155">Flattened Device Tree ( FDT )-CSDN博客</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#Embedded Systems`, `#U-Boot`, `#Vulnerability Disclosure`, `#Firmware Security`

---

<a id="item-5"></a>
## [人工智能发现 Linux 内核中存在 15 年的 Root 级漏洞](https://www.wired.com/story/security-news-this-week-ai-found-a-root-bug-in-linux-that-everyone-missed-for-15-years/) ⭐️ 8.0/10

人工智能成功识别出 Linux 内核中一个存在了 15 年且未被人类研究人员发现的严重 Root 级漏洞。这标志着人工智能在自动化安全研究和漏洞发现方面的应用取得了重大突破。 这一发现证明了网络安全领域的范式转变，表明人工智能能够有效地分析复杂的基础代码库，找出逃避传统人工审计的深层缺陷。它凸显了人工智能在保护关键开源基础设施以及改变漏洞研究方式方面的巨大潜力。 该漏洞是一个 Root 级别的缺陷，意味着它可能使攻击者获得对受影响系统的完全管理员控制权。该漏洞 15 年来未被发现，凸显了 Linux 内核的极大复杂性以及以往人工和自动化扫描方法的局限性。

rss · Wired · 7月11日 10:30

**背景**: Linux 内核是 Linux 操作系统的核心组件，负责管理全球众多服务器和云基础设施的系统资源和硬件交互。Root 级漏洞是最严重的安全缺陷类型，因为它们允许攻击者绕过所有安全机制并获得对系统的完全控制。自动化漏洞发现使用算法和人工智能扫描源代码以寻找表明安全缺陷的模式，旨在比人工审计员更快地发现漏洞。

**标签**: `#Linux`, `#Cybersecurity`, `#Artificial Intelligence`, `#Vulnerability Discovery`, `#Systems Security`

---

<a id="item-6"></a>
## [强化学习实现了量子处理器的实时重新校准。](https://arstechnica.com/science/2026/07/quantum-error-correction-can-constantly-recalibrate-a-processor/) ⭐️ 8.0/10

研究人员将强化学习应用于动态调整量子控制算法，使处理器能够实时持续重新校准并纠正错误。该系统通过评估大约 1000 个控制参数的不同配置，寻找限制错误的最有效设置。 这种方法通过将错误校正从静态的预校准状态转变为持续的动态调整，解决了量子计算中的一个关键瓶颈。它显著提高了硬件的稳定性，并为更可靠且更具扩展性的实用量子处理器铺平了道路。 强化学习代理专门操纵大约 1000 个控制参数，并在运行期间对其限制量子错误的有效性进行评分。这种实时反馈循环使系统能够适应环境噪声和硬件漂移，而无需人工干预或系统停机。

rss · Ars Technica · 7月10日 23:02

**背景**: 量子处理器对环境噪声高度敏感，这会导致量子比特失去其量子态并引入计算错误。量子错误校正对于修复这些错误至关重要，但它传统上需要复杂的静态校准过程，难以跟上实时的硬件波动。强化学习是一种机器学习类型，代理通过试错来学习做出决策，它提供了一种动态自动化和优化这一复杂校准过程的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/science/2026/07/quantum-error-correction-can-constantly-recalibrate-a-processor/">Quantum error correction can constantly recalibrate... - Ars Technica</a></li>
<li><a href="https://odr.chalmers.se/items/4e61f1c0-42da-420d-9cd3-0b47b7bb13ed/full">Deep Reinforcement Learning for Quantum Error Correction</a></li>

</ul>
</details>

**标签**: `#Quantum Computing`, `#Quantum Error Correction`, `#Reinforcement Learning`, `#Machine Learning`

---

<a id="item-7"></a>
## [英伟达、CoreWeave 与 Nebius 的 GPU 循环融资](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 7.0/10

一项分析详细揭示了英伟达与 CoreWeave 和 Nebius 等 AI 云提供商之间复杂的财务关系及潜在的“循环融资”，引发了行业辩论。这种审查聚焦于英伟达对这些新兴云服务商的巨额股权投资是否最终用于购买其自身的 GPU。 了解这些财务结构对于评估当前 AI 基础设施热潮的真实经济可行性及潜在的过度建设至关重要。如果增长严重依赖循环资本流动而非真正的最终用户需求，这可能预示着即将到来的市场调整或泡沫破裂。 批评者指出，英伟达的投资（如对 CoreWeave 的 20 亿美元入股）仅占这些新兴云服务商巨额资本支出的一小部分，从而质疑“循环”这一前提。同时，观察人士正将焦点转向更具体的指标，如每 token 的投资回报率、企业 token 预算，以及部署延迟对限制过剩产能的影响。

hackernews · adletbalzhanov · 7月11日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48873836)

**背景**: CoreWeave 和 Nebius 等“新兴云服务商”是专门为 AI 工作负载提供可扩展 GPU 资源的云计算提供商，与 AWS 等传统超大规模云厂商竞争。在此背景下，“循环融资”指的是一种策略，即硬件制造商向客户进行股权投资，而客户使用这些资金购买该制造商的产品，从而人为地推高收入和需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/spandan-bhattacharya_aieconomy-circularfinancing-nvidia-activity-7381400765505990657-mdT7">How NVIDIA , Oracle, and OpenAI fuel AI boom with circular financing</a></li>
<li><a href="https://medium.com/write-a-catalyst/the-burn-rate-crisis-tracing-the-circular-billions-of-the-ai-arms-race-d32bd5960678">The Burn Rate Crisis: Tracing the Circular Billions of the AI ... | Medium</a></li>
<li><a href="https://thenextweb.com/news/nvidia-40bn-ai-equity-investments-2026">NVIDIA tops $40bn in AI equity bets in 2026</a></li>

</ul>
</details>

**社区讨论**: 社区普遍质疑文章关于“循环融资”的前提，指出英伟达的投资仅占新兴云服务商由多种资金来源支持的总资本支出的一小部分。用户不再争论循环性，而是对这些建设的实际经济可行性更感兴趣，重点关注每 token 的投资回报率、硬件利用率等指标，以及部署延迟是否实际上能防止闲置数据中心的大量过剩。

**标签**: `#AI-Infrastructure`, `#GPU-Market`, `#Industry-Analysis`, `#Venture-Capital`, `#Nvidia`

---

<a id="item-8"></a>
## [智谱 AI 启动“摸高”计划，全面聚焦 AGI 研究](https://www.ithome.com/0/975/620.htm) ⭐️ 7.0/10

智谱 AI 创始人唐杰发布内部信宣布启动“摸高”战略计划，承诺公司将优先进行 AGI 研究而非短期商业变现。公司计划投入百亿级资源攻坚机械可解释性，并同步推进长程任务、自治智能体和完全自我训练等技术。 这一战略转向凸显了头部 AI 公司越来越倾向于优先实现 AGI 基础突破和 AI 安全，而非立即进行产品变现。对机械可解释性的巨额投入表明，随着模型自主性不断增强，业界正在采取主动措施来推进 AI 对齐和安全治理。 “摸高”计划聚焦四大核心引擎：长程任务、自治智能体系统、完全自我训练和极致安全治理。值得注意的是，公司旨在通过机械可解释性厘清模型决策背后的神经元逻辑，从而推动系统从黑盒向透明可解释转变。

rss · IT之家 · 7月11日 14:35

**背景**: 机械可解释性是 AI 安全的一个分支，旨在逆向工程神经网络以准确理解它们如何计算输出，类似于理解计算机程序。随着 AI 模型规模和自主性的增长，长程任务和自我训练等技术不断突破模型能力的边界，这使得可解释性对于确保这些系统与人类价值观对齐且不出现意外行为至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hub.baai.ac.cn/view/27404">2023北京智源大会｜Max Tegmark教授：以 机 械 可 解 释 性 去掌控AI...</a></li>
<li><a href="https://fisherdaddy.com/posts/the-urgency-of-interpretability#what-we-can-do/">解 读 AI 的迫切 性 • Dario Amodei | FisherAI</a></li>

</ul>
</details>

**标签**: `#AGI`, `#AI-strategy`, `#interpretability`, `#AI-safety`, `#Zhipu-AI`

---

<a id="item-9"></a>
## [黑客借 GitHub 和 Go 模块发起“Muck and Load”投毒攻击](https://www.ithome.com/0/975/577.htm) ⭐️ 7.0/10

安全研究人员发现了一起名为“Muck and Load”的大规模供应链攻击，黑客通过 GitHub 上的恶意 Go 模块分发远控木马和加密货币挖矿程序。攻击者利用 GitHub Actions 人为膨胀软件包版本，并采用“死信解析器”技术从公共平台动态获取加密载荷。 此次攻击凸显了供应链安全中一种新颖的规避技术，展示了攻击者如何滥用 GitHub Actions 等 CI/CD 管道来绕过基于版本的检测机制。这对开发者（尤其是 Web3 和游戏领域的开发者）构成了重大风险，因为他们经常下载未经第三方验证的工具和脚本。 该恶意 Go 模块利用 GitHub Actions 每分钟强制推送重写的日志文件，在几个月内生成了超过 1200 个版本，从而制造出大量伪版本。更广泛的攻击活动涉及 190 个账户下的 222 个诱饵仓库，这些仓库均共享统一的提交邮箱指纹，并主要针对加密货币、游戏外挂和机器人工具。

rss · IT之家 · 7月11日 11:14

**背景**: 供应链攻击是指攻击者破坏被其他应用程序广泛使用的软件组件或代码仓库，从而将恶意代码注入下游系统。GitHub Actions 是一个自动化软件工作流的 CI/CD 平台，而 Go 模块是 Go 编程语言的标准依赖管理系统。攻击者经常通过发布恶意包或滥用自动化功能来利用这些生态系统，以隐藏其活动并逃避安全扫描器的检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/features/actions">GitHub Actions · GitHub</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#Supply Chain Security`, `#GitHub`, `#Go`, `#Malware`

---

<a id="item-10"></a>
## [美国国防部启动低成本可消耗无人机蜂群招标以替代“死神”](https://www.ithome.com/0/975/550.htm) ⭐️ 7.0/10

美国国防创新部门（DIU）启动了“蜂群模块化飞行器”（MMA）项目，寻求低成本、可消耗的无人机蜂群方案以替代昂贵的 MQ-9“死神”等平台。该计划旨在 2031 财年实现 20 架无人机的初始作战能力，投标截止日期为 2026 年 7 月 24 日。 这标志着现代战争战略的重大转变，即从依赖少数高价值资产转向部署大规模、廉价且可消耗的无人系统。这反映了军方需要通过数量优势压制先进防空网络，同时最大限度降低战斗损失带来的财务影响的需求。 MMA 无人机必须具备 2800 磅的有效载荷能力、2300 海里的作战半径，以及用于快速重新配置的开放式模块化架构。此外，它们需要 25 千瓦的供电和 5 千瓦的散热能力以支持各类传感器和武器，并支持一名操作员同时控制多架无人机。

rss · IT之家 · 7月11日 10:25

**背景**: “可消耗型”（attritable）无人机是一类新型无人机，其设计成本足够低，使得在战斗中损失它们成为可接受的风险，从而填补了廉价消耗型无人机与 MQ-9“死神”等昂贵高价值平台之间的空白。群体机器人（swarm robotics）的概念涉及多个自主机器人协作完成复杂任务，这在对抗环境中变得日益重要。这一战略转变的驱动力，源于近期冲突表明缓慢、昂贵的无人机在现代分层防空网络面前十分脆弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/military/us-low-cost-combat-drones-defenses">US to build low-cost combat drones that can overwhelm enemy defenses</a></li>
<li><a href="https://www.linkedin.com/posts/diux_our-massed-modular-aircraft-mma-solicitation-activity-7480346281639485440-5ApO">Our Massed Modular Aircraft ( MMA ) solicitation is now live.</a></li>
<li><a href="https://www.linkedin.com/top-content/technology/drone-technology-applications/use-cases-for-attritable-drone-systems-in-defense/">Use Cases for Attritable Drone Systems in Defense</a></li>

</ul>
</details>

**标签**: `#drones`, `#swarm-robotics`, `#defense-tech`, `#military-strategy`, `#unmanned-systems`

---

<a id="item-11"></a>
## [CISA 在密码泄露时临时制定响应预案](https://techcrunch.com/2026/07/10/us-cyber-agency-cisa-had-to-build-its-incident-playbook-during-the-incident-agency-reveals/) ⭐️ 7.0/10

美国网络安全和基础设施安全局（CISA）透露，在一名承包商员工将大量密码暴露于公共 GitHub 仓库后，该机构不得不临时制定其事件响应手册。这种临时应对发生在该机构积极试图遏制和补救这一严重安全漏洞的过程中。 这一事件凸显了美国国家网络安全机构内部严重的运营和安全失误，引发了外界对其应对重大漏洞准备情况以及第三方承包商相关风险的担忧。它强调了在政府和企业环境中建立强大的密钥管理和预先制定的事件响应协议的迫切需求。 这些暴露的密码是由 GitGuardian 的安全研究员发现并由独立记者 Brian Krebs 报道的。由于缺乏预先制定的手册，CISA 不得不在安全事件发生期间临时制定其遏制和补救步骤。

rss · TechCrunch · 7月11日 01:01

**背景**: 事件响应手册（Incident Response Playbook）是一份结构化的分步指南，概述了处理特定网络安全事件的确切程序、角色和通信协议。CISA 是负责提升美国国家网络安全态势的联邦机构，因此其内部安全实践备受审视。密钥管理（Secrets management）涉及安全地存储和控制对密码和 API 密钥等敏感数据的访问，以防止未经授权的暴露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.upwind.io/glossary/incident-response-playbooks">Incident Response Playbooks - Upwind</a></li>
<li><a href="https://www.xurrent.com/blog/incident-response-playbook">What Is an Incident Response Playbook and How Do You... | Xurrent</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#incident-response`, `#CISA`, `#secrets-management`, `#security-news`

---

<a id="item-12"></a>
## [OpenAI 安全主管 Johannes Heidecke 离职](https://www.wired.com/story/openai-head-of-safety-leaving/) ⭐️ 7.0/10

OpenAI 安全主管 Johannes Heidecke 即将离职，与此同时，该人工智能实验室正在进行重组，以进一步整合其研究和安全团队。 顶级安全领导者的离职凸显了 OpenAI 在如何优先考虑 AI 对齐和安全研究方面正在经历的持续结构和理念转变。这一举措可能会显著影响这家业内最具影响力的实验室未来 AI 治理和安全协议的发展方向。 Heidecke 的离职与 OpenAI 将其原本独立的研究和安全部门合并为更统一的运营结构的战略努力直接相关。这种整合表明该公司在平衡快速模型开发与安全评估的方式上发生了转变。

rss · Wired · 7月11日 01:07

**背景**: AI 安全和对齐是指旨在确保人工智能系统按照人类意图和价值观运行的研究与实践。从历史上看，像 OpenAI 这样的组织一直维持着独立的安全团队，以独立评估和减轻其核心研究模型的风险，尽管最近的行业趋势显示出向更集成化方法推进的势头。

**标签**: `#AI Safety`, `#OpenAI`, `#AI Governance`, `#Industry News`, `#Machine Learning`

---

<a id="item-13"></a>
## [“Slopsquatting”：一种由 AI 引发的新型软件供应链威胁](https://venturebeat.com/security/forget-typosquatting-slopsquatting-is-the-software-supply-chain-threat-created-by-ai-coding-tools) ⭐️ 7.0/10

安全研究人员发现了一种名为‘slopsquatting’的新型供应链攻击，网络犯罪分子利用 AI 编码助手的幻觉，诱骗开发者安装包含恶意软件的虚假软件包。与传统的 typosquatting 不同，这种方法依赖于 LLM 生成看似合理但不存在的包名，随后攻击者将其注册。 这一威胁从根本上改变了软件供应链的风险模型，因为 AI 幻觉创造了一个庞大且缺乏保护的恶意软件注入面，能够绕过传统的注册表防御机制。它对越来越多依赖 AI 助手的开发者构成了严重风险，可能会在无形中破坏无数的生产环境。 由于幻觉生成的包名并非流行库的简单拼写错误，现有的针对 typosquatting 的注册表保护机制无法大规模检测它们。研究表明，开源软件包中报告的漏洞正以每年 98%的速度增长，且其平均存在时间增加了 85%，凸显了安全态势的恶化。

rss · VentureBeat · 7月11日 16:00

**背景**: Typosquatting 是一种长期存在的欺骗手段，攻击者通过注册流行域名或包的拼写错误版本来欺骗用户。用于 AI 编码助手的 LLM 经常会出现幻觉，生成自信但完全虚构的信息，在这种情况下表现为编造听起来合理但实际上并不存在的软件包名。

**标签**: `#AI Security`, `#Software Supply Chain`, `#LLM Hallucinations`, `#Cybersecurity`, `#Developer Tools`

---

<a id="item-14"></a>
## [监管重组后腾讯将仅持有 AI 初创公司 Manus 少数股份](https://www.ithome.com/0/975/622.htm) ⭐️ 6.0/10

知情人士澄清，在监管主导的股权重组中，腾讯将仅持有 AI 初创公司 Manus 的少数股份，此次重组旨在填补 Meta 被禁投资留下的空缺。此前传闻腾讯将成为最大股东，但实际上是由社会资本共同补齐 Meta 的投资份额以促使其退出。 这一进展凸显了中国对外资投资国内 AI 企业的严格监管立场，以及防止企业通过离岸迁址进行“洗澡式出海”的努力。它强调了跨境运营的 AI 初创公司在融资和运营中面临的地缘政治复杂性与监管风险。 此次股权重组是由中国外商投资安全审查机制主导的，该机制此前已禁止了 Meta 对 Manus 的收购。尽管此前传闻估值达 20 亿美元且腾讯将成为最大股东，但股权变更完成后腾讯仍只是持有少数股份的外部股东。

rss · IT之家 · 7月11日 14:58

**背景**: Manus 是 2025 年初推出的一款 AI 代理平台，因其能够执行复杂任务和自动化工作流而迅速走红。然而，在将其总部迁至新加坡并停止国内运营后，该公司引发了强烈争议，促使中国监管部门介入并阻止其被外资收购，以防止企业规避国家安全审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://manus.im/">Manus : Hands On AI</a></li>
<li><a href="https://blog.csdn.net/xun527/article/details/146082116">【 Manus 】 AI 代理人正式上岗-附 Manus 邀请码限时通道_monica...</a></li>

</ul>
</details>

**标签**: `#AI-investment`, `#China-regulation`, `#Tencent`, `#geopolitics`, `#AI-startups`

---

<a id="item-15"></a>
## [欧几里得望远镜发现破纪录的古老类星体](https://www.ithome.com/0/975/593.htm) ⭐️ 6.0/10

欧洲航天局的欧几里得空间望远镜发现了 31 个古老类星体，其中两个以 7.77 和 7.69 的红移值打破了现有纪录，其光线可追溯至宇宙大爆炸后约 6.7 亿年。这一单次发现使该早期宇宙时期已知类星体的数量增加了一倍多。 这一突破极大地推进了我们对早期宇宙的理解，特别是再电离纪元期间首批超大质量黑洞和星系的形成过程。它还证明了与以往的观测相比，欧几里得望远镜在探测微弱、遥远天体方面具有前所未有的高效性。 打破纪录的两个类星体编号分别为 EUCL J172902.75+641018.1 和 EUCL J125308.55+705432.3，距离地球超过 130 亿光年，超越了 2021 年红移 7.64 的纪录。未来的研究计划利用詹姆斯·韦布空间望远镜和阿塔卡马大型毫米/亚毫米波阵列（ALMA）对红移超过 8 的类星体进行更深入的分析。

rss · IT之家 · 7月11日 13:24

**背景**: 类星体是由超大质量黑洞吸积物质提供能量的极亮活动星系核，是宇宙中最明亮的天体之一。红移值衡量天体光线因宇宙膨胀而被拉伸的程度；红移值越高，代表距离越远、光线越古老，使天文学家能够回溯更久远的过去。再电离纪元是指第一批恒星和星系电离早期宇宙中中性氢的时期，标志着宇宙“黑暗时代”的结束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20250703A079GA00">“ 欧 几 里 得 ” 空 间 望 远 镜 探测暗物质、暗能量的最新进展_腾讯新闻</a></li>
<li><a href="https://news.sciencenet.cn/htmlpaper/2025/8/2025822152421326138541.shtm">欢迎投票：2025全球十大工程成就评选 Engineering—论文—科学网</a></li>

</ul>
</details>

**标签**: `#astronomy`, `#space-exploration`, `#astrophysics`, `#scientific-discovery`, `#euclid-telescope`

---

<a id="item-16"></a>
## [AMD 发布 PEPS 技术：纹理参数减少 25%](https://www.ithome.com/0/975/580.htm) ⭐️ 6.0/10

AMD 在 2026 年 I3D 研讨会上推出了 PEPS（位置编码投影采样）这一新型神经纹理压缩技术。该方法通过将正弦和余弦投影视为李萨如曲线上的点进行采样，在保持画质不变的前提下将模型参数量减少了 25%。 这项创新应对了现代图形学中日益严峻的显存限制挑战，提供了一种使用显著更少内存来存储高质量纹理和 3D 形状的方法。随着硬件支持的成熟，它最终将惠及 3D 渲染、游戏开发以及依赖符号距离函数（SDF）的应用。 参数量的减少是以增加计算时间为代价的，在 RX 9070 XT 上渲染 1024x1024 纹理耗时 5.47 毫秒，而基准方案为 4.32 毫秒，不过优化版本将差距缩小至 4.86 毫秒。此外，在 SDF 应用中，该技术能将编码器参数减少至八分之一，同时保持几乎相同的交并比（IoU）得分。

rss · IT之家 · 7月11日 11:27

**背景**: 神经纹理压缩使用隐式神经表示（INR），通过多层感知机学习将连续的纹理坐标映射为信号值，从而替代传统的离散像素阵列。传统的位置编码将低维坐标映射到高维的正弦和余弦向量，而 PEPS 通过沿李萨如曲线对这些投影进行采样来改进这一过程，从而用更少的参数承载更多信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peterhuistyping.github.io/INR-Tex/">INR-Tex: Implicit Neural Representation of Textures</a></li>
<li><a href="https://openreview.net/pdf?id=qqIrESv4f_L">Signal Processing for Implicit Neural Representations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lissajous_curve">Lissajous curve - Wikipedia</a></li>

</ul>
</details>

**标签**: `#neural-texture-compression`, `#implicit-neural-representation`, `#computer-graphics`, `#AMD-research`, `#model-optimization`

---

<a id="item-17"></a>
## [Armada OS 让骁龙掌机变身 Steam Deck 运行 3A 游戏](https://www.ithome.com/0/975/539.htm) ⭐️ 6.0/10

基于 Fedora Bootc 开发的开源 Linux 发行版 Armada OS 发布了原型版本，可通过 FEX 转译和 CachyOS Proton 让骁龙安卓掌机运行 x86 PC 游戏。 该项目展示了基于 ARM 的掌机如何突破安卓生态限制以提供类似 PC 的游戏体验，有望为高性能移动游戏设备扩展更广阔的应用生态。 该系统支持骁龙 8 Gen 2、Gen 3 和 Elite 芯片，内置集成 Decky 的控制面板以支持针对单款游戏的 FEX 和 Proton 参数微调，但目前仍存在黑屏等 Bug，且因采用模拟挂起机制导致待机功耗较高。

rss · IT之家 · 7月11日 09:35

**背景**: Fedora Bootc 是一种利用容器镜像进行事务性就地操作系统更新的技术。FEX 是一个 x86 转译层，允许 ARM 设备运行 x86 应用程序，而 CachyOS Proton 则是 Steam 的兼容工具，在原有基础上增加了实验性功能和优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.fedoraproject.org/en-US/bootc/">Fedora /CentOS bootc Documentation :: Fedora Docs</a></li>
<li><a href="https://github.com/CachyOS/proton-cachyos">GitHub - CachyOS / proton - cachyos : Compatibility tool for Steam Play...</a></li>

</ul>
</details>

**标签**: `#Open Source`, `#Linux`, `#Emulation`, `#Gaming Handhelds`, `#ARM Architecture`

---

<a id="item-18"></a>
## [英伟达 RTX 50 显卡隐藏热点传感器被解锁，揭示严重局部过热问题](https://www.ithome.com/0/975/534.htm) ⭐️ 6.0/10

一位硬件爱好者成功逆向工程并解锁了英伟达 RTX 50 系列 GPU 上被隐藏的热点温度传感器，而英伟达此前通过移除 API 支持掩盖了这一功能。解锁后发现，虽然 GPU 平均温度正常显示在 70-80℃，但局部热点实际已超过 107℃。 这一发现表明，仅依赖 GPU 平均温度可能会掩盖因散热器接触不良导致的严重局部过热问题，从而引发意外的降频和长期的硬件损坏。这也暴露了英伟达在消费级 GPU 中通过软件层面禁用诊断功能，却保留底层硬件传感器的做法。 在解锁之前，由于英伟达移除了 API 支持而非物理传感器，GPU-Z 等监控工具显示的热点温度是代表无效值的 255℃（二进制 11111111）。解锁后，该爱好者发现通过重新涂抹硅脂解决接触不良问题，可将热点温度降至 100℃ 左右并恢复正常性能。

rss · IT之家 · 7月11日 09:11

**背景**: 热点温度是指分布在 GPU 芯片表面的多个温度传感器所报告的最高数值，通常比核心平均温度高出 10℃ 以上。监控这一指标对于诊断散热器安装不当或硅脂老化等物理散热问题至关重要，而平均温度读数无法检测到这些问题。英伟达的 RTX 50 系列基于全新的 Blackwell 架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/nvidia-gpu-hotspot-temperature-unlocked-by-mods-as-rtx-50-gpus-face-poor-thermal-issues/">NVIDIA GPU Hotspot Temperature Has Been Unlocked Through Mods...</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/nvidia-blackwell-architecture-deep-dive-a-closer-look-at-the-upgrades-coming-with-rtx-50-series-gpus">Nvidia Blackwell architecture deep dive: A closer... | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#GPU`, `#Hardware`, `#NVIDIA`, `#Reverse Engineering`, `#Thermal Management`

---

<a id="item-19"></a>
## [AI 对音乐版权及训练成本的影响](https://www.tmtpost.com/8061263.html) ⭐️ 6.0/10

文章探讨了 AI 技术给音乐产业带来的日益严峻的版权挑战，并特别质疑了究竟该由谁来承担 AI 模型训练和数据使用的财务与伦理成本。 这一问题至关重要，因为它触及了 AI 伦理和法律框架的核心，可能会重塑生成式 AI 时代知识产权的保护和补偿方式。 讨论的核心围绕“AI 炼化”或“洗歌”概念展开，即利用现有音乐训练 AI 模型以生成新曲目，这模糊了原创与未经授权的衍生作品之间的界限。

rss · 钛媒体 · 7月11日 10:09

**背景**: 生成式 AI 模型需要海量数据进行训练，通常会未经明确许可或未向原作者支付报酬就抓取受版权保护的音乐。“洗歌”是指利用 AI 模仿流行歌曲的风格或元素来创作衍生作品，从而逃避传统的版权检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.21jingji.com/article/20240830/herald/320c2c0e3f50c97cba5d373f90ff9717.html">洗 歌 再进化！ 音乐裁缝正在断送行业未来 - 21经济网</a></li>

</ul>
</details>

**标签**: `#AI`, `#Copyright`, `#Music Industry`, `#AIGC`, `#AI Ethics`

---

<a id="item-20"></a>
## [微软报告碳排放量激增 25%](https://www.wired.com/story/microsoft-25-percent-jump-in-carbon-emissions/) ⭐️ 6.0/10

微软报告其碳排放量激增了 25%，这主要是由于其快速扩张的数据中心基础设施产生了巨大的电力需求。这一激增凸显了支持云计算和人工智能工作负载所需的日益增长的能源消耗。 这一显著增长凸显了扩展人工智能和云基础设施所面临的环境与物理限制，对科技行业的可持续发展目标提出了挑战。它表明向人工智能驱动的计算转型将需要庞大的能源资源，这可能会与企业净零排放承诺相冲突。 这 25%的增长直接归因于为处理增加的计算工作负载而扩建的数据中心。尽管微软继续投资可再生能源，但新基础设施的庞大规模已经超出了其目前的碳减排和抵消策略。

rss · Wired · 7月10日 23:16

**背景**: 数据中心是云计算和人工智能的物理基础，需要消耗大量电力来运行服务器和冷却系统。随着各公司竞相构建和训练大型人工智能模型，这些设施的能源足迹呈指数级增长。因此，科技巨头在实现雄心勃勃的气候承诺的同时扩展计算能力，正面临越来越严格的审查。

**标签**: `#Data Centers`, `#Cloud Computing`, `#Green Computing`, `#AI Infrastructure`, `#Sustainability`

---

