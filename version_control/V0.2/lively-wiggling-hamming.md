# V0.2 重构计划：Section 4/5 对换 + 蓝海/红海压缩

## Context

用户要求根据 `restructuring_plan.md` 对 AIGC 安全综述进行 V0.2 重构。核心改动：
1. **Section 4 (Governance) 与 Section 5 (Countermeasures) 对换**，获得 "威胁→技术对策→治理" 的叙事连续性
2. 按蓝海/红海策略压缩（目标：~20,250 → ~14,750 词）
3. 去除重复内容（Arup案例、VALL-E、MCP服务器数等5处重复）

## 新结构

```
§1 Introduction          (~1,300 词)  ← 从 ~1,850 压缩 + AIGC定义扩展
§2 Capabilities           (~2,800 词)  ← 从 ~3,400 压缩传统模态
§3 Threats                (~3,600 词)  ← 从 ~4,600 压缩红海
§4 Technical Countermeasures (~3,000 词) ← 原 §5，压缩检测/水印，扩展Agent安全
§5 Governance & Regulation  (~2,200 词) ← 原 §4，压缩政策细节
§6 Future Directions       (~1,850 词)  ← 从 ~2,400 压缩 + 扩展Agent方向
```

## 执行步骤（6个文件，按依赖顺序）

### Step 1: `V0.2/paragraph/section4.tex` ← V0.1 `section5.tex`
- **来源**: V0.1/paragraph/section5.tex (Countermeasures, ~4,800词)
- **目标**: ~3,000词 (净减 -1,800)
- **改动**:
  - Header 注释改为 "Section 4"
  - `\label{sec:countermeasures}` 保持不变（LaTeX自动解析）
  - §4.1 Detection: 删除逐方法描述（DetectGPT/Binoculars/DIRE等），替换为2段概述式，细节移入新Table 4 (-600词)
  - §4.2 Watermarking: 删除KGW机制/Stable Signature原理等，保留范式+部署+挑战 (-450词)
  - §4.3.1 Alignment: 删除DPO/IPO/SimPO逐一介绍，保留RLHF→DPO线+局限 (-100词)
  - §4.3.2 Defense: 保持（已well-structured）
  - **§4.3.3 Agentic Security: 扩展 +300词**（harness engineering、OAuth演进、AgentSpec/Pro2Guard、1700威胁数据）
  - 新增/扩展 Table 4 (Detection) 和 Table 5 (Watermarking)

### Step 2: `V0.2/paragraph/section5.tex` ← V0.1 `section4.tex`
- **来源**: V0.1/paragraph/section4.tex (Governance, ~3,200词)
- **目标**: ~2,200词 (净减 -1,000)
- **改动**:
  - Header 注释改为 "Section 5"
  - 开头 "deferred to Section countermeasures" → "covered in Section countermeasures"
  - §5.1.1 EU: 删除Art.50条文、Code of Practice两稿演进、DSA/GDPR细节 (-200词)
  - §5.1.2 US: 删除NIST三文件分别介绍、各州法律逐一列举 (-150词)
  - §5.1.3 China: 删除Deep Synthesis/Interim Measures分述、TC260 31风险分类 (-150词)
  - §5.1.4 International: 删除UK AISI评估细节 (-100词)
  - §5.2 Industry: 轻微压缩红队/平台(-100词)，Agentic治理缺口保持
  - MCP "10,000+ servers" 改为引用 Section 2.4.4

### Step 3: `V0.2/paragraph/section3.tex` ← V0.1 `section3.tex`
- **来源**: ~4,600词 → **目标**: ~3,600词 (-1,000词)
- **改动**:
  - 开头交叉引用修正："reserved for" → "presented in"
  - §3.1: 删TRAPD/LOLLM/Forged documents细节 (-200词)
  - §3.2: 删数学公式、trigger逐类、extraction细节 (-150词)
  - **§3.3: 完全保持**（蓝海核心，~1,300词不动）
  - §3.4.1 Deepfake: 删GAN→diffusion技术史、EMO/LivePortrait/VALL-E重复 (-150词)
  - §3.4.2-3: 删Spamouflage/DOPPELGANGER操作细节 (-150词)
  - §3.5: 删per-modality审计数据、creator displacement (-150词)
  - 重复清理: OWASP #1 仅留此处§3.3.4

### Step 4: `V0.2/paragraph/section1.tex` ← V0.1 `section1.tex`
- **来源**: ~1,850词 → **目标**: ~1,300词
- **改动**:
  - P1: AIGC定义扩展加入 "or action"，论证VLA模型+agentic边界 (+100词)
  - P2: Arup案例简化为一句（完整版在§3.4.1）
  - P3: 贡献2突出 "attack surface evolution ladder"；贡献4改为 "agentic exploitation frontier"
  - P4: **重写**组织段落，反映新顺序 Threats→Countermeasures→Governance
  - **Figure 1**: 更新流程图为 §2→§3→§4→§5→§6

### Step 5: `V0.2/paragraph/section2.tex` ← V0.1 `section2.tex`
- **来源**: ~3,400词 → **目标**: ~2,800词 (-600词)
- **改动**:
  - §2.1: 删模型名罗列/DiT架构史，每段缩到3-4句 (-150词)
  - §2.2: 删Mac/RTX硬件规格 (-70词)
  - §2.3: 删LoRA/ControlNet技术原理 (-100词)
  - §2.4.1: 删CoT/self-consistency/ToT、GPQA分数比较 (-100词)
  - §2.4.2: 删Wang四模块、ReAct框架描述 (-50词)
  - §2.4.3: 删RoPE/YaRN/Ring Attention/RULER/Lost in Middle (-100词)
  - §2.4.4 MCP: 保持（蓝海）
  - §2.4.5: 保持，但删OWASP #1（移至§3.3.4）
  - 重复清理: Arup从Video段删除，VALL-E保留首次出现
  - Table 1: 合并 "Reasoning" 和 "Long context" 为一行

### Step 6: `V0.2/paragraph/section6.tex` ← V0.1 `section6.tex`
- **来源**: ~2,400词 → **目标**: ~1,850词 (-550净)
- **改动**:
  - **§6.1 Securing Agents: 扩展 +200词**（harness engineering方向、从§4.3.3 open challenges自然延伸）
  - §6.2: 轻压 (-50词)
  - §6.3: 删Christ/Golowich/Zhao constructive results (-100词)
  - §6.4: 删TOFU benchmark细节 (-50词)
  - §6.5: 轻压 (-50词)
  - §6.6: 删LiveBench/HLE机制，保留agentic evaluation (-100词)

## 交叉引用审查清单

完成后需验证：
- [ ] `\ref{sec:countermeasures}` 解析为 §4（出现在 section1, section3, section5）
- [ ] `\ref{sec:governance}` 解析为 §5（出现在 section1, section3）
- [ ] 无硬编码 "Section 4" / "Section 5" 文字（全部用 `\ref{}`）
- [ ] Figure 1 流程图反映新顺序
- [ ] 5处重复内容已去重

## 关键文件路径

- 输入: `/home/zelin-zhang/Downloads/JII/version_control/V0.1/paragraph/section[1-6].tex`
- 输出: `/home/zelin-zhang/Downloads/JII/version_control/V0.2/paragraph/section[1-6].tex`
- 规划: `/home/zelin-zhang/Downloads/JII/version_control/V0.2/restructuring_plan.md`
- 引用: `/home/zelin-zhang/Downloads/JII/version_control/V0.2/reference/*.bib`

## 验证

1. 每个文件写完后统计词数，确认接近目标
2. 提取所有 `\cite{}` key 验证在 V0.2 bib 中存在
3. 检查所有 `\ref{}` 标签在6个文件中都有对应 `\label{}`
4. 完成后 git commit 到 GitHub
