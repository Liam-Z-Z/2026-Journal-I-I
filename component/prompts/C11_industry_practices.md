# Component 11 — Industry Practices & Agentic Governance Gap

- **Section:** §4.2
- **Model:** Claude
- **Topic:** Industry Practices and Agentic AI Governance Gap

---

## Prompt

You are helping me write a section of an academic survey on "Security and Safety of AI-Generated Content." This section (Section 4.2) covers industry self-regulation, platform governance, and the governance gap for agentic AI. Focus on institutional practices and standards — no deep technical implementation details.

Please produce a comprehensive research document covering:

**1. MODEL PROVIDER SAFETY FRAMEWORKS**

- Frontier AI Safety Frameworks: document that 12+ companies published or updated frameworks in 2025. List the major ones (Anthropic RSP, OpenAI Preparedness Framework, Google DeepMind Frontier Safety Framework, Meta, xAI, etc.) and summarize their key commitments.
- FLI (Future of Life Institute) AI Safety Index 2025:
  - Overall findings: Anthropic ranked #1, OpenAI #2.
  - The striking finding: no company scored above D in "Existential Safety."
  - What criteria were evaluated and methodology.
- Red teaming practices:
  - Human red teaming: how frontier labs organize red team exercises.
  - Automated red teaming: tools and approaches (e.g., Anthropic's automated red teaming, Microsoft PyRIT).
  - External red teaming programs and bug bounties.
- Acceptable Use Policies (AUPs): compare policies across major providers — what is prohibited, enforcement mechanisms.
- Model Cards / System Cards: their role in transparency, what they disclose, limitations of self-reporting.

**2. PLATFORM GOVERNANCE AND STANDARDS**

- Major platform AI content policies:
  - Meta: AI-generated content labeling, "Imagined with AI" labels, deepfake policies.
  - Google/YouTube: SynthID deployment, content policies.
  - TikTok: AI-generated content disclosure requirements.
  - X (Twitter): Community Notes approach, AI content policies.
  - Compare and contrast approaches across platforms.
- C2PA (Coalition for Content Provenance and Authenticity) / Content Credentials:
  - Overview of the standard and participating organizations.
  - Current adoption status across platforms and devices.
  - Note: detailed technical implementation covered in Section 5.2 of the paper.
- Industry alliances and collective commitments:
  - Partnership on AI.
  - Frontier Model Forum.
  - Voluntary commitments made at the White House (July 2023) and Seoul Summit.
  - OECD AI Principles adherence.

**3. AGENTIC AI GOVERNANCE GAP**

- Current Frontier AI Safety Frameworks primarily address model-level safety and are INSUFFICIENT for agent deployment scenarios. Explain why.
- MCP governance gap: Anthropic initially "left security to the user" when launching MCP — document this and its consequences.
- The deployment-governance velocity mismatch: agents are already in production (Claude Code, Codex, Devin, etc.) but governance frameworks haven't caught up.
- Emerging standards attempting to fill the gap:
  - OWASP Top 10 for LLM Applications 2025 — how it addresses agentic scenarios.
  - MCP security best practices guides (Anthropic's own, community-driven).
  - Wiz, Trail of Bits, and other security firm recommendations.
- The standardization challenge: no equivalent of "ISO 27001 for AI agents" exists yet.

Provide complete references — organization names, document titles, publication dates, URLs. This section requires authoritative primary sources from the organizations themselves.
