# ISSUE #007: GEO (Generative Engine Optimization) Threat

**Priority:** High — 时效性极强（2026.3.15 CCTV 315晚会刚曝光3天）  
**Status:** Open  
**Assignee:** TBD  
**Estimated words:** 250 words (main block) + 50 words (governance patch) + 1 sentence (future directions patch)  
**Target merge locations:** §3.4, §4.1.3, §6.5  

---

## 1. Background & Motivation

2026年3月15日，央视315晚会曝光了"AI大模型投毒"灰产链：GEO（Generative Engine Optimization，生成式引擎优化）服务商通过批量生成虚假软文"投喂"AI大模型，操控AI搜索推荐结果。节目组虚构了一款"Apollo-9智能手环"，通过GEO系统发布虚假内容后，多个AI大模型在用户查询时将其推荐为"业界第一"。

GEO是SEO在AI时代的变异形态。学术上，Aggarwal et al. (KDD 2024) 已将其形式化，证明内容优化策略可将生成引擎中的来源可见度提升40%。后续研究（Kumar & Lakkaraju 2024, Wen et al. 2025）进一步揭示了GEO用于操纵LLM产品推荐的对抗性风险。

**为什么必须加入本文：**
- 投在中国机构主办刊物（JII），315晚会是极强的现实锚点
- GEO是全球性问题：Gartner预测传统搜索引擎访问量将下降25%，AI搜索成为主要信息入口
- 它是论文中三个已有主题的交叉点：content weaponization (§3.1) × information pollution (§3.4.3) × indirect manipulation (§3.3.3)
- 有KDD 2024等顶会学术支撑，不是纯新闻

---

## 2. Merge Plan (3个insertion points)

### Insertion A: §3.4 新增 subsubsection（主体，~250词）

**位置：** §3.4.3 "Information Ecosystem Degradation" 之后，作为 §3.4.4  
**标题：** `Generative Engine Optimization as an Emerging Threat`

### Insertion B: §4.1.3 China 子节追加一段（~50词）

**位置：** §4.1.3 "China" 子节中，TC260安全基本要求之后  
**形式：** 追加一个bullet point

### Insertion C: §6.5 追加一句（~20词）

**位置：** §6.5 "International Governance Harmonization" 末尾  
**形式：** 追加一句话

---

## 3. Terminology（写作时必须遵守）

| 术语 | 定义 | 使用规则 |
|------|------|----------|
| **GEO** (Generative Engine Optimization) | 优化网络内容以提升其在LLM生成回答中可见度的技术，类比传统搜索引擎的SEO | 首次出现给全称；区分"white-hat GEO"（合法内容优化）和"black-hat GEO"（伪造内容操纵AI输出）|
| **Generative engine** | 基于LLM的搜索/问答系统，通过RAG检索+生成来回答用户查询 | 如ChatGPT, Perplexity, DeepSeek等AI搜索产品 |
| **Inference-time manipulation** | 在模型推理时（而非训练时）通过操纵其访问的信息环境来影响输出 | 与data poisoning (§3.2) 的区别：GEO不改变模型参数，只改变模型检索到的内容 |

---

## 4. Cross-Reference Rules（防止与已有章节重复）

| 概念 | 已在哪里展开 | GEO段落中如何引用 |
|------|-------------|------------------|
| Data poisoning | §3.2 | "Unlike training-time data poisoning (§3.2), GEO operates at inference time..." |
| Indirect prompt injection | §3.3.3 | "GEO can be viewed as a commercialized form of indirect prompt injection (§3.3.3), where the motivation shifts from adversarial exploitation to profit-driven manipulation" |
| AI slop / information pollution | §3.4.3 | GEO段落紧接§3.4.3，自然承接；不重复定义AI slop |
| Liar's dividend | §3.4.3 | 引用但不重新解释："extending the authenticity crisis described above to AI-mediated commercial contexts" |
| China regulation | §4.1.3 | GEO治理内容直接追加在§4.1.3末尾 |

---

## 5. Content Spec: Insertion A（主体段落）

### 写作prompt（可直接复制给AI）

```
你是一位AI安全领域的综述论文作者。请撰写综述论文 "Security and Safety of AI-Generated Content" 中§3.4的一个新子节 "Generative Engine Optimization as an Emerging Threat"。

## 术语约定
- GEO = Generative Engine Optimization（生成式引擎优化）
- Security = 对抗外部恶意攻击
- Safety = 确保AI行为符合人类意图
- Generative engine = 基于LLM的搜索/问答系统（如ChatGPT, Perplexity, DeepSeek）

## 章节定位
本段是§3.4 "Misinformation, Disinformation, and Deepfakes" 的第四个子节。前三个子节分别讨论了deepfakes (§3.4.1)、AI驱动的信息操作 (§3.4.2)、信息生态退化 (§3.4.3)。本段聚焦GEO——一种商业化的AI输出操纵威胁。

叙事递进关系：deepfakes(伪造人) → 虚假信息(伪造事实) → 信息生态污染(AI slop) → GEO(商业化操纵AI输出)——从个体伪造升级到系统性信息生态操纵。

## 边界约束（严格遵守）
- 只讲威胁/问题，不讲防御方案
- 不讲政策法规（§4负责）
- 不重复解释data poisoning（引用§3.2）
- 不重复解释indirect prompt injection（引用§3.3）
- 不重复解释AI slop/model collapse（前一段§3.4.3已讲）

## 写作要求
- 英文，学术综述风格
- 约250词
- 引用标记：[ref: 简短描述]

## 必须覆盖的内容点

1. **定义与机制**（~60词）：
   - GEO是SEO在AI时代的对应物
   - 核心机制：批量生成AI偏好的结构化内容（结论前置、分点逻辑、引用权威来源），发布到高权重渠道，使生成引擎在RAG检索时优先抓取
   - 与data poisoning (§3.2) 的关键区别：GEO在推理时操纵模型访问的信息环境，而非在训练时篡改模型参数
   - 与indirect prompt injection (§3.3) 的关系：GEO可视为IPI的商业化变体，动机从对抗性利用转向逐利

2. **已验证的影响**（~60词）：
   - 学术证据：Aggarwal et al. (KDD 2024) 形式化GEO框架，证明优化策略可将来源可见度提升40% [ref: Aggarwal et al., KDD 2024]
   - 对抗性GEO：Kumar & Lakkaraju (2024) 证明可操纵LLM产品推荐 [ref: Kumar and Lakkaraju, 2024]
   - 315晚会实验：虚构产品"Apollo-9智能手环"通过GEO系统发布虚假内容后，被多个AI大模型推荐为顶级产品

3. **规模与产业化**（~60词）：
   - 中国GEO市场2024年规模超42亿元人民币，CAGR 38% [ref: 中国信通院, 2024]
   - 中国AI搜索月活用户超6亿 [ref: IDC, 2025]
   - 全球趋势：Gartner预测传统搜索引擎流量将下降25%，AI搜索成为主要信息入口
   - GEO已形成完整灰产链：从内容生成到分发到效果监测

4. **深层影响**（~70词）：
   - 信任侵蚀：用户信任LLM输出为"客观分析"，实际可能被商业内容注入塑造
   - 从deepfake的"眼见不为实"延伸到AI搜索的"AI说的不可信"
   - 公平性问题：LLM推荐位有限（如手机品牌仅5-10个位置），付费GEO将排挤合法但无力优化的中小企业
   - 与§3.4.3的model collapse形成双重打击：AI生成低质内容 + 人类为操纵AI生成的低质内容，共同污染信息生态

## 格式要求
- 不用bullet points，写成连贯的学术段落（2-3个段落）
- 段落之间有逻辑过渡
- 每段有明确主题句
```

---

## 6. Content Spec: Insertion B（治理补丁）

### 写作prompt

```
请用英文写一段约50词的内容，作为综述论文§4.1.3 "China"子节的追加段落。

上下文：前文已介绍了中国的《生成式AI服务管理暂行办法》、深度合成管理规定、算法备案制度、TC260安全基本要求。现在需要追加GEO相关的治理动向。

内容要点：
- 2026年315晚会曝光GEO灰产后，中国监管开始针对性响应
- 中国信通院启动《生成式引擎优化（GEO）可信基本要求》首轮评测
- 中国人工智能产业发展联盟（AIIA）发起GEO安全专项承诺，10家企业签署
- 2026年全国广告监管工作要点明确将AI生成广告列为重点整治对象
- 但GEO的法律定性仍处模糊地带

写成一个连贯的段落，不用bullet points。
引用标记：[ref: 描述]
```

---

## 7. Content Spec: Insertion C（未来方向补丁）

直接追加这一句（无需单独prompt）：

> The emergence of commercial manipulation ecosystems such as Generative Engine Optimization (GEO) further highlights the urgency of cross-border content integrity standards for AI-powered information retrieval systems.

---

## 8. Required References

| Cite Key | Full Reference | Used In |
|----------|---------------|---------|
| `geo` | Aggarwal, P., et al., "GEO: Generative Engine Optimization," KDD, 2024. | Insertion A |
| `geomanipulate` | Kumar, A. and Lakkaraju, H., "Manipulating Large Language Models to Increase Product Visibility," arXiv:2404.07981, 2024. | Insertion A |
| `georisks` | Wen, Y., et al., "Position: On the Risks of Generative Engine Optimization in the Era of LLMs," TechRxiv, 2025. | Insertion A |
| `egeo` | (Optional) "E-GEO: A Testbed for Generative Engine Optimization in E-Commerce," arXiv:2511.20867, 2025. | Insertion A |
| `315gala` | CCTV 315 Gala, "AI大模型遭投毒曝光," March 15, 2026. | Insertions A, B |

---

## 9. Merge Checklist（PR时逐项检查）

- [ ] Insertion A 放置在 §3.4.3 之后，编号为 §3.4.4
- [ ] §3.4 的 wordcount 标注从 `$\sim$800 words` 更新为 `$\sim$1,000 words`
- [ ] Insertion B 追加在 §4.1.3 的 TC260 条目之后
- [ ] Insertion C 追加在 §6.5 末尾
- [ ] 3条新引用加入 bibliography
- [ ] 术语表增加 GEO 条目
- [ ] 章节边界文档增加 GEO 交叉引用规则
- [ ] 全文搜索 "information ecosystem" 确认无重复定义
- [ ] 全文搜索 "SEO" 确认仅在 GEO 上下文中出现
- [ ] §3.4 的 Table 2 (Threat Taxonomy) 增加 GEO 行
