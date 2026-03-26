# Table & Figure 规划方案
## AIGC Security Survey 视觉体系重建

---

# 第一部分：现有视觉元素诊断

## 现有Table诊断

| 编号 | 内容 | 信息传达效率 | 核心问题 |
|------|------|-------------|---------|
| Table 1 | 能力→威胁映射（5行） | **中** | 行数太少，信息密度低；"Key Metric"列混杂了不同量纲的数据（百分比、价格、token数）；缺少"对应防御"列导致读者需要自行跨Section查找 |
| Table 2 | 攻击面演化阶梯（5行） | **中偏低** | 最关键的表却设计最弱——Year列暗示这是时间线而非分析框架；缺少"跃迁触发条件"列；三个维度的描述过于抽象（"Active instruction following"对Level 2-4区分度不够）；没有代表性攻击/CVE列使表格缺乏concrete anchoring |
| Table 3 | 威胁总结（9行） | **中偏高** | 结构清晰，但与Table 1有信息重叠（两张表都包含capability-threat映射）；"Key Metric"列的数据来源可靠性参差不齐但未标注 |
| Table 4 | 检测方法对比（7行） | **较高** | 现有表中设计最好的一张——维度清晰（Modality/Paradigm/Methods/Mechanism/Limitation）；但缺少2024-2025年的新方法；Audio和Video各只有一行，信息不足 |
| Table 5 | 水印方案对比（7行） | **较高** | 维度选择合理（Embedding Strategy/Capacity/Quality/Robustness）；但Robustness列用自然语言描述而非量化指标，可比性差 |

## 现有Figure诊断

| 编号 | 内容 | 信息传达效率 | 核心问题 |
|------|------|-------------|---------|
| Figure 1 | 论文结构图 | **很低** | 仅展示5个Section的依赖关系——任何读者看目录就能获得相同信息；占据半页篇幅但几乎无增量价值；在一篇40页的综述中，这张图是纯粹的篇幅浪费 |
| Figure 2 | AIGC威胁分类图 | **中** | 概念上很重要（是全文taxonomy的视觉锚点），但执行有问题：§3.5在正文中无对应章节；底部的攻击面演化阶梯arrow过于简单——这个本应是核心贡献的框架只获得了一条带4个dot的箭头；颜色编码不清晰 |
| Figure 3 | 分层防御架构 | **中偏高** | 概念设计合理（4层 × 多列的矩阵布局）；但"maturity"的评判标准未说明；Governance层标注为"Fragmented"但用了与其他层不同的视觉语言，不够统一 |

## 总体诊断

**核心问题：视觉元素没有形成体系。** 5张Table各自独立，没有统一的设计语言（有的用自然语言描述，有的用量化指标，有的混用两者）。3张Figure风格各异。最重要的是，**没有一张视觉元素直接展示文章声称的核心贡献——攻击面演化阶梯。** Table 2试图做这件事，但一个5行×5列的简单表格无法承载一个"四级递进分析框架"的复杂信息。

---

# 第二部分：视觉体系总体规划

## 设计原则

1. **每张Table/Figure必须有明确的"引用用途"**——后续研究者引用这张表/图时，他们在说什么？
2. **Table用于精确对比，Figure用于结构关系**——需要读者逐行比较具体数值的用Table；需要读者理解整体结构、流向、层级关系的用Figure
3. **信息自包含**——读者不需要阅读正文就能理解每张Table/Figure的核心信息（通过标题、列名、注脚完成）
4. **统一的视觉语言**——所有Table使用统一的列设计逻辑；所有Figure使用统一的配色和标注体系
5. **消除冗余**——任何一个数据点只在一张Table中出现

## 总体布局

| 编号 | 类型 | 位置 | 内容 | 引用用途 | 状态 |
|------|------|------|------|---------|------|
| Table 1 | Table | §2 | 能力-威胁-防御映射（升级版） | "AIGC capability-threat mapping, see [Table 1]" | **重设计** |
| Figure 1 | Figure | §2/§3之间 | 攻击面演化阶梯可视化（核心贡献图） | "The attack surface evolution framework [Fig. 1]" | **新建，替代原Figure 1** |
| Table 2 | Table | §3.3 | 攻击面演化阶梯详细规格（增强版） | "Attack escalation characteristics, see [Table 2]" | **重设计** |
| Figure 2 | Figure | §3 | AIGC威胁分类图（修复版） | "AIGC threat taxonomy [Fig. 2]" | **修复** |
| Table 3 | Table | §3.3 | Jailbreak攻击方法对比 | "Jailbreak mechanisms compared in [Table 3]" | **新建** |
| Table 4 | Table | §3.3 | MCP安全事件时间线 | "MCP security incidents [Table 4]" | **新建** |
| Table 5 | Table | §3 末尾 | 威胁态势总结（原Table 3的升级） | "Current AIGC threat landscape [Table 5]" | **重设计** |
| Table 6 | Table | §4.1 | 检测方法对比（原Table 4的扩展） | "AIGC detection methods [Table 6]" | **扩展** |
| Table 7 | Table | §4.2 | 水印方案对比（原Table 5的增强） | "Watermarking schemes compared in [Table 7]" | **增强** |
| Figure 3 | Figure | §4 | 分层防御架构（增强版） | "Layered defense architecture [Fig. 3]" | **增强** |
| Table 8 | Table | §4.3 | Agentic防御方法对比 | "Agentic AI defense landscape [Table 8]" | **新建** |
| Figure 4 | Figure | §5 | 时序错配可视化 | "Temporal misalignment pattern [Fig. 4]" | **新建** |
| Table 9 | Table | §5.1 | 开放研究问题结构化清单 | "Open research agenda [Table 9]" | **新建** |

总计：**9张Table + 4张Figure**（现有5+3=8个元素 → 13个元素，净增5个）

---

# 第三部分：每个视觉元素的详细设计

---

## Table 1（重设计）：能力-威胁-防御映射

### 引用用途
后续研究者引用："The mapping between generative AI capabilities and their security implications is summarized in [Table 1]."

### 设计目标
将现有Table 1从简单的5行映射扩展为一张**综合参照表**——读者一眼看到能力、威胁、现有防御、防御成熟度的完整链条。

### 列结构

| 列名 | 内容 | 数据类型 |
|------|------|---------|
| Capability | 能力类别 | 分类标签 |
| Key Metric | 代表性量化指标 | 数值+来源标注 |
| Primary Threats | 主要威胁类型 | 分类标签（链接到§3子节） |
| Representative Attack | 代表性攻击案例/方法 | 具体名称 |
| Defense Layer | 对应防御层 | 分类标签（链接到§4子节） |
| Maturity | 防御成熟度 | ●●●○○ 级别指示 |

### 行数：6-7行

### 关键设计决策
- **消除与原Table 3的重叠**：Table 1聚焦于"能力→威胁→防御"的水平链条；Table 5（原Table 3）聚焦于"威胁态势的量化总结"
- **Maturity列使用统一的符号系统**（●=成熟, ○=不成熟），与Figure 3的maturity评级保持一致
- **行业数据在Key Metric列用†标注**

---

## Figure 1（新建）：攻击面演化阶梯——核心贡献可视化

### 引用用途
后续研究者引用："The attack surface evolution from prompt injection to agentic exploitation follows a four-level escalation framework [Fig. 1]."

### 这是全文最重要的Figure——必须直观展示以下信息：
1. 四/五级攻击的递进关系
2. 每一级在三个维度（attacker access, victim agency, impact scope）上的位置
3. 级间跃迁的触发条件
4. 时间线（何时出现）
5. 代表性攻击案例

### 设计方案
采用**阶梯式上升布局**——左下到右上的阶梯，每一级是一个"台阶"。三个维度用颜色编码的条形图在每个台阶内部显示。台阶之间的连接箭头标注跃迁触发条件。

### 视觉结构
```
                                          ┌─────────────┐
                                          │  Level 5    │
                                          │ Multi-agent │
                                    ┌─────┴─────────────┘
                                    │  Level 4          │
                                    │ Agentic exploit   │
                              ┌─────┴───────────────────┘
                              │  Level 3                │
                              │ Indirect PI             │
                        ┌─────┴─────────────────────────┘
                        │  Level 2                      │
                        │ Jailbreaking                  │
                  ┌─────┴───────────────────────────────┘
                  │  Level 1                            │
                  │ Direct PI                           │
                  └─────────────────────────────────────┘
```

每个台阶内部包含：
- 三个小型水平条（A/V/I三维度），用长度表示等级
- 代表性攻击名称（小字）
- 时间标签（e.g., "2022"）

台阶间的向上箭头标注触发条件（e.g., "Instruction tuning普及", "RAG架构普及", "Tool-use framework + MCP"）

---

## Table 2（重设计）：攻击面演化阶梯详细规格

### 引用用途
后续研究者引用："The characteristics of each attack escalation level are detailed in [Table 2]."

### Figure 1展示结构关系，Table 2提供精确规格——两者互补。

### 列结构

| 列名 | 内容 | 说明 |
|------|------|------|
| Level | 级别编号+名称 | L1 Direct PI, L2 Jailbreaking, etc. |
| Year | 首次出现年份 | 保留 |
| Attacker Access | 攻击者接入要求 | 具体描述+等级标记(0-3) |
| Victim Agency | 受害者自主度 | 具体描述+等级标记(0-3) |
| Impact Scope | 影响范围 | 具体描述+等级标记(0-3) |
| Escalation Trigger | **新增**：跃迁触发条件 | 从上一级到本级的架构条件 |
| Representative Attacks | **新增**：代表性攻击 | 2-3个具体攻击名称/CVE |
| Peak ASR | **新增**：代表性攻击成功率 | 量化数据+来源 |

### 行数：5行（L1-L5）

### 关键改进
- **Escalation Trigger列**是最重要的新增——它回答"为什么攻击面会从一级演化到下一级"
- **Representative Attacks列**提供concrete anchoring
- **Peak ASR列**提供量化证据
- L1的Escalation Trigger标注"N/A (baseline)"

---

## Figure 2（修复）：AIGC威胁分类图

### 修复要点
1. **删除§3.5 "Ethical & Societal Risks"作为独立分支**——改为底部的cross-cutting bar
2. **强化攻击面演化阶梯的视觉权重**——底部的阶梯不应只是一条箭头，而应与Figure 1的设计语言呼应（简化版）
3. **统一配色**——每个分支用一个主色，与Table/正文标题对应
4. **每个叶节点增加对应Section编号**——方便读者跳转

---

## Table 3（新建）：Jailbreak攻击方法对比

### 引用用途
后续研究者引用："Jailbreak mechanisms and their effectiveness are compared in [Table 3]."

### 设计目标
将§3.3.2的五分类从prose转化为可一目了然的对比表。

### 列结构

| 列名 | 内容 |
|------|------|
| Category | 五大类别名称 |
| Mechanism | 一句话机制描述 |
| Representative Methods | 2-3个代表性方法 |
| Peak ASR | 最高报告ASR（来源标注） |
| Target Models | 主要测试模型 |
| Defense Robustness | 已知防御的有效性（一句话） |
| Cross-category? | 是否与其他类别重叠（标注具体重叠） |

### 行数：5行

### 关键设计决策
- **Cross-category列**直接回应"分类非互斥"的问题
- 不试图穷尽所有方法，每类只列2-3个代表性方法
- ASR数据标注来源（HarmBench/JailbreakBench/原论文）

---

## Table 4（新建）：MCP安全事件时间线

### 引用用途
后续研究者引用："The timeline of MCP security incidents and mitigations is documented in [Table 4]."

### 这是文章独有的高价值资产——目前没有其他综述系统整理过MCP安全事件。

### 列结构

| 列名 | 内容 |
|------|------|
| Date | 年/月 |
| Event | 事件名称 |
| Type | 分类（Vulnerability / Attack Research / Mitigation / Governance） |
| CVE/ID | CVE编号或论文标识 |
| CVSS | 评分（如适用） |
| Impact | 一句话影响描述 |
| Response | 对应的防御/修复措施（如有） |

### 行数：12-15行（覆盖2024.11 MCP发布 → 2026.02 NIST Initiative）

### 关键设计决策
- **Type列用颜色编码**：红色=漏洞，橙色=攻击研究，绿色=缓解措施，蓝色=治理
- 这张表直接支撑temporal misalignment论点——读者可以一眼看到漏洞出现的密集期和防御/治理响应的滞后
- 时间排序让"部署→漏洞→防御→治理"的时序模式自然浮现

---

## Table 5（重设计）：威胁态势量化总结

### 原Table 3的升级版

### 改进
- 增加**Data Source Quality列**：标注每个数据点的来源类型（Peer-reviewed / Industry report† / Government report）
- 增加**Trend列**：用↑↓→符号表示趋势方向
- 删除与Table 1重叠的capability映射信息
- 仅保留§3的量化威胁数据

### 列结构

| 列名 | 内容 |
|------|------|
| Threat Category | 威胁类别 |
| Specific Threat | 具体威胁 |
| Key Metric | 核心量化指标 |
| Source | 数据来源标注 |
| Source Type | Peer-reviewed / Industry† / Gov. report |
| Trend | ↑ 加剧 / → 稳定 / ↓ 缓解 |
| §Ref | 对应正文Section |

---

## Table 6（扩展）：检测方法对比

### 原Table 4的扩展

### 改进
- 增加2024-2025年新方法（Fast-DetectGPT、Ghostbuster等）
- Audio/Video各扩展到2行
- 增加**Cross-generator Robustness列**：这是检测领域最关键的性能维度
- 增加**Deployment Status列**：标注是否有production deployment

---

## Table 7（增强）：水印方案对比

### 原Table 5的增强

### 改进
- **Robustness列从自然语言改为量化指标**：统一用"survives X% of [attack type]"格式
- 增加**Spoofing Resistance列**：回应robustness-spoofing tradeoff
- 增加**Production Deployment列**：标注SynthID等实际部署

---

## Figure 3（增强）：分层防御架构

### 改进
- **增加maturity评判标准的图例**：在图底部用文字定义Established/Developing/Nascent/Fragmented
- **增加威胁→防御的映射连线**：从Figure 2的威胁类别到Figure 3的防御层之间用虚线连接（如果两图相邻）
- 或者替代方案：在Figure 3内部，每个防御框标注其对应的威胁类别（§3.x）

---

## Table 8（新建）：Agentic防御方法对比

### 引用用途
后续研究者引用："Defenses for agentic AI systems are compared in [Table 8]."

### 列结构

| 列名 | 内容 |
|------|------|
| Defense | 防御名称 |
| Category | 类别（Architecture / Protocol / Runtime / Monitoring） |
| Mechanism | 一句话机制描述 |
| Target Threat | 针对的攻击类型 |
| Effectiveness | 有效性数据 |
| Limitation | 一句话局限性 |
| Deployment | 研究/原型/生产 |

### 行数：8-10行

---

## Figure 4（新建）：时序错配可视化

### 引用用途
后续研究者引用："The temporal misalignment between capability deployment and governance response is illustrated in [Fig. 4]."

### 设计方案
**双轴时间线图**——横轴为时间（2022→2026），三条平行的水平时间线分别代表Capability Deployment（顶）、Defense Response（中）、Governance Response（底）。关键事件标注在对应时间线上。相同主题的事件之间用虚线连接（如"MCP发布" → "Tool poisoning研究" → "ETDI提出" → "IMDA框架"），使时间差可视化。

---

## Table 9（新建）：开放研究问题结构化清单

### 引用用途
后续研究者引用："Key open research questions in AIGC security are summarized in [Table 9]."

### 这张表直接面向后续研究者——他们可以据此identify自己的研究贡献对应哪个open problem。

### 列结构

| 列名 | 内容 |
|------|------|
| # | 编号 |
| Research Question | 具体研究问题 |
| Current State | 目前的最佳结果/进展 |
| Key Gap | 核心未解决点 |
| Required Breakthrough | 需要的突破类型 |
| §Ref | 对应正文Section |

### 行数：6-8行

---

# 第四部分：视觉元素间的交叉引用体系

## 表间引用链

```
Table 1（能力-威胁-防御映射）
  ├── "Primary Threats"列 → Table 5（威胁态势量化）
  ├── "Defense Layer"列 → Table 8（Agentic防御）/ Figure 3（分层防御）
  └── "Representative Attack"列 → Table 3（Jailbreak对比）/ Table 4（MCP时间线）

Table 2（攻击面阶梯规格）
  ├── 与Figure 1互补（Figure展示结构，Table提供精确规格）
  ├── "Representative Attacks"列 → Table 3 / Table 4
  └── "Peak ASR"列 → Table 5中的对应数据

Table 4（MCP时间线）
  ├── 直接支撑Figure 4（时序错配可视化）
  └── Type颜色编码与Figure 4的三条时间线对应

Table 9（开放问题）
  └── "Current State"列引用Table 5/6/7/8中的最佳已知结果
```

## Figure间的视觉统一

- **颜色体系**：威胁相关用暖色系（coral/amber/red），防御相关用冷色系（blue/teal/green），治理相关用中性色（purple/gray）
- **Figure 1和Figure 2共享攻击面阶梯的视觉语言**——Figure 2底部的阶梯是Figure 1的缩略版
- **Figure 3和Figure 4共享时间/成熟度维度**——Figure 3的maturity评级与Figure 4的时间线对应

---

# 第五部分：关键设计决策总结

## 删除/替代决策

| 现有元素 | 决策 | 理由 |
|---------|------|------|
| 原Figure 1（论文结构图） | **删除，替换为攻击面演化Figure** | 信息密度近零，占位浪费 |
| 原Table 1-3之间的重叠 | **Table 1聚焦映射链，Table 5聚焦量化态势** | 消除信息冗余 |
| Figure 2的§3.5分支 | **改为cross-cutting bar** | 正文无对应章节 |

## 新增决策

| 新元素 | 优先级 | 理由 |
|--------|--------|------|
| Figure 1（攻击面演化阶梯） | **P0** | 核心贡献缺乏可视化是最大的缺失 |
| Table 4（MCP安全时间线） | **P0** | 文章独有的高价值资产，无其他文献覆盖 |
| Figure 4（时序错配可视化） | **P1** | 直接支撑temporal misalignment论点 |
| Table 3（Jailbreak对比） | **P1** | 将五分类从prose转为可引用表格 |
| Table 8（Agentic防御对比） | **P1** | §4.3.3的核心内容目前无表格支撑 |
| Table 9（开放研究问题） | **P2** | 提升§5的引用价值 |

## 总体效果预期

修改前：5 Table + 3 Figure = 8个视觉元素，缺乏体系性
修改后：9 Table + 4 Figure = 13个视觉元素，形成完整的视觉信息体系

每个Section至少有一个视觉锚点。核心贡献（攻击面演化阶梯）获得Table + Figure双重支撑。所有量化数据集中在Table中，所有结构关系集中在Figure中，两类元素互补而不重叠。
