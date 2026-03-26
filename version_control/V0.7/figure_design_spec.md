# Figure Design Specification

---

## 文章背景

本文是一篇面向 Journal of Information and Intelligence (JII) 的综合性 survey，题为 *"Security and Safety of AI-Generated Content: A Comprehensive Survey from Content Risks to Agentic Exploitation"*。文章追踪 AIGC 安全从内容层面风险到自主 agent 级攻击的完整演化，覆盖 2022–2026 年的威胁、防御与治理。

**文章结构（5 sections）**：
- §1 Introduction
- §2 Capabilities & Threat-Relevant Properties（能力如何创造威胁）
- §3 Threat Landscape（四类威胁 + 攻击面演化阶梯）
- §4 Technical Countermeasures（检测、水印、对齐、agentic 防御）
- §5 Discussion and Outlook（研究议程、治理缺口、结论）

**文章核心贡献**：
1. 攻击面演化阶梯（Direct PI → Jailbreak → Indirect PI → Agentic → Multi-agent）
2. MCP 生态系统安全的系统梳理（首篇 survey 覆盖）
3. Temporal misalignment 元模式（部署→防御→治理的时间差加速）

**视觉体系目标**：4 张图覆盖文章的 4 个核心视觉需求——每张图对应一个读者必须"一眼理解"的概念，而非通读正文才能获取的信息。

---

## 4 张 Figure 的定位与目的

| Figure | 位置 | 目的 | 读者 30 秒内应获取的信息 |
|--------|------|------|------------------------|
| **Fig 1: Evolution Ladder** | §1 末尾 | 展示论文核心贡献——攻击面从 2022 到 2025 的逐级升级 | "攻击从简单的 prompt 注入一路升级到多 agent 级别的系统攻击，每一级在三个维度上都更严重" |
| **Fig 2: Threat Taxonomy** | §3 末尾 | 展示威胁分类的完整结构——读者定位"我关心的威胁在哪个分支" | "AIGC 威胁分为 4 大类 9 个子类，Adversarial Manipulation 分支是本文重点" |
| **Fig 3: Defense Layers** | §4 末尾 | 展示防御体系的分层架构和各层成熟度 | "防御从成熟的检测（顶）到新兴的 agent 安全（底），成熟度递减" |
| **Fig 4: Temporal Misalignment** | §5.5 | 可视化部署→防御→治理的时间差——论文的 meta-pattern | "MCP 发布后 14 个月才有治理框架，攻击在前、防御在中、治理在后" |

---

## 统一设计规范

### 配色体系
```
威胁/攻击：暖色系
  - Level 1 Direct PI:     #E8F5E9 边框 #4CAF50（绿，低威胁）
  - Level 2 Jailbreaking:  #FFF3E0 边框 #FF9800（橙）
  - Level 3 Indirect PI:   #FFEBEE 边框 #F44336（红）
  - Level 4 Agentic:       #F3E5F5 边框 #9C27B0（紫）
  - Level 5 Multi-agent:   #ECEFF1 边框 #455A64（深灰，emerging）

防御：冷色系
  - Detection:    #E3F2FD 边框 #2196F3
  - Watermarking: #E0F7FA 边框 #00BCD4
  - Alignment:    #E8EAF6 边框 #3F51B5
  - Agentic Sec:  #EDE7F6 边框 #673AB7

治理/政策：中性色
  - Governance:   #F5F5F5 边框 #9E9E9E

时间线事件类型：
  - Protocol/Deployment: #2196F3（蓝）
  - Attack/Vulnerability: #F44336（红）
  - Defense/Mitigation:   #4CAF50（绿）
  - Governance/Standard:  #FF9800（橙）
```

### 字体
- 标题: Inter Bold 或 system sans-serif bold, 16-18px
- 正文标签: Inter Regular, 11-13px
- 小注释: 10px, #666

### 尺寸
- 每张图宽度: 1400-1500px
- 高度: 根据内容自适应（400-800px）
- 最终输出: PDF（矢量）+ PNG（300dpi 位图备用）

---

## Figure 1：Attack Surface Evolution Ladder

### 替代原 Figure 1（论文结构图）
### 位置：§1 Introduction 末尾
### LaTeX label: `fig:evolution-ladder`

### 目的
这是全文最重要的 Figure。论文的核心贡献是"攻击面演化阶梯"，但该框架目前仅以 Table 2（5 行表格）呈现——读者无法直观感受"逐级升级"的递进关系。Figure 1 的目的是将这个框架从抽象表格转化为**一眼可感知的视觉阶梯**：每升一级，三个维度（攻击者接入、受害者自主度、影响范围）都在扩大。读者不需要读表格就能理解"越往上越危险"。

**替代论文结构图的理由**：原 Figure 1 是论文 5 个 section 的依赖关系图，读者看目录就能获得相同信息，信息密度近零。用核心贡献的可视化替代它，让 §1 的读者在第一页就看到本文的独特框架。

### 布局：左下→右上阶梯式

```
视觉结构（从下到上）：

                                    ┌──────────────────┐
                                    │  2025   │
                                    │  Multi-agent      │
                                    │  ▪ Inter-agent    │
                              ┌─────┤    trust exploit  │
                              │     └──────────────────┘
                              │  2024
                              │  Agentic Exploitation
                              │  ▪ Tool poisoning
                        ┌─────┤  ▪ EchoLeak, Cursor RCE
                        │     └────────────────────────┘
                        │  2023
                        │  Indirect PI
                        │  ▪ PoisonedRAG
                  ┌─────┤  ▪ Slack AI exfil.
                  │     └──────────────────────────────┘
                  │  2023
                  │  Jailbreaking
                  │  ▪ GCG, PAIR, Crescendo
            ┌─────┤
            │     └────────────────────────────────────┘
            │  2022
            │  Direct PI
            │  ▪ Goal hijacking, prompt leaking
            └──────────────────────────────────────────┘
```

### 每个台阶包含
1. **左上角**：年份标签（大号加粗，如 "2022"）
2. **标题**：攻击类名（加粗，如 "Direct Prompt Injection"）
3. **右侧**：三个水平进度条（短→长），分别代表：
   - 🔴 Attacker Access（红色系）
   - 🟡 Victim Agency（橙色系）
   - 🔵 Impact Scope（蓝色系）
   - 三条的长度从 Level 1 到 Level 5 递增，直观表达"每一级在三个维度上都更严重"
4. **底部小字**：2-3 个代表性攻击名称（灰色，italic）
5. **台阶间的向上箭头**：细箭头，无文字（Transition Trigger 已从表中删除，图中也不放）

### 背景色
- 每个台阶用对应 Level 的背景色（见配色体系）
- Level 5 台阶用实线边框（与其他级别一致），年份标注 "2025--" 表示仍在发展

### SVG / CSS 资源需求
- **无需外部 SVG asset**——纯 CSS 可实现
- 圆角矩形（`border-radius: 8px`）作为台阶
- CSS gradient 或纯色条作为三维度进度条
- CSS `transform: translateX/Y` 实现阶梯偏移
- 或用 CSS Grid / Flexbox 布局

### 关键设计约束
- 从左下到右上的视觉流向——读者视线自然"爬楼梯"
- Level 5 与 Level 1-4 视觉一致（实线边框），仅年份标注 "2025--" 表示持续发展中
- 三维度进度条是核心视觉元素——它把抽象的"三个 escalation axis"变成可视的"三条在增长的条"
- 整体宽高比 ~3:2（宽图，适合论文单栏或跨栏）

---

## Figure 2：AIGC Threat Taxonomy

### 位置：§3 末尾（Table 3 之前）
### LaTeX label: `fig:threat-taxonomy`

### 目的
§3 包含 4 大类 9 个子类的威胁，正文按顺序逐个展开，但读者在阅读过程中容易迷失于细节而丧失全局感。Figure 2 的目的是提供**一张完整的威胁地图**——读者可以在任何时候回看这张图确认"我现在读的这个威胁属于哪个分支"。同时，通过视觉高亮 Adversarial Manipulation 分支（★ 标记），引导读者注意本文的重点贡献区域。

**与 Figure 1 的关系**：Figure 1 展示攻击面的时间演化（纵向递进），Figure 2 展示威胁的分类结构（横向展开）。两者互补：演化阶梯是 Adversarial Manipulation 分支内部的深入分析。

### 布局：树形结构，根节点在左，分支向右展开

```
视觉结构：

AIGC Threat         ┬─ Content Weaponization ─┬─ Phishing & Malware (§3.1.1)
Landscape           │                         └─ NCII (§3.1.2)
(§3)                │
                    ├─ Model-Level Attacks ────┬─ Data Poisoning (§3.2.1)
                    │                          ├─ Backdoors (§3.2.2)
                    │                          └─ Supply Chain (§3.2.3)
                    │
                    ├─ Adversarial ────────────┬─ Direct PI (§3.3.1)
                    │  Manipulation            ├─ Jailbreaking (§3.3.2)
                    │  ★ Evolution Ladder      ├─ Indirect PI + Agentic (§3.3.3)
                    │                          └─ Attack-Defense Landscape (§3.3.4)
                    │
                    └─ Misinfo & Deepfakes ────┬─ Deepfakes (§3.4.1)
                                               └─ Info Operations (§3.4.2)
```

### 设计要点
1. **根节点**：灰色圆角矩形，"AIGC Threat Landscape"
2. **一级分支**（4 个 Category）：用对应颜色的圆角矩形
   - Content Weaponization: 暖黄 #FFF8E1
   - Model-Level Attacks: 浅红 #FFEBEE
   - Adversarial Manipulation: 浅紫 #F3E5F5（★ 标记为核心）
   - Misinfo & Deepfakes: 浅蓝 #E3F2FD
3. **二级叶节点**：小号圆角矩形，包含 §ref 编号
4. **Adversarial Manipulation 分支高亮**：边框加粗/加深，标注 "★ Evolution Ladder"
5. **连线**：实线，弯角连接（`border-radius` 或 SVG path）

### SVG / CSS 资源需求
- **无需外部 SVG asset**——纯 HTML div + CSS 连线
- 连线可用 CSS border-left + border-top 的组合实现 L 型拐角
- 或使用 SVG `<path>` 画贝塞尔曲线连线
- ★ 标记可用 emoji 或 SVG star icon

### 关键设计约束
- Adversarial Manipulation 分支必须视觉上最突出（加粗边框 + ★ 标记）
- 没有 §3.5 Ethical & Societal Risks 分支（已在 V0.5 删除）
- §ref 编号让读者可以直接跳转
- 宽高比 ~2:1（横向展开的树）

---

## Figure 3：Layered Defense Architecture

### 位置：§4.3.3 末尾
### LaTeX label: `fig:defense-layers`

### 目的
§4 涵盖检测、水印、对齐、adversarial defense、agentic security 五类防御技术，散布在多个 subsection 中。Figure 3 的目的是回答一个关键问题：**这些防御如何组合成一个完整的安全栈？** 通过自上而下的分层堆叠，读者一眼看到：(1) 防御有 4 层 + 1 个 cross-cutting 层；(2) 成熟度从上到下递减——检测已成熟，agentic 安全仍是新兴领域；(3) 每层包含哪些具体方案。这直接支撑论文的 defense-in-depth 论点。

**与 Figure 2 的关系**：Figure 2 是威胁侧的地图，Figure 3 是防御侧的地图。两者构成攻防对照。

### 布局：自上而下的分层堆叠，每层包含多个防御方法

```
视觉结构（从上到下，成熟度递减）：

┌─────────────────────────────────────────────────────────┐
│  Layer 1: Detection & Provenance          [Established] │
│  ┌──────────┐ ┌──────────┐ ┌─────────┐ ┌────────────┐  │
│  │DetectGPT │ │ UnivFD   │ │ASVspoof │ │ C2PA v2.2  │  │
│  │Binoculars│ │ DIRE     │ │         │ │ SynthID    │  │
│  └──────────┘ └──────────┘ └─────────┘ └────────────┘  │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Watermarking                    [Developing]  │
│  ┌──────────┐ ┌──────────┐ ┌───────────────────────┐   │
│  │ KGW      │ │Tree-Ring │ │ SynthID-Image (10B+)  │   │
│  │ SemStamp │ │ StegaStm │ │                       │   │
│  └──────────┘ └──────────┘ └───────────────────────┘   │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Alignment & Adversarial Defense [Developing]  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │ RLHF/DPO │ │ Circuit  │ │ Llama    │ │ SmoothLLM│  │
│  │ KTO/SimPO│ │ Breakers │ │ Guard    │ │ StruQ    │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
├─────────────────────────────────────────────────────────┤
│  Layer 4: Agentic Security                [Nascent]     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │ ETDI     │ │AgentSpec │ │Pro2Guard │ │ Progent  │  │
│  │ OAuth2.1 │ │          │ │          │ │          │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┤
│  Cross-cutting: Governance               [Fragmented]  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐               │
│  │ EU AI Act│ │ NIST RMF │ │ IMDA     │               │
│  └──────────┘ └──────────┘ └──────────┘               │
└─────────────────────────────────────────────────────────┘
```

### 每层设计
1. **层标题栏**：左侧层名（加粗），右侧 Maturity 标签（badge 样式）
2. **层内方法卡片**：小号圆角矩形，水平排列
3. **层间分隔**：实线（Layer 1-4），虚线（Layer 4 到 Governance）
4. **背景色渐变**：从上到下逐渐变浅，表达"成熟度递减"
   - Layer 1: #E3F2FD（深蓝底）
   - Layer 2: #E0F7FA（青底）
   - Layer 3: #E8EAF6（靛底）
   - Layer 4: #EDE7F6（浅紫底）
   - Governance: #F5F5F5（灰底，虚线边框）

### Maturity badge 颜色
- Established: #4CAF50 绿色 badge
- Developing: #FF9800 橙色 badge
- Nascent: #F44336 红色 badge
- Fragmented: #9E9E9E 灰色 badge

### SVG / CSS 资源需求
- **无需外部 SVG asset**
- CSS flexbox 布局每层内的方法卡片
- CSS background-color 渐变区分层级
- Badge 用 `display: inline-block; border-radius: 12px; padding: 2px 10px;` 实现
- 虚线用 `border-style: dashed`

### 关键设计约束
- 上下排列必须传达"从成熟到新兴"的递减关系
- Layer 4 (Agentic) 应该视觉上最突出（加粗边框或高亮色）——对应论文蓝海贡献
- Governance 虚线分隔——它是 cross-cutting 的，不属于技术防御栈
- 宽高比 ~4:3（偏方形，适合半页展示）

---

## Figure 4：Temporal Misalignment Timeline

### 位置：§5.5 Concluding Remarks（在 temporal misalignment 段落之后）
### LaTeX label: `fig:temporal-misalignment`
### 需要在 section5.tex 中新增 figure 引用

### 目的
Temporal misalignment 是论文在 §5.5 提出的 meta-pattern——"部署跑在前面，防御跟在后面，治理拖在最后"。但正文只用文字描述了 MCP 的 14 个月时间差，读者很难直觉感受这个滞后的严重性。Figure 4 的目的是**让时间差变成可视的空间差**：三条平行的时间轨道上，Capability 事件密集在左侧（2022-2024），Defense 事件集中在中部（2025），Governance 事件偏在右侧（2025末-2026）——三轨之间的水平偏移就是 temporal misalignment 的具象化。14-month gap 用红色弧线标注，成为全图的视觉焦点。

**与 Table 6 (MCP timeline) 的关系**：Table 6 提供精确的事件日期和 CVE 编号（查阅用），Figure 4 提供时间差的直觉感受（浏览用）。表格精确，图形直观，两者互补不冗余。

### 布局：三轨水平时间线

```
视觉结构：

时间轴 →  2022    2023    2024     2025              2026
          │       │       │        │                  │
─────── Capability ─────────────────────────────────────────
          │       │       │        │                  │
     ChatGPT  GPT-4   Claude    Claude Code GA     Codex
              Llama   Computer  Operator            (1.6M users)
                      Use       MCP launch
                                (Nov 2024)

─────── Defense ────────────────────────────────────────────
                                   │        │       │
                              OAuth 2.1  ETDI    MCPTox
                              (Mar 25)  (Jun 25) (Aug 25)
                                   │              │
                              Tool poison    Circuit
                              disclosed      Breakers
                              (Apr 25)

─────── Governance ─────────────────────────────────────────
                      │                           │    │
                  EU AI Act                   OWASP  IMDA
                  (Aug 24)                   Agentic  framework
                                             (Dec 25) (Jan 26)
                                                      │
                                                   NIST Agent
                                                   Standards
                                                   (Feb 26)

          ◄───── 14-month gap (MCP launch → IMDA) ─────►
```

### 设计要点

1. **三条水平轨道**（从上到下）：
   - **Capability** 轨：蓝色系 (#2196F3)
   - **Defense** 轨：绿色系 (#4CAF50)
   - **Governance** 轨：橙色系 (#FF9800)

2. **事件节点**：
   - 圆形节点（`border-radius: 50%`），颜色对应轨道
   - 节点下方/上方标注事件名称 + 日期
   - 关键事件（MCP launch, IMDA framework）节点更大

3. **时间差标注**：
   - MCP launch (2024-11) 到 IMDA (2026-01) 之间用红色虚线弧连接
   - 弧上标注 "14-month gap"
   - 这是全图的视觉焦点——temporal misalignment 的具象化

4. **事件密度可视化**：
   - Defense 轨在 2025 年 3-8 月密集出现事件（5 个月内 5 个事件）
   - Governance 轨在 2025-12 到 2026-02 才开始密集
   - 这种"密度差"自然展示滞后

5. **虚线连接**：
   - 同一主题的跨轨事件用灰色虚线连接
   - 如："MCP launch" (Capability) → "Tool poisoning" (Defense) → "OWASP Agentic" (Governance)

### SVG / CSS 资源需求
- **可能需要 SVG**：弧形连接线（CSS 不方便画弧）
- 圆形节点：CSS `border-radius: 50%` 即可
- 水平轨道线：CSS `border-top: 2px solid #color`
- 事件标签：HTML div 绝对定位
- 14-month gap 弧：SVG `<path>` 画弧线 + 文字

### 关键设计约束
- 水平方向必须等比例对应时间（2022-2026）
- 三轨之间有足够间距，不能挤在一起
- "14-month gap" 是视觉焦点——用红色/加粗/大字号
- Capability 轨密集在 2022-2024，Defense 密集在 2025，Governance 密集在 2025-2026——这个时间错位必须一眼可见
- 宽高比 ~3:1（宽扁时间线，适合论文全宽或跨栏）

---

## 资源需求总结

### 无需外部 SVG asset 的 Figure
| Figure | 技术栈 | 原因 |
|--------|--------|------|
| Figure 1 (Ladder) | 纯 HTML + CSS | 圆角矩形 + 渐变条 + 定位偏移 |
| Figure 2 (Taxonomy) | HTML + CSS（或 SVG 连线） | 树形连线可用 CSS border 或 SVG path |
| Figure 3 (Defense) | 纯 HTML + CSS | Flexbox 布局 + 背景色 |

### 可能需要 SVG 的 Figure
| Figure | 需要 SVG 的部分 | 原因 |
|--------|----------------|------|
| Figure 4 (Timeline) | 弧形连接线 + "14-month gap" 弧 | CSS 不方便画弧线 |

### 建议的 HTML 结构
所有 4 张图共享一个 CSS 文件（统一配色、字体、卡片样式），每张图一个独立 HTML 文件。用浏览器截图工具（如 Puppeteer 或手动截图）导出 PDF/PNG。
