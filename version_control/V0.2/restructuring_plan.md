# AIGC Survey 重构手术方案

## 一、现状诊断

### 各节当前字数估算（正文，不含表格/图）

| 章节 | 当前词数 | 大纲计划 | 超出比 |
|------|---------|---------|--------|
| §1 Introduction | ~1,200 | 1,200 | ✅ 合理 |
| §2 Capabilities | ~3,500 | 1,500 | ⚠️ 2.3× |
| §3 Threats | ~4,500 | 3,500 | ⚠️ 1.3× |
| §4 Governance | ~3,000 | 2,000 | ⚠️ 1.5× |
| §5 Countermeasures | ~4,200 | 3,050 | ⚠️ 1.4× |
| §6 Future | ~2,000 | 850 | ⚠️ 2.4× |
| **总计** | **~18,400** | **12,100** | **1.52×** |

加上参考文献（~200条 × ~3行 = ~5页）、表格（5个 ≈ 3页）、图（3个 ≈ 2页），
当前约 **50–55页**。

### 目标：压缩到 35–40 页（正文 ~14,000–15,000 词）

**需砍 ~4,000 词，同时对蓝海部分定向扩展 ~800 词**
→ 净删减目标：~3,200 词


---

## 二、核心战略：蓝海 vs 红海的精确识别

### 🔵 蓝海内容（扩展或保持）— 你的引用壁垒

| 内容 | 位置 | 竞品survey覆盖 | 行动 |
|------|------|---------------|------|
| 攻击面演进阶梯（PI→Jailbreak→IPI→Agentic） | §3.3 | ❌ 无人系统化 | **保持** |
| MCP 生态安全分析 | §2.4.4 + §3.3.3 | ❌ 2025年才出现 | **保持** |
| Agentic AI 治理空白 | §4.2.4 | ❌ 几乎无survey涉及 | **保持** |
| Agentic AI 安全防御 | §5.3.4 | ❌ 零散论文无系统综述 | **扩展 +300词** |
| Securing Autonomous Agents 未来方向 | §6.1 | ❌ 你可成为标准参考 | **扩展 +200词** |
| Reasoning models 安全影响 | §2.4.1 | ⚠️ 少量覆盖 | **保持** |
| Inverse scaling（能力越强越脆弱） | §2.4.4 + §3.3.3 | ❌ 关键洞察 | **保持** |

### 🔴 红海内容（大幅压缩）— 已有大量专门survey

| 内容 | 位置 | 竞品survey数量 | 行动 |
|------|------|---------------|------|
| 文本检测方法逐一介绍 | §5.1.1 | 20+ 篇专门survey | **砍50%** |
| 图像检测方法逐一介绍 | §5.1.2 | 15+ 篇专门survey | **砍50%** |
| 音视频检测方法 | §5.1.3 | 10+ 篇专门survey | **砍40%** |
| 文本水印方案细节 | §5.2.1 | 10+ 篇专门survey | **砍40%** |
| 图像水印方案细节 | §5.2.2 | 10+ 篇专门survey | **砍50%** |
| EU AI Act 条文细节 | §4.1.1 | 大量法学survey | **砍40%** |
| US 政策碎片化描述 | §4.1.2 | 大量政策survey | **砍35%** |
| China 监管框架细节 | §4.1.3 | 中文学术界已有大量 | **砍40%** |
| Deepfake 技术演进历史 | §3.4.1 | 50+ 篇deepfake survey | **砍50%** |
| Bias amplification 细节 | §3.5.1 | 大量公平性survey | **砍30%** |


---

## 三、逐节手术方案

### §1 Introduction（~1,200词 → 1,300词）+100

**修改1：P1 中 AIGC 定义扩展**
- 当前："any content—text, images, audio, video, or code—produced by generative AI systems"
- 改为：加入 "or **action**"，并用2–3句论证为何 action 属于 AIGC
- 论证逻辑：VLA 模型将 action token 化为与 language token 同构的生成对象；
  当 AIGC 的边界从 content 扩展到 action，安全威胁也从内容风险升级到 agentic exploitation
- 这为全文的演进叙事提供了**定义层面的逻辑基础**

**修改2：P3 贡献表述微调**
- 贡献2 更突出"attack surface evolution ladder"作为原创分类框架
- 贡献4 从"full-modality coverage"调整为"emphasis on agentic exploitation as the emerging frontier"


---

### §2 Capabilities（~3,500词 → 2,800词）−700

**§2.1 High-Fidelity（~500词 → 350词）−150**
- 删除：各模态的具体模型名罗列（GPT-4, Claude, Gemini... 在intro已出现过）
- 删除：Image段中关于DiT架构演进的技术描述（从GAN到LDM到DiT）
- 保留：每模态的"人类无法区分"的关键证据数字（53-61%等）
- 保留：安全含义总结句
- 方法：四个\paragraph各缩到3-4句，只保留security-relevant的证据

**§2.2 Low-Cost（~350词 → 280词）−70**
- 删除：Mac统一内存架构细节、RTX显卡型号等硬件规格
- 保留：三维度论证（开源、硬件、API价格）+ BEC成本计算
- 压缩为三句话各一维度 + 一段安全含义

**§2.3 Controllability（~400词 → 300词）−100**
- 删除：LoRA/ControlNet/IP-Adapter的技术原理描述（rank decomposition等）
- 保留：链式工具使用的攻击场景描述（LinkedIn照片→身份克隆）
- 保留：stylometric cloning的关键数字（82.7%→62%翻转）
- 保留：multi-channel attack场景

**§2.4 Autonomy and Tool Use（~2,250词 → 1,870词）−380**

- §2.4.1 Reasoning Models（~350词 → 250词）−100
  - 删除：CoT/self-consistency/ToT的技术描述（这是NLP基础知识）
  - 删除：GPQA Diamond的详细分数对比
  - 保留：o1→o3的能力跳跃（一句）、DeepSeek-R1（一句）、安全含义（一句）
  
- §2.4.2 AI Agents（~300词 → 250词）−50
  - 删除：Wang et al.的四模块定义（profile/memory/planning/action）
  - 删除：ReAct框架的详细描述
  - 保留：coding agents和browser agents的生产部署证据
  - 保留：SWE-bench从5%到70%的能力增长
  
- §2.4.3 Long Context（~250词 → 150词）−100
  - 删除：RoPE/YaRN/Ring Attention等技术细节
  - 删除：RULER和Lost in the Middle的实验细节
  - 压缩为：context从8K到10M的事实 + 对agentic系统的意义（一句）

- §2.4.4 MCP Ecosystem（~500词 → 保持500词）
  - 这是蓝海，不动

- §2.4.5 Security Implications（~350词 → 保持350词）
  - 这是核心论点，不动

- Table 1（保持）
  - 但考虑合并"Reasoning & planning"和"Long context windows"两行
    为一行"Advanced reasoning and extended context"，减少页面占用


---

### §3 Threats（~4,500词 → 3,600词）−900

**§3.1 Content Weaponization（~850词 → 650词）−200**

- §3.1.1 Malicious Content Generation
  - 删除：AI-phishing的冗余统计（保留2个最强数据点，删除TRAPD等）
  - 删除：LOLLM attacks细节描述
  - 删除：Forged documents段（法院案例、学术造假的细节在§3.4.2重复出现）
  - 保留：phishing统计（82.6%）、malware零检测率、weaponized LLMs underground市场

- §3.1.2 NCII（~250词 → 200词）−50
  - 保持大部分，只删Operation Cumberland细节

**§3.2 Model-Level Attacks（~700词 → 550词）−150**
- 删除：Data poisoning的数学公式化描述（$D_p$, $M_\theta = A(D \cup D_p)$）
- 删除：Backdoor triggers的逐类列举
- 删除：Model extraction的技术细节
- 保留：每种攻击的关键数字（250 documents、$60成本、$200移除安全训练）
- 方法：每段从4-5句压到2-3句，focus on "why dangerous" not "how works"

**§3.3 Adversarial Manipulation（~1,300词 → 保持1,300词）**
- 🔵 这是你的核心原创贡献，完全不动
- 四级演进阶梯 + MCP漏洞 + 攻防现状，每个字都有价值

**§3.4 Misinformation & Deepfakes（~750词 → 450词）−300**

- §3.4.1 Deepfakes（~300词 → 150词）−150
  - 删除：从GAN到diffusion的技术演进描述（"paradigm shift from GANs to diffusion..."）
  - 删除：EMO, LivePortrait等具体框架名
  - 删除：VALL-E技术细节（已在§2.1和§2.3中出现过两次）
  - 保留：Arup \$25M案例（一句）、Sumsub 2137%数字（一句）、攻防不对称结论（一句）
  - 注意：Arup案例在§1(P2)、§2.1(Video段)、§3.4.1已出现三次 → 只在§3.4.1保留完整版，§1和§2用简短引用

- §3.4.2 AI-Powered Information Operations（~300词 → 200词）−100
  - 删除：Spamouflage/DOPPELGANGER的具体操作描述
  - 保留：核心结论（AI disinformation更有效）+ election interference一句 + 学术造假一句

- §3.4.3 Information Ecosystem Degradation（~150词 → 100词）−50
  - 压缩为三个概念各一句：AI slop、model collapse、liar's dividend

**§3.5 Ethical Risks（~700词 → 550词）−150**

- §3.5.1 Bias（~350词 → 250词）−100
  - 删除：各modality的详细审计数据（Bloomberg/SDXL/PNAS/TTS逐一举例过多）
  - 保留：bias amplification的理论证明（Wang et al.）+ 2个最典型例子 + 评估benchmark列表

- §3.5.2 Psychological Impact（~150词 → 100词）−50
  - 删除：creator displacement anxiety细节
  - 保留：Character.ai事件 + 核心结论

- §3.5.3 Copyright（~200词 → 200词）保持
  - 已经很简洁

**Table 2（保持）**


---

### §4 Governance（~3,000词 → 2,200词）−800

**§4.1 Government Policies（~1,800词 → 1,100词）−700**

- §4.1.1 EU（~500词 → 300词）−200
  - 删除：Article 50的详细条文内容
  - 删除：Code of Practice两稿的演进细节（"first draft...second draft..."）
  - 删除：DSA和GDPR的细节段（DSA的45M用户阈值、CNIL/EDPB指导细节）
  - 保留：风险分级框架（一句）+ 关键义务（deepfake labeling, Aug 2025/2026日期）+ 处罚（一句）
  - 保留：GDPR对训练数据的影响（一句总结）

- §4.1.2 US（~450词 → 300词）−150
  - 删除：NIST框架的详细描述（AI RMF、600-1、IR 8596三个文件的分别介绍）
  - 删除：各州法律的逐一列举（TRAIGA细节、New York、DEFIANCE Act等）
  - 保留：EO14110→EO14179的政策反转（核心叙事）+ SB 53作为里程碑 + Take It Down Act
  - 保留：联邦 vs 州的碎片化结论

- §4.1.3 China（~350词 → 200词）−150
  - 删除：Deep Synthesis Provisions和Interim Measures的分别详述
  - 删除：TC260的31个具体安全风险分类
  - 保留：三层监管架构概述（一句）+ 算法备案制度（一句）+ 执法案例（一句）

- §4.1.4 International（~300词 → 200词）−100
  - 删除：UK AISI的详细评估结果
  - 保留：AI Safety Reports + Summit trajectory + G7/OECD（各一句）
  - 保留：三范式比较分析段（这是有价值的原创分析）

**§4.2 Industry Practices（~1,200词 → 1,100词）−100**

- §4.2.1 Safety Frameworks（保持）— 有FLI Safety Index等独特数据
- §4.2.2 Red teaming（~150词 → 100词）−50 — 精简
- §4.2.3 Platform Governance（~250词 → 200词）−50 — 删除X平台细节
- §4.2.4 Agentic AI Governance Gap（保持）— 🔵 蓝海核心内容

**Table 3（保持）**


---

### §5 Countermeasures（~4,200词 → 3,000词）−1,200

**§5.1 AIGC Detection（~1,200词 → 600词）−600** ⭐ 最大压缩区

- §5.1.1 Text Detection（~400词 → 200词）−200
  - 删除：DetectGPT/Fast-DetectGPT/Binoculars/DNA-GPT的逐一机制描述
  - 删除：GPTZero/Ghostbuster/RADAR的逐一描述
  - 替换为：2段综述式描述
    - P1: "Zero-shot methods exploit statistical properties of LM-generated text (DetectGPT [x], Binoculars [x]); trained classifiers fine-tune encoders on labeled pairs (GPTZero [x], RADAR [x]). See Table X for comparison."
    - P2: Challenges段保留，但压缩为4个bullet各一句
  - 关键策略：让Table 4承载方法对比的重量，正文只做导读

- §5.1.2 Image Detection（~300词 → 150词）−150
  - 删除：频域分析/CNN-ViT/GAN fingerprinting/DIRE的逐一描述
  - 替换为：一段概述 + 核心困境（ProGAN→diffusion的3.05%迁移失败 + JPEG robustness崩溃）

- §5.1.3 Audio & Video Detection（~250词 → 100词）−150
  - 压缩为一段：ASVSpoof + FaceForensics++ + Sora-class新挑战（各一句）

- §5.1.4 Cross-Modal Challenges（~200词 → 150词）−50
  - 保留大部分（这是你的分析，不是方法罗列）

- **新增/扩展 Table 4** 
  - 将所有被删掉的方法细节移入表格
  - 列：Modality | Paradigm | Representative Methods | Mechanism (1句) | Key Limitation

**§5.2 Watermarking（~1,000词 → 550词）−450**

- §5.2.1 Text Watermarking（~350词 → 200词）−150
  - 删除：KGW的green/red list机制描述
  - 删除：Unigram/Multi-bit/SemStamp的逐一描述
  - 删除：Distortion-free段的Christ/DiPmark/KTH细节
  - 保留：KGW基本思路（一句）+ 核心trade-off + SynthID部署 + 攻击面
  - 保留：impossibility result（Zhang et al.）——这与§6.3直接相连

- §5.2.2 Image Watermarking（~300词 → 150词）−150
  - 删除：Stable Signature/Tree-Ring/Gaussian Shading的技术原理
  - 删除：HiDDeN/StegaStamp的encoder-decoder细节
  - 替换为：diffusion-native vs encoder-decoder两范式（各一句）+ SynthID 10B部署 + robustness挑战

- §5.2.3 Content Provenance（~200词 → 150词）−50
  - 保留C2PA核心 + 限制（这与agentic trust chain有关联价值）

- §5.2.4 Challenges（保持 ~150词）

- **Table 5 扩展**承载被删方法细节

**§5.3 Alignment, Defense, Agentic Security（~2,000词 → 1,850词）−150 但内部重分配**

- §5.3.1 Alignment（~350词 → 250词）−100
  - 删除：DPO/IPO/SimPO/ORPO的逐一介绍
  - 删除：Pluralistic alignment的Sorensen et al.细节
  - 保留：RLHF→DPO演进线（一句）+ Constitutional AI（一句）+ 局限性（reward hacking, superficial alignment）

- §5.3.2 Defense Against Adversarial Manipulation（保持 ~500词）
  - 已经很好，每层防御一段，不需要改

- §5.3.3 Securing Agentic AI Systems（~500词 → 800词）+300 🔵 扩展
  - (a) Architecture-level: 增加 harness engineering 的安全维度（~80词）
    "The emerging discipline of harness engineering [OpenAI 2026] — designing 
    constraints, feedback loops, and lifecycle management around AI agents — 
    addresses reliability but intersects critically with security: its core 
    components (permission boundaries, human-in-the-loop gates, tool access 
    scoping) directly instantiate the defense principles above."
  - (b) MCP-specific: 增加 OAuth 2.1 → Resource Server的演进分析（~50词）
  - (c) Monitoring: 增加 agent behavior verification 的最新进展（AgentSpec, Pro2Guard）（~70词）
    这些内容目前在§6.1而不在§5.3，但作为已有方案应在countermeasures中先出现
  - (d) Open challenges: 增加 multi-agent trust chain的量化数据（~100词）
    1,700 candidate threats数据、lethal trifecta概念的展开


---

### §6 Future Directions（~2,000词 → 1,850词）−150

**§6.1 Securing Autonomous Agents（~400词 → 500词）+100**
- 增加：与harness engineering的关系——安全版harness作为研究方向
- 增加：从§5.3.3 open challenges自然过渡的unsolved问题

**§6.2 Unified Multi-Modal Detection（~250词 → 200词）−50**
- 适度压缩

**§6.3 Provably Robust Watermarking（~300词 → 200词）−100**
- 删除：Christ/Golowich/Zhao的逐一constructive results
- 保留：impossibility result + what remains unsolved

**§6.4 Privacy-Preserving Generation（~300词 → 250词）−50**
- 删除：TOFU benchmark细节

**§6.5 International Governance（~300词 → 250词）−50**
- 适度压缩

**§6.6 Dynamic Evaluation（~400词 → 300词）−100**
- 删除：LiveBench/HLE的详细机制
- 保留：核心gap + agentic evaluation benchmarks（与你的主题直接相关）


---

## 四、重构后的词数分配

| 章节 | 当前 | 目标 | 增减 | 占比 |
|------|------|------|------|------|
| §1 Introduction | 1,200 | 1,300 | +100 | 9% |
| §2 Capabilities | 3,500 | 2,800 | −700 | 19% |
| §3 Threats | 4,500 | 3,600 | −900 | 24% |
| §4 Governance | 3,000 | 2,200 | −800 | 15% |
| §5 Countermeasures | 4,200 | 3,000 | −1,200 | 20% |
| §6 Future | 2,000 | 1,850 | −150 | 13% |
| **总计** | **18,400** | **14,750** | **−3,650** | **100%** |

**预估总页数**：正文14,750词(~22页) + 表格5个(~3页) + 图3个(~2页) 
+ 参考文献~200条(~5页) = **~32–35页**
含abstract/title page = **~35–38页** ✅


---

## 五、重复内容清理清单

以下内容在多处出现，需要去重：

| 内容 | 出现位置 | 保留位置 | 其他处改为引用 |
|------|---------|---------|--------------|
| Arup \$25M deepfake fraud | §1 P2, §2.1 Video段, §3.4.1 | §3.4.1（完整版） | §1用一句引述, §2.1删除 |
| VALL-E 3秒克隆 | §2.1 Audio段, §2.3 Voice段, §3.4.1 | §2.1（首次出现） | §2.3改为"As established in §2.1", §3.4.1删除 |
| 82.6% phishing AI-generated | §1 P2, §3.1.1 | §3.1.1（带完整出处） | §1保留简述 |
| MCP 10,000+ servers | §2.4.4, §4.2.4 | §2.4.4（首次出现） | §4.2.4引用 |
| OWASP #1 ranking | §2.4.5, §3.3.4 | §3.3.4（在攻防总结中更自然） | §2.4.5删除 |
| FLI Safety Index D grade | §4.2.1 | 仅此处 | 无重复 |


---

## 六、优先级排序（建议执行顺序）

### Phase 1: 高收益压缩（砍掉红海细节，省时最多）
1. §5.1 Detection 方法描述 → 表格化（−600词，1小时）
2. §5.2 Watermarking 方案描述 → 表格化（−450词，1小时）
3. §4.1 Government Policies 条文细节删减（−700词，1小时）

### Phase 2: 内容去重
4. 清理上表中的5处重复内容（−200词，30分钟）
5. §3.4 Deepfakes 技术演进历史删减（−300词，30分钟）

### Phase 3: 蓝海扩展
6. §5.3.3 Agentic Security 扩展 + harness engineering（+300词，1小时）
7. §6.1 Securing Autonomous Agents 扩展（+100词，30分钟）
8. §1 P1 AIGC定义扩展（含action）（+100词，20分钟）

### Phase 4: 中等收益压缩
9. §2.1-2.3 Capabilities 传统模态压缩（−320词，1小时）
10. §2.4.1-2.4.3 Reasoning/Agents/Context 技术细节压缩（−250词，30分钟）
11. §3.2 Model-Level Attacks 压缩（−150词，30分钟）
12. §3.5 Ethics 压缩（−150词，30分钟）
13. §6.3-6.6 Future minor sections 压缩（−250词，30分钟）


---

## 七、关于标题

重构后论文的实际权重分布：
- Agentic 相关内容：§2.4(1,870) + §3.3(1,300) + §4.2.4(500) + §5.3.3(800) + §6.1(500) = **4,970词 = 34%**
- 传统AIGC内容：剩余 **9,780词 = 66%**

Agentic内容占1/3且是全文最密集、最原创的部分。标题推荐：

**Generative AI Security and Safety: A Comprehensive Survey from Content Risks to Agentic Exploitation**

这准确反映了重构后的内容重心。
