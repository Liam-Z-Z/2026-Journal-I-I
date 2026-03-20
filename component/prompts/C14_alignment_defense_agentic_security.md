# Component 14 — Alignment, Adversarial Defense & Agentic Security

- **Section:** §5.3
- **Model:** Claude
- **Topic:** Alignment Techniques, Adversarial Defense, and Securing Agentic AI Systems

---

## Prompt

You are helping me write a section of an academic survey on "Security and Safety of AI-Generated Content." This section (Section 5.3) covers three interconnected defense layers: alignment techniques, defenses against adversarial manipulation, and the emerging field of securing agentic AI systems.

Please produce a comprehensive research document covering:

**1. ALIGNMENT TECHNIQUES**

- The RLHF pipeline: Ouyang et al. (2022) — explain the three stages (SFT → reward model training → PPO optimization).
- Evolution beyond RLHF:
  - DPO (Direct Preference Optimization) — Rafailov et al. (2023): how it eliminates the reward model. Technical intuition and practical advantages.
  - KTO (Kahneman-Tversky Optimization): using only binary feedback.
  - Constitutional AI (Bai et al., 2022) and RLAIF: using AI feedback instead of human feedback. Explain the constitutional principles approach.
  - IPO (Identity Preference Optimization) and other variants.
- Multi-objective alignment: balancing helpful + harmless + honest. The tension between helpfulness and safety (over-refusal problem).
- Pluralistic alignment: how should "safe behavior" be defined when cultural norms differ? The challenge of whose values to align to.
- Limitations of current alignment:
  - Reward hacking: models gaming the reward signal.
  - Annotator bias: RLHF reflects annotator demographics and values.
  - Superficial alignment: safety training may be a "veneer" that is easily removed (cite evidence on fine-tuning attacks removing safety).
  - Alignment tax: the capability cost of safety training.

**2. DEFENSE AGAINST ADVERSARIAL MANIPULATION**

- Opening: "To counter the adversarial manipulation strategies categorized in Section 3.3..."
- INPUT LAYER defenses:
  - Prompt classification and filtering: detecting malicious inputs before they reach the model. Specific systems and approaches.
  - Perplexity-based filtering: using perplexity scores to detect adversarial suffixes (which tend to have high perplexity).
  - Input preprocessing: paraphrasing, retokenization.
- SYSTEM LAYER defenses:
  - Instruction hierarchy: giving system instructions higher priority than user inputs. Cite OpenAI's instruction hierarchy paper.
  - Privilege separation between system and user instructions.
  - Delimiters and structured prompting.
- OUTPUT LAYER defenses:
  - Safety classifiers on model outputs.
  - Output filtering and post-processing.
  - Self-check mechanisms: having the model evaluate its own output for safety.
- MODEL LAYER defenses:
  - Safety fine-tuning and its robustness.
  - Circuit breakers (Zou et al., 2024): representation engineering approach to refusing harmful requests — explain the mechanism.
  - Refusal training and its limitations.
  - Representation engineering: directly modifying model internals.
  - Adversarial training: training on adversarial examples.
- Defense-in-depth: why no single layer is sufficient and how layers compose.
- Evaluation benchmarks: HarmBench, JailbreakBench, StrongREJECT — what they measure and current state-of-the-art results.
- Current status: "sophisticated attacks still succeed ~50% of the time" — the defense gap is real and significant.

**3. SECURING AGENTIC AI SYSTEMS**

- Opening: "To secure against the agentic threats identified in Section 3.3.3..."

**(a) Architecture-Level Defenses:**
- Trust boundaries: strict separation of system instructions vs. external data.
- Context isolation: prevent retrieved/external content from executing as instructions. Techniques and challenges.
- Least privilege principle applied to agents: restrict tool access scope and action permissions by default.
- Privilege separation: distinguish read vs. write; require explicit user confirmation for high-risk actions (destructive operations, external communications, financial transactions).
- Reference Google's layered defense strategy for Gemini, OWASP LLM01:2025 guidance.

**(b) MCP-Specific Security:**
- Input validation: parameterized queries to prevent SQL injection → stored prompt injection chains.
- Tool call validation: security checks before each tool invocation — what should be verified?
- Authentication and authorization: session tokens, origin verification. Cite the MCP Inspector authentication bypass fix as a case study.
- Secure configuration: avoid exposing MCP servers to public internet, restrict network access.
- Emerging standards: MCP protocol 2025-03 authorization specification updates, community security guidelines.

**(c) Monitoring and Observability:**
- Agent behavior audit trails: logging all tool calls, decisions, and data flows.
- Anomaly detection: identifying tool-call patterns deviating from expected behavior.
- Human-in-the-loop mechanisms: when and how to require confirmation for high-risk operations.
- The statistic: "only 47% of organizations have implemented GenAI-specific security controls" — cite the source.

**(d) Open Challenges:**
- Tool name collision / tool poisoning defense.
- Cross-agent trust chain management in multi-agent systems.
- Balancing security with usability — over-restricting agents defeats their purpose.
- The structural challenge: OpenAI's characterization as "a frontier research problem."

Provide complete references — full paper titles, author names, publication venues, years, arXiv IDs, and URLs for web sources.
