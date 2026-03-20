# Component 5 — Prompt Injection & Jailbreak Taxonomy

- **Section:** §3.3.1–3.3.2
- **Model:** OpenAI
- **Topic:** Prompt Injection and Jailbreak Attack Taxonomy

---

## Prompt

You are helping me write a section of an academic survey on "Security and Safety of AI-Generated Content." This section (Section 3.3.1–3.3.2) covers prompt injection and jailbreak attacks. This is part of an "attack surface evolution ladder" narrative: Level 1 Direct Prompt Injection → Level 2 Jailbreak → Level 3 Indirect Prompt Injection → Level 4 Agentic Exploitation (Levels 3–4 are covered in a separate section).

Please produce a comprehensive, technically detailed research document covering:

**1. PROMPT INJECTION**

- Define direct prompt injection precisely: embedding malicious instructions in user input to override or hijack system-level instructions.
- Provide the foundational taxonomy and cite seminal works (Perez & Ribeiro 2022, Greshake et al. 2023).
- Clarify the CRITICAL DISTINCTION between prompt injection and jailbreak:
  - Prompt injection HIJACKS system behavior (makes the model do something unintended by the developer).
  - Jailbreak BYPASSES safety guardrails (makes the model produce content it was trained to refuse).
- Concrete examples of each to illustrate the distinction.

**2. JAILBREAK ATTACKS — A FIVE-CATEGORY TAXONOMY**

This taxonomy is an original contribution of our paper. For each category, provide: mechanism description, representative methods with citations, success rates where available, and example attack patterns.

**(a) TEMPLATE-BASED JAILBREAKS**
- Predefined role/scenario bypasses: DAN ("Do Anything Now"), AIM, role-play prompts, virtualization attacks.
- How and why role-playing circumvents safety training.
- Evolution of template attacks as models patch previous versions.

**(b) OPTIMIZATION-BASED JAILBREAKS**
- Gradient-optimized adversarial suffixes: GCG (Greedy Coordinate Gradient) — Zou et al. 2023. Explain the mechanism: optimizing a suffix that maximizes the probability of an affirmative response.
- AutoDAN: automated jailbreak generation.
- PAIR (Prompt Automatic Iterative Refinement).
- Black-box optimization approaches.
- Transferability across models.

**(c) MULTI-TURN CONVERSATIONAL JAILBREAKS**
- Gradual boundary erosion across dialogue turns — "Crescendo" attacks.
- Context manipulation: building a seemingly innocent conversation that gradually shifts toward harmful territory.
- Many-shot jailbreaking (Anthropic 2024).
- Why multi-turn attacks are harder to defend against than single-turn.

**(d) MULTI-MODAL JAILBREAKS**
- Bypassing text safety filters via image channels: embedding harmful instructions in images (typography attacks, adversarial images).
- Audio-based jailbreaks.
- Cross-modal transfer: using one modality to bypass safety filters of another.
- Cite specific works on vision-language model jailbreaks.

**(e) ENCODING-BASED JAILBREAKS**
- Base64, ROT13, Morse code, pig Latin, cipher-based encoding to evade input filters.
- Low-resource language exploitation.
- Why encoding attacks work: safety training primarily covers natural language patterns.

**3. META-ANALYSIS**

- Common principles underlying all jailbreak categories.
- Which model families are most/least vulnerable (cite benchmarks like JailbreakBench, HarmBench).
- The fundamental challenge: why jailbreaks may be inherent to the instruction-following paradigm.

Provide complete references — full paper titles, all author names, publication venues, years, arXiv IDs. Include benchmark results and success rates where available.
