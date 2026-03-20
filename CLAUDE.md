# JII AIGC Security Survey

Survey paper targeting Journal of Information and Intelligence (JII).
Author: Zelin Zhang, Queen's University.

## What This Paper Is About

A comprehensive survey on "Security and Safety of AI-Generated Content," covering the full spectrum from content-level risks to autonomous agentic exploitation. The paper's original contributions are:
1. An attack surface evolution ladder: Direct PI → Jailbreak → Indirect PI → Agentic Exploitation
2. First AIGC survey to systematically cover MCP ecosystem security
3. Cross-disciplinary analysis (technology + policy + ethics)

## Current Phase: V0.2 Restructuring

**Active task:** Execute the restructuring plan at `version_control/V0.2/restructuring_plan.md`

Key changes from V0.1 to V0.2:
- Section 4 and 5 SWAPPED: §4 = Technical Countermeasures (was §5), §5 = Governance (was §4)
- Total word target: ~14,750 (from ~20,250)
- Blue ocean content (MCP, agentic exploitation, attack surface ladder) → PRESERVE or EXPAND
- Red ocean content (detection method details, watermark internals, policy specifics) → COMPRESS into tables

## Repository Map

```
guide/JII_AIGC.tex              ← Master outline (read this FIRST for any section work)
component/draft/                ← 15 raw deep-research drafts (C01–C15), the source material
component/prompts/              ← Research prompts + orchestration plan
version_control/V0.1/paragraph/ ← First draft: section1-6.tex (BASELINE, do not modify)
version_control/V0.1/reference/ ← Per-section bibtex + consolidated references_all.bib
version_control/V0.2/paragraph/ ← Restructured sections (OUTPUT goes here)
version_control/V0.2/reference/ ← Topic-split bib files (18 topics + aliases)
version_control/V0.2/restructuring_plan.md ← The detailed surgery plan
```

## Section Structure (V0.2)

| New § | Label | Content | Word Target | Source |
|-------|-------|---------|-------------|--------|
| 1 | sec:introduction | Introduction | ~1,300 | V0.1 section1 |
| 2 | sec:capabilities | Capabilities & Threat-Relevant Properties | ~2,800 | V0.1 section2 |
| 3 | sec:threats | Threat Landscape | ~3,600 | V0.1 section3 |
| 4 | sec:countermeasures | Technical Countermeasures | ~3,000 | V0.1 **section5** |
| 5 | sec:governance | Governance & Regulation | ~2,200 | V0.1 **section4** |
| 6 | sec:future | Future Research Directions | ~1,850 | V0.1 section6 |

## Writing Rules

- LaTeX: elsarticle document class, elsarticle-num-names bibliography
- Every \cite{} MUST resolve to a key in `V0.2/reference/*.bib`
- Cross-references: always use \ref{sec:label}, never hardcode "Section 4"
- References marked `TODO: verify` need manual checking — never remove the marker
- When compressing, move deleted method details into comparison tables (not lost, relocated)
- When a fact appears in multiple sections, keep ONE canonical location and cross-reference others

## Duplicate Content Policy (5 items to enforce)

| Content | Keep in | Elsewhere |
|---------|---------|-----------|
| Arup $25M deepfake fraud | §3.4.1 (full) | §1: one clause only; §2.1: delete |
| VALL-E 3-second cloning | §2.1 (first mention) | §2.3: "As established in §2.1"; §3.4.1: delete |
| 82.6% phishing AI-generated | §3.1.1 (with source) | §1: brief mention |
| MCP 10,000+ servers | §2.4.4 (first mention) | §5.2.4: cross-reference |
| OWASP prompt injection #1 | §3.3.4 (in attack-defense summary) | §2.4.5: delete |

## What NOT to Do

- Do not add new content not supported by the draft files in component/draft/
- Do not fabricate citations — use placeholder `\cite{TODO_find_ref}` if unsure
- Do not modify V0.1 files — they are the frozen baseline
- Do not compile LaTeX locally — final rendering is done in Overleaf
- Do not expand red-ocean sections (detection, watermarking, policy details)
- Do not use emoji in .tex files
