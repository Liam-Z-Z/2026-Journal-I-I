# JII AIGC Security Survey — Project Context

## Project
- Survey paper: "Security and Safety of AI-Generated Content"
- Target journal: Journal of Information and Intelligence (JII)
- Author: Zelin Zhang, Queen's University

## Repository Structure
- `guide/JII_AIGC.tex` — Master outline with section targets and writing notes
- `component/draft/` — 15 deep research drafts (C01-C15)
- `component/prompts/` — Research task prompts + orchestration plan
- `version_control/V0.1/` — First draft (section1-6.tex + per-section bibtex)
- `version_control/V0.2/` — Restructured version (§4/§5 swapped, compressed)

## Current Status
- V0.1: All 6 sections drafted, references consolidated (822 entries)
- V0.2: Restructuring in progress — §4↔§5 swap + blue ocean/red ocean compression
- Next: Execute restructuring plan at `version_control/V0.2/restructuring_plan.md`

## Writing Standards
- elsarticle document class, elsarticle-num-names bibliography style
- Every \cite{} must resolve to an entry in V0.2/reference/*.bib
- All reference entries marked TODO: verify need manual checking
- Blue ocean content (MCP security, agentic exploitation, attack surface ladder): PRESERVE
- Red ocean content (detection methods, watermarking details, policy specifics): COMPRESS

## Build
- No local LaTeX compilation — final assembly done in Overleaf
- Reference verification: check arXiv IDs manually before submission

## Key Decisions
- §4 = Technical Countermeasures (was §5 in V0.1)
- §5 = Governance & Regulation (was §4 in V0.1)
- Target: ~14,750 words total, 35-38 pages
