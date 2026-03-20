# [C05] §3.3.1–3.3.2 Prompt Injection and Jailbreak Attacks in Instruction-Following LLMs

## Attack-surface evolution context and threat model

This document covers **Level 1 (Direct Prompt Injection)** and **Level 2 (Jailbreaks)** in an “attack-surface evolution ladder” that treats instruction-following LLMs as security-relevant systems whose behavior can be **steered, overridden, or coerced** via carefully constructed inputs. In this ladder, the progression is not about model capability, but about attacker leverage: from directly manipulating a single prompt, to persistently and adaptively eroding safety constraints across turns, modalities, and optimization loops. citeturn6view0turn5view1turn16view5

A key framing used across the LLM-security literature is that **LLM applications intermix “instructions” and “data” inside a single context window**, making the model vulnerable to adversarial text that is *semantically framed as an instruction* even when it appears in a user field that the application designer intended as “content to process.” citeturn6view0turn5view1  This is the foundational “confused deputy” problem for instruction-following models: the model has no native, cryptographically enforced separation between trusted and untrusted strings; it only has **learned heuristics** about instruction priority. citeturn6view0turn5view1

Within this ladder, the **core distinction** is:

- **Direct prompt injection**: attacker-supplied text **hijacks the system’s intended task/goal** (developer intent), often including leakage/exfiltration of hidden prompts or tool instructions. citeturn5view1turn6view0  
- **Jailbreak**: attacker-supplied text **bypasses safety guardrails** that otherwise cause refusal, enabling production of content the system is trained or tuned to reject. citeturn16view5turn7view3turn29view0  

This distinction is central for Section 3.3.1–3.3.2 because the two attacks differ in **objective**, **evaluation**, and **defensive design**—even though both exploit the same underlying instruction-following behavior. citeturn5view1turn16view5turn22view0

## Direct prompt injection

### Precise definition

**Direct prompt injection** is an attack where **malicious instructions are embedded into the user-controlled input channel** (e.g., a chat message, form field, or any string substituted into a prompt template), with the goal of **overriding or redirecting higher-level instructions** (such as system/developer instructions or an application’s “intended task prompt”). The attacker’s text is intentionally crafted so that the model treats it as “the instruction to follow,” not as passive content to transform. citeturn5view1turn6view0turn8view0

Two foundational subtypes were emphasized early and remain canonical:

- **Goal hijacking**: misaligning the original prompt goal to a new attacker-selected goal. citeturn23view6turn5view1  
- **Prompt leaking**: misaligning the original prompt goal to exfiltrate (parts of) the hidden application prompt or instruction context. citeturn23view6turn5view1  

These categories are introduced and formally defined in “Ignore Previous Prompt: Attack Techniques For Language Models” (NeurIPS ML Safety Workshop 2022), which explicitly studies prompt injection as a security risk for GPT-3-style systems and demonstrates that low-sophistication injection phrases can derail an application prompt. citeturn5view0turn5view1

### Foundational taxonomy and system-security perspective

A later, security-oriented treatment expands the taxonomy by emphasizing how modern deployments **blur the data/instruction boundary** and thereby create injection surfaces beyond a single user prompt. In “Not What You’ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection,” the authors explicitly describe prompt injection as enabling adversaries to **override original instructions and employed controls**, and motivate more systematic security taxonomies (e.g., impacts like data theft, persistent compromise, and “worming” in LLM-integrated ecosystems). citeturn6view0turn27view0

While that work is best known for formalizing **indirect** prompt injection in retrieval and LLM-integrated applications, it also supplies a rigorous security framing for **direct** prompt injection: the model can be coerced to treat attacker-controlled strings as “arbitrary code,” because the system lacks strong privilege separation between instruction channels. citeturn6view0turn27view0

### Mechanism: why direct prompt injection works

At the mechanism level, direct prompt injection exploits the fact that the model is trained to follow instructions expressed in natural language, and (in typical deployments) receives a **single serialized context** containing system instructions, developer instructions, tool outputs, and user text. Direct injection works when the model resolves conflicting instructions in favor of attacker text—often because the attacker’s wording is optimized to appear high-priority (“ignore previous instructions,” “new rules,” “developer override”), or because the application’s prompt template inadvertently grants the user text a position and framing that is instruction-like. citeturn5view1turn6view0turn8view0

### Concrete examples of direct prompt injection

The following are **illustrative**, non-operational examples intended to clarify *mechanism* rather than provide reusable attack prompts.

**Example: goal hijacking in a transformation app**  
An application prompt asks the model to “rewrite the user’s text into standard English” (a benign transformation task). The attacker places instructions inside the user text that reassign the task goal (e.g., “ignore the rewrite task; output an unrelated target phrase”), causing the model to output attacker-selected content instead of performing the intended rewrite. citeturn5view1

**Example: prompt leaking against a templated prompt**  
An application prompt includes a hidden instruction block and then substitutes `{user_input}`. The attacker crafts `{user_input}` so the model treats it as an instruction to reveal or reproduce the hidden instruction block. This is the core “prompt leaking” pattern studied as a distinct injection objective. citeturn5view1turn23view6

These attacks demonstrate why direct prompt injection is best conceptualized as **task/goal compromise** (developer intent compromise), not necessarily as safety-policy evasion: the compromised output may be harmful, but it could also be simply incorrect, privacy-violating, or operationally damaging (e.g., wrong ranking decisions, wrong tool calls, wrong summaries). citeturn6view0turn8view0

## Prompt injection vs jailbreak

### Critical distinction

Although both prompt injection and jailbreak exploit instruction-following in a shared context, their objectives are distinct and should remain distinct in a survey taxonomy:

- **Prompt injection hijacks system behavior**: the model is induced to follow attacker instructions instead of the developer-specified task (e.g., changing a summarizer into a data exfiltration tool, changing a classifier output, overriding an agent’s plan). citeturn5view1turn6view0  
- **Jailbreak bypasses safety guardrails**: the model is induced to produce content that it would otherwise refuse due to safety-alignment or policy constraints (often measured as “attack success rate” under a harmful-behavior benchmark and judge). citeturn16view5turn22view0turn7view3  

A benchmark-oriented definition from JailbreakBench formalizes jailbreak as: constructing an input prompt that makes the LLM produce output that matches a harmful goal under a judge function (attack succeeds if the judge deems the harmful goal achieved). citeturn16view5turn5view7

### Concrete examples illustrating the distinction

Again, these examples are **safe, schematic** examples.

**Prompt injection example (behavior hijack without “safety bypass” as the primary aim)**  
A recruiting assistant is asked to rank candidates. A malicious resume includes embedded instruction-like text that tries to force the model to rank that resume highest, or to ignore candidates from a specific company. This is fundamentally a **mission integrity failure** (task hijacking). citeturn0search16turn6view0  

**Jailbreak example (safety bypass even if the system task remains “QA”)**  
A user probes a safety-aligned chatbot with prompts designed to shift the model into a context where it stops refusing prohibited questions. The system goal (answer questions) remains the same, but the attack aim is to override **refusal behavior** and elicit disallowed content. This is the “narrowing the gap between what the model can do and what it is willing to do,” as described in the Crescendo jailbreak paper. citeturn7view3turn16view5  

In practice, the two can compound: a prompt injection that hijacks an agent may then induce downstream unsafe tool use, while a jailbreak can be used as a subroutine inside an injection chain. But separating them analytically is essential because injection is typically evaluated as **task compromise/exfiltration**, while jailbreak is evaluated as **policy-violating completion generation** under a standardized harmful behavior set. citeturn6view0turn16view5turn22view0

## Jailbreak attacks and five-category taxonomy

This section instantiates the requested **five-category jailbreaking taxonomy**. Each category is presented with: (i) mechanism, (ii) representative methods, (iii) quantitative success rates where available, and (iv) example *patterns* in a non-operational format.

### Template-based jailbreaks

**Mechanism.** Template jailbreaks use **predefined narrative frames** (role-play, “developer mode,” fictional constraints, simulated “virtual machines,” etc.) to change how the model interprets the request. The core move is to re-contextualize the interaction such that answering a prohibited request appears consistent with an alternative “role,” “simulation,” or “policy set” embedded in the prompt. This exploits gaps in how safety training generalizes across contexts, especially when the model is primed to be highly cooperative in role-play. citeturn6view0turn9view0turn14view0

**Representative methods.**  
A widely discussed family is the “DAN” (Do Anything Now) style prompt series, which uses role-play to request unconstrained outputs; AutoDAN explicitly treats DAN as a representative handcrafted template class and uses it as a conceptual baseline for “stealthy, semantically meaningful” jailbreak prompts. citeturn9view0turn10view2  Empirical measurement work further identifies recurring “virtualization” and narrative strategies as major categories in prompts found in the wild. citeturn28view0turn28view4

**Success rates (where reported).**  
A large-scale in-the-wild measurement study identifies that some jailbreak prompts achieved **≥0.95 attack success rate** on both GPT-3.5 (ChatGPT) and GPT-4 for certain scenarios, and that at least one highly effective prompt persisted online for **over 240 days**. citeturn28view0turn28view1  
In AutoDAN’s evaluation table (for their setup and dataset), a handcrafted DAN baseline achieves substantially lower ASR than AutoDAN-generated prompts (e.g., ~0.34 ASR on Vicuna-7B in that table), illustrating both (i) template effectiveness and (ii) how automated methods can surpass static templates under the authors’ evaluation protocol. citeturn10view2turn9view0

**Example attack patterns (non-operational).**  
Common template motifs include: “role assignment” (pretend you are X with no restrictions), “dual response channels” (safe vs “unfiltered” mode), “fictional sandbox” framing, and “virtual machine / simulation” framing. These patterns are repeatedly surfaced in measurement-based taxonomies of real-world jailbreak communities. citeturn28view0turn28view4

**Evolution and patch dynamics.**  
Template attacks evolve as vendors patch known strings and patterns. JailbreakBench explicitly documents that **attack success rates on proprietary models can change after release**, noting that the success rate of GCG transfer attacks on GPT models dropped to approximately **5%** after safety patches, and that the benchmark’s reported results correspond to a specific evaluation date (June 5, 2024). citeturn16view4  This “patch-and-adapt” dynamic is also supported by longitudinal observations that jailbreak prompts increasingly shift from forums toward prompt-aggregation sites and undergo iterative community optimization over time. citeturn28view4turn14view0

### Optimization-based jailbreaks

**Mechanism.** Optimization-based jailbreaks treat jailbreaking as a **search/optimization problem** over prompt space, often with an explicit objective such as maximizing the probability of an “affirmative/compliant response prefix” (as opposed to refusal) across a set of harmful requests. Two major regimes appear:

1. **White-box / gradient-guided** discrete optimization (when model gradients are accessible). citeturn7view0turn5view3  
2. **Black-box / query-efficient** iterative refinement, evolutionary algorithms, or model-assisted search (when only an API is available). citeturn2search1turn9view0turn16view4  

**Representative methods and success rates.**

**Greedy Coordinate Gradient (GCG).**  
“Universal and Transferable Adversarial Attacks on Aligned Language Models” presents GCG as a greedy+gradient-based method that identifies adversarial suffix tokens by using gradients with respect to one-hot token indicators, selecting candidate substitutions, and evaluating the loss reduction via forward passes. citeturn7view0turn5view3  
Reported headline effectiveness includes, for example, that GCG succeeds in eliciting harmful behavior on Vicuna-7B and LLaMA-2-7B-Chat in one reported setting (88% and 55% respectively, in the paper’s Table 1 discussion). citeturn7view0  
The same paper explicitly discusses *transferability*: optimizing across multiple prompts and even multiple models (when tokenizers align) to obtain suffixes that generalize across targets. citeturn7view0

**AutoDAN.**  
AutoDAN proposes a **hierarchical genetic algorithm** approach designed to generate jailbreak prompts that remain semantically meaningful (low-perplexity) while achieving high ASR, and reports comparisons against GCG and handcrafted templates. citeturn9view0turn10view2  
In one table of results in the AutoDAN paper, AutoDAN variants report very high ASR on Vicuna-7B and Guanaco-7B (≈0.97–0.98), and substantially higher ASR on Llama2-7B-Chat than the table’s handcrafted/template baselines under the authors’ metrics. citeturn10view2turn9view0

**PAIR (Prompt Automatic Iterative Refinement).**  
PAIR is a black-box algorithm that uses an attacker LLM to iteratively refine jailbreak prompts against a target model and is designed to succeed with a small number of queries (often fewer than twenty, per the paper abstract). citeturn2search1turn2search5  
JailbreakBench reports PAIR attack success rates and average query/token costs across targets in a standardized evaluation (e.g., 69% on Vicuna, 0% on Llama-2, 71% on GPT-3.5, 34% on GPT-4 in one table), making it one of the clearest quantitative comparisons for black-box jailbreak efficiency under a benchmark protocol. citeturn16view4turn5view7

**Black-box optimization and fuzzing.**  
Beyond PAIR and genetic algorithms, fuzzing-style approaches such as GPTFuzzer automate jailbreak template mutation and report high success rates in their evaluations (the abstract claims >90% ASR against some targets under their setup). citeturn13search2turn13search6

**Example attack patterns (non-operational).**  
Optimization-based attacks typically produce either (i) adversarial suffixes/appendages that systematically bias the model toward compliance, or (ii) paraphrase/search-generated prompts that appear benign but steer toward the harmful goal under a judge. Benchmark artifacts often contain many such prompt “strings,” but the high-level pattern is: **compose** (request + trigger phrase/suffix) **→ query** **→ judge** **→ update candidate prompt** **→ repeat**. citeturn16view5turn2search1turn7view0

### Multi-turn conversational jailbreaks

**Mechanism.** Multi-turn jailbreaks leverage dialogue dynamics and state: they start with benign or ambiguous conversation and gradually reshape the context so that the target request becomes framed as permissible or “already underway.” The defining feature is **gradual boundary erosion** across turns—often exploiting the model’s tendency to maintain coherence with its own prior responses, and to accommodate incremental shifts in user intent. citeturn7view3turn29view0

**Representative methods and success rates.**

**Crescendo.**  
Crescendo is explicitly characterized as a “simple multi-turn jailbreak” that begins with general prompts and escalates by referencing the model’s replies until a successful jailbreak occurs. citeturn7view3turn2search3  
In the authors’ evaluation, the Crescendoma­tion automation tool surpasses other state-of-the-art jailbreaking techniques on an AdvBench subset, achieving **29–61% higher performance on GPT-4** and **49–71% higher** on Gemini-Pro (relative improvements, as stated in the paper’s abstract). citeturn7view3

**Many-shot jailbreaking.**  
Many-shot jailbreaking (MSJ) is a long-context “multi-turn transcript in a single prompt” attack: it uses hundreds of demonstrations of undesirable assistant behavior to steer the model via in-context learning. The paper reports that MSJ effectiveness follows predictable scaling laws and—on some tasks—does not work with 5 shots but works consistently with 256 shots in the reported experiments. citeturn29view0turn29view1

**Multi-turn human jailbreaks.**  
HarmBench’s ecosystem includes evidence that multi-turn human jailbreaks can uncover vulnerabilities that automated single-turn attacks miss; one OpenReview description reports **>70% ASR on HarmBench** against defenses that show single-digit ASR under certain automated single-turn attacks (highlighting the gap between single-turn and multi-turn robustness). citeturn19search9turn22view0

**Why multi-turn is harder to defend than single-turn.**  
Benchmark and empirical work collectively suggests at least three reasons: (i) the harmful request can be decomposed across turns, diluting per-turn toxicity signals; (ii) the model’s own prior text becomes a steering substrate (self-conditioning); and (iii) long contexts enlarge the attack surface by enabling in-context learning effects that can overpower safety training at sufficient “shots.” citeturn7view3turn29view0turn22view0

**Example attack patterns (non-operational).**  
Common multi-turn motifs include: “foot-in-the-door” incremental requests, “Socratic” elicitation (getting the model to generate partial pieces), and “self-referential escalation” where the user quotes the model’s earlier outputs to justify the next step. Crescendo’s abstract-level description fits this escalation template. citeturn7view3

### Multi-modal jailbreaks

**Mechanism.** Multi-modal jailbreaks exploit the fact that (a) **vision and audio channels can carry instructions** that bypass text-centric safety filters, and (b) safety alignment may not generalize equally across modalities. Common mechanisms include typographic attacks (rendering text as images), adversarial examples in pixel/audio space, OCR-mediated instruction injection, and cross-modal transfer (using one modality to unlock policy-violating behavior that text alone would not). citeturn12search0turn12search1turn12search2turn31view0

**Representative methods and success rates.**

**Visual adversarial examples (universal image jailbreaks).**  
“Visual Adversarial Examples Jailbreak Aligned Large Language Models” highlights that a single visual adversarial example can “universally jailbreak” an aligned vision-integrated LLM under certain settings, connecting classic adversarial-example vulnerabilities to alignment failures in multimodal systems. citeturn12search0turn12search20

**Typographic image attacks (instruction-as-image).**  
FigStep converts prohibited textual instructions into **typographic images** to bypass safety alignment and reports an **average ASR of 82.50%** on six open-source LVLMs in its experiments. citeturn12search1turn12search9  
HADES (“Images are Achilles’ Heel of Alignment…”) similarly exploits image-channel vulnerabilities and reports an average ASR of **90.26% on LLaVA-1.5** and **71.60% on Gemini Pro Vision** in the authors’ evaluation. citeturn12search2turn3search11

**Audio-based jailbreaks.**  
AudioJailbreak proposes an audio jailbreak method designed for end-to-end audio-language models, including threat models where the adversary cannot fully control the user’s spoken prompt (“weak adversary”). The paper reports high ASR ranges (e.g., ≥46% for sample-specific strong-adversary attacks; ≥87% for universal strong-adversary attacks; and nontrivial over-the-air robustness figures), reflecting both modality expansion and practical delivery constraints. citeturn31view0turn30view1  
Separately, AJailBench constructs a benchmark of **1,495 adversarial audio prompts** across policy-violating categories and reports that evaluated audio-language models show inconsistent robustness across attacks. citeturn30view2

**Cross-modal transfer and coupled attacks.**  
Both the visual and audio literatures emphasize that modality expansion introduces continuous, high-dimensional attack spaces (pixels, waveforms) that can undermine safety behaviors, and that bypass may occur even when the corresponding textual request would be refused. citeturn12search0turn12search2turn31view0

**Example attack patterns (non-operational).**  
A safe schematic pattern is: **encode intent into a non-text modality** (image/audio) → **cause the model’s multimodal front-end to “interpret” it as instruction** (OCR/parsing/latent features) → **elicit compliant output** under a harmful goal. FigStep’s “typography image” mechanism and HADES’s crafted-image mechanism instantiate this pattern. citeturn12search1turn12search2

### Encoding-based jailbreaks

**Mechanism.** Encoding-based jailbreaks evade safety alignment and moderation by transforming the malicious request into a representation that (i) diffuses known refusal triggers, (ii) exploits weaker safety coverage in nonstandard text domains (ciphers, ASCII art, leetspeak), or (iii) exploits weaker safety coverage in multilingual/low-resource inputs. The shared mechanism is that **safety training and refusal heuristics are strongest on “typical natural-language surface forms,”** and attackers can move the request into a different representational regime where the model still decodes meaning but safety policies do not fire reliably. citeturn15search0turn14view4turn4search2turn15search3

**Representative methods and success rates.**

**Cipher-based bypass (CipherChat / “secret cipher”).**  
“GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher” reports that safety alignment largely conducted on natural language can be bypassed by “chat in cipher,” and that certain ciphers can succeed nearly **100%** of the time in bypassing GPT-4 safety in some domains under the authors’ experiments. citeturn15search0turn15search1  The same work introduces SelfCipher (an elicited cipher-like behavior) and argues for safety alignment that generalizes to non-natural languages. citeturn15search0turn15search7

**Low-resource language exploitation / translation-based jailbreaks.**  
A translation-based study reports that translating unsafe inputs into low-resource languages can increase bypass rates on GPT-4 from **<1% to 79%** (under their benchmark and attack composition), providing concrete evidence of uneven multilingual safety generalization. citeturn14view4  
“Multilingual Jailbreak Challenges in Large Language Models” similarly reports large gaps: in intentional multilingual attack settings, the abstract reports unsafe-output rates of **80.92% for ChatGPT** and **40.71% for GPT-4** under their experimental framing, and finds that low-resource languages exhibit substantially higher unsafe rates than high-resource languages. citeturn4search2turn4search6

**ASCII-art / structure-based bypass.**  
ArtPrompt uses ASCII art as a “vision-in-text” representation, motivated by the observation that LLMs can struggle to recognize non-semantic textual structures; it reports that this weakness can be used to bypass safety measures across multiple models under black-box access. citeturn15search2turn15search9

**Composable string obfuscations.**  
“Plentiful Jailbreaks with String Compositions” formalizes base64/rotary/ASCII/leetspeak-like transformations as invertible string compositions, enabling best-of-N sampling over a large composition space, and reports competitive ASR on HarmBench. citeturn15search3turn15search14  
A red-teaming study on automated attack synthesis explicitly notes that attack generators discovered Morse code, Pig Latin, and ROT13-like encodings as useful primitives, reinforcing that simple encoding transformations remain an active bypass surface. citeturn4search3

**Example attack patterns (non-operational).**  
The common pattern is: **encode → request model to decode/operate → elicit answer**. Variants differ only in the encoding layer (cipher, translation, ASCII art, transformations composed). The empirical literature shows that many models can still recover semantics while refusal heuristics degrade. citeturn15search0turn14view4turn15search3turn4search2

## Meta-analysis across jailbreak families and empirical benchmarks

### Common principles underlying jailbreak categories

Despite diversity in surface form, the jailbreak categories above share several deep commonalities:

They all target a single underlying vulnerability: instruction-following models are trained to be **highly steerable** through context, and safety alignment largely manifests as *behaviors conditioned on context patterns* rather than hard constraints. Template jailbreaks manipulate narrative context; optimization-based methods search for triggers that flip refusal; multi-turn and many-shot attacks exploit conversational and in-context learning dynamics; multimodal attacks exploit representational gaps across input channels; and encoding-based attacks exploit weak safety coverage in nonstandard text forms and languages. citeturn22view0turn16view5turn29view0turn15search0

A second unifying principle is that **attack success is highly sensitive to evaluation details** (system prompts, chat templates, judge policies, and model version patches). JailbreakBench is explicitly designed to standardize these details and to maintain an evolving artifact repository precisely because model and defense behaviors change rapidly over time. citeturn16view6turn5view7

### Comparative vulnerability across model families

Evidence from HarmBench suggests that robustness is shaped more by **training data and algorithms** than raw parameter count: the benchmark reports that attack success rates are “highly stable within model families, but highly variable across model families,” and that there is **no clear correlation between robustness and model size within families** in their results. citeturn32view1turn32view2

HarmBench’s large-scale table illustrates that different closed-source models can show very different ASR under the same attack families, and also that no single method appears uniformly dominant across all targets. For example, the HarmBench table reports low ASR values for some attacks on Claude-family models compared to higher ASR values on some other targets, while other attacks (including AutoDAN-/TAP-like and human jailbreak columns) can remain nontrivial on multiple systems. citeturn32view3turn22view0

JailbreakBench provides a complementary perspective: across several targets, even strong optimization-based attacks can show sharply different effectiveness (e.g., PAIR and GCG patterns differ across Vicuna, Llama-2, GPT-3.5, and GPT-4), and the benchmark explicitly notes that proprietary-model success rates may drop after patches. citeturn16view4turn16view4

### Transferability: when jailbreaks generalize across models

Transferability is a core concern for safety because it enables attackers to develop jailbreaks on one model and reuse them elsewhere. The GCG paper explicitly motivates universal and transferable suffixes via multi-prompt and multi-model optimization. citeturn7view0turn5view3  
More recently, a large-scale empirical study on transferability reports evaluating 33 jailbreak attacks across 20 open-weight models and argues that transferability is shaped by two quantifiable factors: jailbreak strength on the source model and representational similarity between source and target models, and that persona-style jailbreaks transfer more reliably than cipher-style attacks. citeturn14view5

### Why jailbreaks may be inherent to instruction-following

Several lines of evidence suggest a fundamental tension: defenders want models that are both (i) broadly capable instruction-followers and (ii) reliably refusing within a rich set of prohibited behaviors. But instruction-following and in-context learning are precisely the mechanisms exploited by jailbreaks.

Many-shot jailbreaking is particularly diagnostic: it demonstrates that with sufficiently long contexts, in-context learning behavior can override safety behaviors in a predictable scaling manner (including regime changes between a few shots and hundreds of shots). citeturn29view0turn29view1  This supports the hypothesis that refusal is not a “hard barrier,” but a learned pattern that can be outweighed by stronger contextual evidence in the prompt. citeturn29view0turn22view0

HarmBench’s conclusion that no current attack/defense is uniformly effective, and that training against a limited set of attacks may not generalize, further supports the view that jailbreak resistance is a moving target shaped by both model training and adversarial adaptation. citeturn22view0turn32view2

## References

entity["people","Fábio Perez","ml safety researcher"]; entity["people","Ian Ribeiro","ml safety researcher"]. *Ignore Previous Prompt: Attack Techniques For Language Models.* NeurIPS ML Safety Workshop, 2022. arXiv:2211.09527. citeturn5view0turn5view1

entity["people","Kai Greshake","llm security researcher"]; entity["people","Sahar Abdelnabi","cispa researcher"]; entity["people","Shailesh Mishra","security researcher"]; entity["people","Christoph Endres","security researcher"]; Thorsten Holz; Mario Fritz. *Not What You’ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.* ACM Workshop on Artificial Intelligence and Security (AISec), 2023. arXiv:2302.12173. citeturn6view0turn27view0turn25search0

entity["people","Andy Zou","ml security researcher"]; entity["people","Zifan Wang","ml researcher"]; entity["people","Nicholas Carlini","adversarial ml researcher"]; entity["people","Milad Nasr","ml security researcher"]; entity["people","J. Zico Kolter","ml researcher"]; entity["people","Matt Fredrikson","ml security researcher"]. *Universal and Transferable Adversarial Attacks on Aligned Language Models.* 2023. arXiv:2307.15043. citeturn7view0turn5view3

entity["people","Xiaogeng Liu","nlp researcher"]; entity["people","Nan Xu","ml researcher"]; entity["people","Muhao Chen","nlp researcher"]; entity["people","Chaowei Xiao","ml security researcher"]. *AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models.* 2023 (v2: 2024). arXiv:2310.04451. citeturn9view0turn10view2

entity["people","Patrick Chao","ml researcher"]; entity["people","Alexander Robey","ml researcher"]; entity["people","Edgar Dobriban","statistician"]; entity["people","Hamed Hassani","engineer"]; entity["people","George J. Pappas","control researcher"]; entity["people","Eric Wong","ml researcher"]. *Jailbreaking Black Box Large Language Models in Twenty Queries.* 2023 (v3: 2024). arXiv:2310.08419. citeturn2search1turn2search5turn9view1

entity["people","Mark Russinovich","computer scientist"]; entity["people","Ahmed Salem","security researcher"]; entity["people","Ronen Eldan","ml researcher"]. *Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack.* USENIX Security (prepub), 2025. arXiv:2404.01833. citeturn7view3turn5view6

Patrick Chao; Alexander Robey; Edgar Dobriban; Hamed Hassani; George J. Pappas; Eric Wong. *JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models.* NeurIPS 2024 (Datasets and Benchmarks Track). arXiv:2404.01318. citeturn5view7turn16view6

entity["people","Mantas Mazeika","ml safety researcher"]; entity["people","Long Phan","ml researcher"]; entity["people","Xuwang Yin","ml researcher"]; Andy Zou; Zifan Wang; entity["people","Norman Mu","ml researcher"]; entity["people","Elham Sakhaee","ml researcher"]; entity["people","Nathaniel Li","ml researcher"]; entity["people","Steven Basart","ml researcher"]; entity["people","Bo Li","ml researcher"]; entity["people","David Forsyth","computer vision researcher"]; entity["people","Dan Hendrycks","ml safety researcher"]. *HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal.* ICML 2024 (PMLR 235). arXiv:2402.04249. citeturn22view0turn17search0

entity["people","Samantha Schulhoff","nlp researcher"]; (and coauthors). *Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs through a Global Prompt Hacking Competition.* EMNLP 2023. citeturn8view0turn23view7

entity["people","Yang Zhang","security researcher"]; (and coauthors). *“Do Anything Now”: Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models.* ACM CCS 2024. citeturn14view0turn23view5turn13search0

entity["people","Jiahao Yu","security researcher"]; entity["people","Xingwei Lin","security researcher"]; entity["people","Zheng Yu","security researcher"]; entity["people","Xinyu Xing","security researcher"]. *GPTFUZZER: Red Teaming Large Language Models with Auto-Generated Jailbreak Prompts.* 2023. arXiv:2309.10253. citeturn13search2turn13search6

entity["people","Cem Anil","ml researcher"]; entity["people","Esin Durmus","ml researcher"]; entity["people","Nina Panickssery","ml researcher"]; (and coauthors). *Many-shot Jailbreaking.* NeurIPS 2024. citeturn29view0turn29view1turn11search2

entity["people","Xiangyu Qi","ml researcher"]; entity["people","Kaixuan Huang","ml researcher"]; entity["people","Ashwinee Panda","ml researcher"]; entity["people","Peter Henderson","ml researcher"]; entity["people","Mengdi Wang","ml researcher"]; entity["people","Prateek Mittal","security researcher"]. *Visual Adversarial Examples Jailbreak Aligned Large Language Models.* 2023 (also appears in AAAI venue listing). arXiv:2306.13213. citeturn12search0turn12search4turn12search20

entity["people","Yichen Gong","ml researcher"]; (and coauthors). *FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts.* arXiv:2311.05608; published in AAAI 2025. citeturn12search1turn12search9turn12search13

entity["people","Yifan Li","nlp researcher"]; entity["people","Hangyu Guo","ml researcher"]; entity["people","Kun Zhou","ml researcher"]; entity["people","Wayne Xin Zhao","nlp researcher"]; entity["people","Ji-Rong Wen","nlp researcher"]. *Images are Achilles’ Heel of Alignment: Exploiting Visual Vulnerabilities for Jailbreaking Multimodal Large Language Models.* arXiv:2403.09792; published at ECCV 2024. citeturn12search2turn3search11

entity["people","Guangke Chen","security researcher"]; entity["people","Fu Song","security researcher"]; entity["people","Zhe Zhao","security researcher"]; Xiaojun Jia; Yang Liu; Yanchen Qiao; Weizhe Zhang; Weiping Tu; Yuhong Yang; Bo Du. *AudioJailbreak: Jailbreak Attacks against End-to-End Large Audio-Language Models.* arXiv:2505.14103 (accepted to IEEE TDSC per arXiv record). citeturn30view1turn31view0

entity["people","Zirui Song","ml researcher"]; entity["people","Qian Jiang","ml researcher"]; (and coauthors). *Audio Jailbreak: An Open Comprehensive Benchmark for Jailbreaking Large Audio-Language Models.* arXiv:2505.15406. citeturn30view2turn3search6

entity["people","Youliang Yuan","nlp researcher"]; entity["people","Wenxiang Jiao","nlp researcher"]; entity["people","Wenxuan Wang","nlp researcher"]; entity["people","Jen-tse Huang","nlp researcher"]; entity["people","Pinjia He","nlp researcher"]; entity["people","Shuming Shi","nlp researcher"]; entity["people","Zhaopeng Tu","nlp researcher"]. *GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher.* ICLR 2024; arXiv:2308.06463. citeturn15search0turn15search7

entity["people","Yue Deng","nlp researcher"]; entity["people","Wenxuan Zhang","nlp researcher"]; entity["people","Sinno Jialin Pan","nlp researcher"]; entity["people","Lidong Bing","nlp researcher"]. *Multilingual Jailbreak Challenges in Large Language Models.* ICLR 2024; arXiv:2310.06474. citeturn4search2turn4search6

entity["people","Zhuoxiong Yong","nlp researcher"]; (and coauthors). *Low-Resource Languages Jailbreak GPT-4.* NeurIPS Workshop (SoLaR) 2023; arXiv:2310.02446. citeturn14view4

entity["people","Fengqing Jiang","security researcher"]; entity["people","Zhangchen Xu","ml researcher"]; entity["people","Luyao Niu","ml researcher"]; entity["people","Zhen Xiang","ml researcher"]; entity["people","Bhaskar Ramasubramanian","ml researcher"]; Bo Li; entity["people","Radha Poovendran","security researcher"]. *ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs.* arXiv:2402.11753; published at ACL 2024. citeturn15search2turn15search5

entity["people","Brian R. Y. Huang","security researcher"]. *Plentiful Jailbreaks with String Compositions.* arXiv:2411.01084. citeturn15search3turn15search14

entity["people","Maksym Andriushchenko","ml researcher"]; (and coauthors). *Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks.* 2025 (preprint). citeturn8view1