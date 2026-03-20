# Deep Research Orchestration Plan

## Survey: "Security and Safety of AI-Generated Content"

**Target Journal:** Journal of Information and Intelligence
**Total Components:** 15 deep research tasks
**Model Allocation:** Gemini ×5 | OpenAI ×4 | Claude ×6

---

## Component Overview

| # | File | Topic | Section | Model | Rationale |
|---|------|-------|---------|-------|-----------|
| 1 | `C01_content_generation_capabilities.md` | Security-Relevant Capabilities (Content Generation) | §2.1–2.3 | **Gemini** | Requires extensive real-time web search for latest model releases, user adoption data, market size, benchmark results |
| 2 | `C02_autonomy_agentic_capabilities.md` | Autonomy, Tool Use & Agentic Capabilities | §2.4 | **Claude** | MCP ecosystem originated from Anthropic; Claude has deepest understanding of agentic architecture and its security implications |
| 3 | `C03_content_weaponization.md` | Content Weaponization | §3.1 | **Gemini** | Needs broad web search for underground market models (WormGPT etc.), real-world fraud cases, crime statistics |
| 4 | `C04_model_level_attacks.md` | Model-Level Attacks | §3.2 | **OpenAI** | Classic ML security — data poisoning, backdoors, model extraction — requires structured academic literature retrieval from top venues |
| 5 | `C05_prompt_injection_jailbreak.md` | Prompt Injection & Jailbreak Taxonomy | §3.3.1–3.3.2 | **OpenAI** | Adversarial attack taxonomy demands precise academic paper tracking (GCG, AutoDAN, PAIR etc.) |
| 6 | `C06_ipi_agentic_exploitation.md` | Indirect Prompt Injection & Agentic Exploitation | §3.3.3–3.3.4 | **Claude** | IPI-to-agentic escalation is the paper's original contribution; requires deep understanding of MCP CVEs and agent security frontier |
| 7 | `C07_deepfakes.md` | Deepfakes | §3.4.1 | **Gemini** | Requires extensive case search — Hong Kong fraud, election deepfakes, statistics from Sensity/Sumsub reports |
| 8 | `C08_info_operations_ecosystem.md` | AI Info Operations & Ecosystem Degradation | §3.4.2–3.4.3 | **Gemini** | 2024 election year events, AI slop phenomenon, bot farm documentation — broad news and research retrieval |
| 9 | `C09_ethical_societal_risks.md` | Ethical and Societal Risks | §3.5 | **Claude** | Bias, psychological impact, copyright — requires nuanced multi-perspective ethical analysis |
| 10 | `C10_government_policies.md` | Government Policies & International Governance | §4.1 | **Gemini** | Policy/regulation retrieval — EU AI Act articles, US executive orders, China regulations — Gemini excels at official document search |
| 11 | `C11_industry_practices.md` | Industry Practices & Agentic Governance Gap | §4.2 | **Claude** | Synthesizing safety frameworks (FLI Index), platform governance, and MCP governance gap requires integrated judgment |
| 12 | `C12_aigc_detection.md` | AIGC Detection Methods | §5.1 | **OpenAI** | Dense academic content — detection methods, benchmarks, performance numbers — systematic literature retrieval |
| 13 | `C13_watermarking_provenance.md` | Watermarking & Content Provenance | §5.2 | **OpenAI** | Technical watermarking schemes (KGW, Tree-Ring, C2PA) — concentrated academic literature domain |
| 14 | `C14_alignment_defense_agentic_security.md` | Alignment, Adversarial Defense & Agentic Security | §5.3 | **Claude** | RLHF→DPO→Constitutional AI directly involves Anthropic's research lineage; agentic security is Claude's core domain |
| 15 | `C15_future_research_directions.md` | Future Research Directions | §6 | **Claude** | Forward-looking synthesis and gap identification requires deep reasoning and research-direction insight |

---

## Model Selection Rationale

The three deep research tools have largely comparable capabilities for academic survey tasks. The allocation above optimizes for marginal advantages:

- **Gemini (5 tasks):** Strongest at broad, real-time web retrieval — policy documents, news events, market data, incident reports, statistics from multiple sources.
- **OpenAI (4 tasks):** Strongest at structured academic literature search — ML security papers from top venues (IEEE S&P, USENIX, CCS, NeurIPS, ICML), benchmark results, technical method comparisons.
- **Claude (6 tasks):** Strongest at nuanced synthesis, ethical analysis, and domains where Anthropic has direct involvement (MCP, Constitutional AI, alignment, agentic security).

> **Note:** Swapping models between tasks will not cause catastrophic quality differences. The allocation is an optimization, not a hard constraint.

---

## Recommended Execution Order

### Phase 1 — Foundation (Components 1–2)
Capability analysis that grounds all subsequent threat/defense discussion.

### Phase 2 — Threat Landscape (Components 3–9)
Core taxonomy — the paper's primary academic contribution.

### Phase 3 — Governance (Components 10–11)
Policy and industry practices.

### Phase 4 — Technical Countermeasures (Components 12–14)
Detection, watermarking, alignment, and agentic security.

### Phase 5 — Synthesis (Component 15)
Future directions — best done after reviewing all Phase 1–4 materials.

### Phase 6 — Manual Writing
- **Section 1 (Introduction):** Write last, after all sections are complete.
- **Section 7 (Conclusions):** Write last, summarizing the four-fold contribution.

---

## Post-Processing Checklist

- [ ] **Reference verification:** Confirm every arXiv ID / DOI / URL actually exists
- [ ] **Deduplication:** Remove overlapping content across components
- [ ] **Cross-reference consistency:** Ensure all "as discussed in §X" pointers are accurate
- [ ] **Word count compression:** Trim from rich raw material to outline target word counts
- [ ] **Narrative smoothing:** Ensure logical flow between sections
- [ ] **Citation format:** Unify to elsarticle-num-names bibliography style
- [ ] **Figure/Table creation:** Produce the placeholder figures and tables
