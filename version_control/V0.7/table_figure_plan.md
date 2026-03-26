# V0.7 Table & Figure 改进计划

## Review 评估

这份视觉体系 review 的诊断部分（第一部分）质量高，尤其是：
- Figure 1 信息密度近零的判断完全正确
- 攻击面演化阶梯缺乏核心可视化的诊断准确
- MCP 时间线表的高价值判断正确（V0.7 已创建 Table 6）
- Table 间信息冗余的识别有效

**但建议部分存在过度工程问题**：
- 13 个视觉元素（9 Table + 4 Figure）对一篇 ~30 页的 survey 来说太多
- 按每个 table ~0.5-1 页、每个 figure ~0.5 页估算，13 个元素 = 8-10 页纯视觉，占全文 25-30%
- Table 3 (Jailbreak)、Table 8 (Agentic defense)、Table 9 (Open questions) 的内容在正文的 description list 和 enumerate 中已经结构化呈现，转表格是冗余
- Figure 4 (temporal misalignment) 与 Table 6 (MCP timeline) 功能重叠

---

## 采纳决策

### 采纳（高价值）

| # | 建议 | 理由 | 工作量 |
|---|------|------|--------|
| 1 | **Figure 1 替换**：删除论文结构图，改为攻击面演化阶梯可视化 | 诊断完全正确——结构图信息密度为零；核心贡献缺乏可视化是最大缺失 | 中（需生成新图） |
| 2 | **Figure 2 修复**：确认 §3.5 已不在图中 | V0.7 gen_fig2.py 已不含 §3.5，已确认 clean | 无（已解决） |
| 3 | **Table 6 (MCP timeline)**：V0.7 已创建 | 与 review 建议的 Table 4 一致 | 无（已完成） |

### 不采纳（过度工程）

| 建议 | 不采纳理由 |
|------|-----------|
| Table 3 (Jailbreak 对比) | §3.3.2 的 description list 已是结构化呈现，5 类 × 7 列的表太宽 |
| Table 8 (Agentic 防御) | §4.3.3 的 description list 已覆盖，新增表格信息冗余 |
| Table 9 (Open questions) | §5.1 的 enumerate 已是编号清单，转表格无增量价值 |
| Figure 4 (Temporal misalignment) | Table 6 (MCP timeline) 已可视化时序差——表格按时间排序，Type 列交替出现 Attack/Defense/Governance 已清晰展示滞后 |
| Table 1 增加 Defense Layer + Maturity 列 | Table 1 已精简为 4 列（Capability/Metric/Threat/§），加列会回到之前"太杂乱"的问题 |
| Table 5 增加 Source Type + Trend 列 | ↑↓→ 符号主观，Source Type 在方法论声明段已统一处理 |
| Table 6/7 扩展 (Detection/Watermark) | 当前 Table 4/5 的覆盖已足够，Audio/Video 各 1 行反映的是文献现状而非遗漏 |

### 保持现状

当前 V0.7 视觉元素清单：
- **6 Tables**: Table 1-5 (V0.6 继承) + Table 6 (MCP timeline, V0.7 新建)
- **3 Figures**: Figure 1 (需替换), Figure 2 (clean), Figure 3 (enhanced caption)

改进后：
- **6 Tables**: 不变
- **3 Figures**: Figure 1 替换为攻击面演化阶梯

总计 9 个视觉元素，对 30 页 survey 合理（~4-5 页视觉，15% 占比）。

---

## 执行计划

### 唯一需要做的新工作：Figure 1 替换

**删除**：当前的论文结构图（fig1_paper_structure.pdf/png）
**新建**：攻击面演化阶梯可视化（fig1_evolution_ladder.pdf/png）

设计要求（采纳 review 建议的阶梯式布局）：
1. 左下→右上的 5 级阶梯
2. 每级标注：年份、攻击类名、代表性攻击 1-2 个
3. 三个维度（Access/Agency/Impact）用颜色编码的进度条
4. 级间箭头标注 Transition Trigger
5. 配色与正文表格一致

**section1.tex 同步更新**：
- `\includegraphics{fig1_paper_structure.pdf}` → `\includegraphics{fig1_evolution_ladder.pdf}`
- caption 更新
- 删除 §1 P4 中的 "Figure~\ref{fig:structure} illustrates the paper's structure and logical dependencies"

**生成方式**：Python + Pillow（与 V0.3.5 fig2/fig3 相同的技术栈）

### 关键文件

| 文件 | 改动 |
|------|------|
| `V0.7/figure/fig1_evolution_ladder.{pdf,png}` | 新建 |
| `V0.7/figure/gen_fig1.py` | 新建 |
| `V0.7/paragraph/section1.tex` | 更新 figure 引用和 caption |
| `V0.7/figure/fig1_paper_structure.{pdf,png}` | 可删除或保留 |
