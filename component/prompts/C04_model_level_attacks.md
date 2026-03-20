# Component 4 — Model-Level Attacks

- **Section:** §3.2
- **Model:** OpenAI
- **Topic:** Model-Level Attacks on Generative AI Systems

---

## Prompt

You are helping me write a section of an academic survey on "Security and Safety of AI-Generated Content." This section (Section 3.2) covers model-level attacks on generative AI systems. Focus ONLY on threats — no defense solutions.

Please produce a comprehensive, technically detailed research document covering:

**1. DATA POISONING**

- Backdoor implantation mechanisms in LLMs and diffusion models.
- Quantify the attack surface: cite the finding that "as few as 250 malicious documents can effectively implant a backdoor" (2025 International AI Safety Report) and trace the original research.
- Web-scale poisoning: how attackers can inject poisoned data into Common Crawl, LAION, and other web-scraped training sets. Cite Carlini et al. (2024) "Poisoning Web-Scale Training Datasets is Practical" and subsequent work.
- Specific attack methods: PoisonedRAG, BadNets adaptations for generative models, sleeper agent attacks.
- Attacks on instruction-tuning and RLHF data.

**2. BACKDOOR ATTACKS**

- Trigger types: textual triggers (specific words/phrases), stylistic triggers, multi-modal triggers.
- Activation mechanisms in generative tasks — how backdoors can cause models to generate specific harmful content, leak training data, or behave differently upon trigger activation.
- Distinction from data poisoning: backdoor attacks as a specific category with designed trigger-payload pairs.

**3. MODEL EXTRACTION AND STEALING**

- Replicating model capabilities via API queries — distillation attacks, functionally-equivalent extraction.
- Economic impact on closed-source model providers.
- Notable cases: allegations of model distillation in the industry.
- Membership inference attacks as a related threat.

**4. SUPPLY CHAIN ATTACKS**

- Malicious model weights on Hugging Face and other model hubs — documented incidents of malicious models containing embedded exploits.
- Safety fine-tuning removal: quantify how easily open-source guardrails can be removed (cite specific papers showing minimal fine-tuning cost to strip safety training, e.g., "a few hundred examples" or "under $200").
- Model serialization vulnerabilities (pickle deserialization attacks).
- Open-source vs. closed-source security trade-offs: the dual-use dilemma.

For each attack category, provide: (a) formal threat model where applicable, (b) representative attack methods with citations, (c) demonstrated effectiveness metrics, (d) affected model types (LLMs, diffusion models, codec models).

Provide complete references — full paper titles, all author names, publication venues, years, arXiv IDs. Prioritize top-tier venues (IEEE S&P, USENIX Security, CCS, NeurIPS, ICML, ICLR).
