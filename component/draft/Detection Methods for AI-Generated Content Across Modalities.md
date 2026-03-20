# [C12] §5.1 Detection Methods for AI-Generated Content Across Modalities

## Scope and threat model

Across modalities (text, images, audio, video), “AI-generated content detection” typically means deciding whether an observed artifact was produced by a generative model (fully or partially) versus a human process (camera capture, human writing, natural speech, or conventional editing). Most deployed detectors are **binary classifiers** (real vs. synthetic), sometimes extended to **proportion estimates** (what fraction is AI), **localization** (which regions/sentences are synthetic), or **source attribution** (which generator family or model produced it). These goals correspond to fundamentally different statistical problems and are often conflated in marketing claims, leading to mismatched expectations in real-world settings. citeturn21view0turn30view3turn40view0turn43search11

A practical threat model must assume **adaptive adversaries**: once a detector’s decision boundary is known (or can be probed), an attacker can modify content (paraphrase text, apply re-encoding, crop/resize, post-process outputs) to push samples toward “human-like” regions. Several benchmark efforts explicitly show that modest changes (sampling settings for text generation, benign image degradations, or adversarial perturbations) can cause large drops in detection fidelity. citeturn21view0turn40view0turn43search11

## AI-generated text detection

### Zero-shot and statistical detectors

**DetectGPT (Mitchell et al., 2023): probability curvature via perturbation-based log-probability analysis.**  
DetectGPT operationalizes the hypothesis that **LM-generated text lies closer to local maxima of the generating model’s probability landscape** than human-authored text. Concretely, given a candidate passage *x*, DetectGPT creates many *perturbations* of *x* (e.g., by replacing tokens/spans using a separate “perturbation model”), and then evaluates the suspected generator’s **log-probability** on the original and perturbed texts. The detector estimates **probability curvature**: if small perturbations systematically *decrease* the generator’s log-probability more strongly (relative to the original), that is evidence the original was sampled from that generator’s high-probability region (a “peak”), consistent with machine generation. This yields a **zero-shot** detector when the suspected generator is available for scoring, because no supervised training on labeled human/AI text is required. citeturn0search3turn21view1

Strengths:
- **No labeled training corpus required** (reduces data collection/labeling burden and mitigates dataset leakage artifacts). citeturn0search3
- **Model-grounded signal**: it directly interrogates the probability geometry of the suspected generator, rather than relying only on surface stylometry. citeturn0search3

Limitations:
- **Requires access to the suspected generator (or a close proxy)** for log-probability scoring; this is difficult against closed or unknown models. citeturn0search3turn21view1
- **Computational cost**: many perturbation-and-score passes are needed; this is a major obstacle at scale. citeturn0search3turn0search4
- **Robustness**: paraphrasing and other post-processing can neutralize the curvature signal, while also changing the distributional match between detector assumptions and observed text. citeturn21view0turn25search6

**Fast-DetectGPT (Bao et al., 2023): efficiency via factorization of curvature approximations.**  
Fast-DetectGPT targets DetectGPT’s bottleneck: repeated decoding/scoring for each perturbation. It provides an efficient approximation of the same curvature-inspired statistic so that the detector can be computed with far fewer model calls. In reported experiments, Fast-DetectGPT achieves large speedups (on the order of hundreds of times faster) while maintaining comparable detection performance in the authors’ settings. citeturn0search4turn21view0

Strengths:
- **Order(s)-of-magnitude faster** inference makes curvature-style detection more feasible in deployment pipelines. citeturn0search4turn21view0

Limitations:
- Still inherits key structural constraints of the curvature approach: reliance on an LM for token-level scoring and sensitivity to distribution shift and editing attacks. citeturn0search4turn21view0

**Binoculars (Hans et al., 2024): two-model “agreement” signals (cross-perplexity style).**  
Binoculars is a zero-shot detector designed to work without the generator’s token probabilities. It computes a statistic built from the behavior of **two related language models** when scoring the same text, using their agreement/disagreement as a cue that the text has been produced by an LM rather than a human process. The paper argues this yields strong zero-shot detection under certain settings and emphasizes calibration/false-positive tradeoffs. citeturn25search9turn21view0turn13view0

Strengths:
- Reduces dependence on direct access to the generator’s logprobs (useful for black-box scenarios). citeturn25search9turn21view1

Limitations:
- Practical robustness can be brittle: in RAID’s robustness testing framework, metric-based detectors (including Binoculars-style methods) can degrade heavily under some adversarial modifications (e.g., synonym swaps) and under decoding changes (e.g., repetition penalty). citeturn21view0turn23view0turn23view2

**DNA-GPT (Yang et al., 2023): divergent n-gram analysis via middle truncation and regeneration.**  
DNA-GPT is a training-free approach that uses an LM as a probe: given a text, it truncates the sequence and uses the prefix to prompt the LM to regenerate successor content, then compares the observed continuation structure to regenerated continuations. Divergence patterns in n-gram statistics (or related similarity metrics) are used as the detection signal. The method is positioned for settings where only plain text is available and token probabilities from the true generator are not. citeturn25search5turn25search1

Strengths:
- **Training-free** (no labeled detector training) and oriented to **black-box** contexts. citeturn25search5

Limitations:
- Requires repeated generation/scoring by a probe model and thus can be **costly** and **sensitive to model mismatch** (if the probe LM differs substantially from the true generator family). citeturn25search5turn21view0

**Watermark-based detection (cross-reference to Section 5.2).**  
Watermark detection is qualitatively different from post-hoc inference: if a generator intentionally embeds a statistical watermark in token choices, detection can be reduced to verifying that secret pattern. However, watermarking requires the generator to cooperate and is vulnerable to paraphrasing/translation and rewriting, so survey treatments usually discuss it as a provenance mechanism rather than a general “catch-all” detector. citeturn21view1turn26view0

### Trained classifiers and commercial detectors

**RoBERTa-style supervised detectors (generic pattern): transformer encoders + classification head.**  
A common baseline is to fine-tune a transformer encoder (e.g., RoBERTa or XLM-R) on labeled human vs machine text. The model learns discriminative features from token sequences and produces a document-level score. In robustness benchmarks, these detectors often show strong in-distribution performance but can be fragile under domain shift, model shift, and adversarial rewriting. RAID explicitly demonstrates strong bias toward the sampling/model distributions observed during detector training, with sharp drops when evaluated on generators outside that distribution. citeturn21view0turn23view3turn26view0

**OpenAI AI Text Classifier (withdrawn): fine-tuned LM classifier with substantial false positives/negatives.**  
entity["company","OpenAI","ai lab, san francisco, us"] released an “AI classifier for indicating AI-written text” on January 31, 2023, then **disabled it on July 20, 2023** citing a “low rate of accuracy.” In OpenAI’s published evaluation on an English “challenge set,” the classifier identified only **26%** of AI-written text as “likely AI-written” (true positives) and incorrectly labeled **9%** of human text as AI-written (false positives), and it was noted as unreliable on short inputs and non-English. citeturn20view0

Mechanism (as described by OpenAI):
- A language model was fine-tuned on paired human-written and AI-written texts on the same topic, with operational thresholds tuned to keep false positives low. citeturn20view0

Deployment takeaways:
- This is a canonical illustration of the **calibration/generalization problem**: the same model family that powers generators is not automatically reliable as a detector, particularly under shift (code, short text, multilingual). citeturn20view0turn21view0

**GPTZero: hierarchical multi-task supervised detection with Human/AI/Mixed outputs.**  
entity["company","GPTZero","ai detection company, us"] describes an industrial detector architecture that explicitly models mixed authorship. The paper presents a **hierarchical, multi-task classification framing**, where the top level includes **Human / AI / Mixed**, and the AI branch further separates subclasses such as “Pure AI,” “Polished” (human-written then AI-polished), and “AI paraphrased,” while also producing sentence-level probabilities via a multi-task objective (document-level CE + sentence-level BCE). The paper stresses robustness via multi-tier automated “red teaming,” while leaving detailed architecture/hyperparameters proprietary. citeturn13view0

Strengths:
- Formalizes a key real-world need: **partial AI assistance** is common; modeling “mixed” explicitly can reduce ambiguity in user interpretation. citeturn13view0
- Provides a conceptual path toward **localization** (sentence-level scoring), improving interpretability relative to purely document-level scores. citeturn13view0

Limitations:
- Proprietary architecture details limit reproducibility and independent assessment, and generalization cannot be assumed in the face of new generator releases without continuous retraining and new data. citeturn13view0turn21view0

**Turnitin AI writing detection: large-scale deployment with thresholding and sentence/document metrics.**  
entity["company","Turnitin","edtech company, oakland, ca, us"] integrates AI-writing indicators into its plagiarism/similarity workflows. Public materials emphasize that detection is not a misconduct verdict but an indicator to support educator judgment. citeturn17view3turn17view2turn19view2

Reported metrics and operational decisions:
- Document-level false positive rate is reported as **<1% for documents with ≥20% AI writing**; sentence-level false positive rate is **~4%** (i.e., a highlighted sentence has ~4% chance of being human-written). citeturn17view0turn14view3
- False positives are disproportionately concentrated near real AI-written regions: Turnitin reports **54%** of false positive sentences occur immediately adjacent to AI-written sentences (a key mixed-authorship failure mode). citeturn17view0turn14view3
- Turnitin’s interface no longer surfaces 1–19% AI scores (displayed as an asterisk without a percentage) to reduce potential harm from low-confidence outputs, and it separates “AI-generated only” from “AI-generated then AI-paraphrased” categories. citeturn17view2turn17view3
- Scale claims: by March 21, 2024, Turnitin reported “over **200 million papers**” reviewed, with **~11%** having ≥20% AI writing and **~3%** having ≥80% AI writing. citeturn19view1turn19view2
- Early public claims at launch-time were more optimistic: a 2023 report quotes Turnitin claiming it identifies ChatGPT/GPT-3 writing **97%** of the time with “<1/100” false positive rate. Subsequent reporting indicates the company later acknowledged higher-than-expected false positives and added caveats for low-percentage outputs. citeturn19view3turn14view3turn17view2

**Ghostbuster (Verma et al., 2024): feature search over weaker LMs + shallow classifier (no target logprobs required).**  
Ghostbuster explicitly aims at black-box detection: it passes documents through a sequence of weaker language models, constructs candidate feature sets from their behaviors, uses a structured search to select features, then fits a lightweight classifier. The paper reports strong cross-domain generalization (including comparison to a RoBERTa baseline) and analyzes robustness to perturbations and paraphrasing, as well as performance on non-native English writers. citeturn21view1turn13view0

Strengths:
- **Black-box applicability**: does not need the target generator’s token probabilities. citeturn21view1
- Emphasizes **generalization** as the primary goal rather than maximizing in-distribution accuracy. citeturn21view1

Limitations:
- Like all supervised detectors, it depends on the diversity of training data and is vulnerable to new generator families and adaptive attacks that change the distribution of cues. citeturn21view0turn21view1

**RADAR (Hu et al., 2023): adversarial learning jointly training paraphraser and detector.**  
RADAR directly targets paraphrase-based evasion by setting up an adversarial game: a paraphraser is trained to produce realistic paraphrases that evade a detector, while the detector is trained to resist. This couples evasion and defense during training rather than treating paraphrasing as a post-hoc attack. citeturn25search2turn25search6

Strengths:
- Produces detectors that are more robust to **LLM-based paraphrasing** under the training assumptions. citeturn25search2turn25search6

Limitations:
- The robustness guarantee is limited to the **attack model class** seen during adversarial training; stronger or different paraphrasers, multi-step editing pipelines, or cross-lingual rewriting can still break generalization. citeturn21view0turn25search6

### Key challenges for text detection

**Paraphrase attacks (and related rewriting attacks) reduce detector reliability.**  
RAID operationalizes paraphrasing using the DIPPER-11B paraphraser (designed explicitly to evade detectors), and shows that certain detectors experience measurable performance drops under paraphrase compared to clean text at the same false-positive operating point. For example, RAID’s Table 16 reports one evaluated detector dropping from **71.0** accuracy (at FPR=5%) on clean data to **52.6** under paraphrase (a **−18.4 point** decrease), while other attacks (e.g., zero-width space insertion) can cause near-collapse in some detectors. citeturn21view0turn23view1turn22view2

A crucial nuance is that “paraphrasing” spans many transformations (human rewriting, LLM rewriting, style transfer, translation + back-translation). Robustness to one paraphraser does not imply robustness to others, motivating adversarial-training approaches such as RADAR but also highlighting ongoing arms-race dynamics. citeturn25search6turn21view0

**Cross-model generalization is weak: detectors overfit to generator families and decoding settings.**  
RAID demonstrates that performance often depends sharply on the generator model and even simple decoding settings. It reports that adding repetition penalties and changing decoding strategies can reduce accuracy by up to **32 points** at a fixed false-positive rate, and that some detectors can deteriorate from near-perfect accuracy to near-failure under relatively modest changes. citeturn23view2turn23view3turn21view0

The same work shows a pronounced “training distribution bias”: a RoBERTa detector trained on one generator achieves **95%+** accuracy on outputs from that generator, yet often fails to exceed **~60%** on text from other models in the same domain. citeturn23view3turn21view0

**Multilingual detection degrades substantially outside English.**  
MULTITuDE reports that detectors trained/tuned primarily on English can fail badly when transferred to other languages, including a cited example where DetectGPT AUC drops from **0.946** to **0.537** when moving from English to German, reinforcing that English-only evaluations are an unreliable proxy for multilingual performance. citeturn24view0

**Human–AI collaborative writing is hardest because signals are localized and transitions are ambiguous.**  
Both GPTZero’s explicit “Mixed” class and Turnitin’s observation that false positives cluster near AI-written regions indicate that **partial AI usage** and **transition boundaries** are especially challenging: detectors may either miss AI-assisted spans (false negatives) or over-attribute adjacent human spans (false positives). citeturn13view0turn17view0turn14view3

**Detector staleness and temporal drift.**  
M4 explicitly evaluates detectors across multiple axes including different generators, domains, languages, and “data generated from different time periods,” emphasizing that detector effectiveness evolves over time and that datasets should grow as new generator families appear. citeturn26view0turn21view0

**Short text remains a major failure mode.**  
OpenAI reports that its withdrawn classifier was “very unreliable” on short texts (<1,000 characters) and recommended English-only use; Turnitin similarly indicates that accuracy improves with more text and uses operational thresholds (e.g., hiding low-percentage scores) to reduce harm. M4 reports that as character length decreases (e.g., from 1,000 to ~125), F1 for detecting machine-generated text decreases across subsets, consistent with the intuition that short samples carry fewer stable statistical cues. citeturn20view0turn17view2turn26view0

### Benchmarks shaping the text-detection landscape

**RAID** evaluates robustness (domain shift, generator shift, decoding strategies, adversarial attacks) at a scale intended to stress detectors beyond curated benchmarks: **6M+ generations**, **11 generators**, **8 domains**, **11 adversarial attacks**, and **4 decoding strategies**. Key findings include strong dependence of accuracy on the target false-positive operating point, large drops under decoding/penalty changes, and attack-specific vulnerabilities (e.g., synonym swaps and invisible-character attacks). citeturn21view0turn23view2turn23view0turn23view1

**MULTITuDE** targets multilingual detection: **74,081** texts in **11 languages**, generated by **8 multilingual LLMs**, and explicitly measures generalization to unseen languages and unseen LLMs. It concludes that multilingual generalization is strongly affected by script/family and that English is an especially poor default training language if multilingual generalization is the goal. citeturn24view0turn24view1

**M4** presents a multi-generator / multi-domain / multilingual benchmark for black-box machine-generated text detection and explicitly studies generalization across domains, generators, languages, and time periods. It reports that detectors often misclassify machine-generated text as human when evaluated on unseen domains or unseen LLMs, emphasizing persistent generalization gaps. citeturn26view0turn24view2

**HC3** (as summarized within M4) is positioned as a human-vs-ChatGPT answer dataset with English and Chinese coverage across multiple domains (e.g., computer science, finance, medicine, law, psychology, open-domain), providing one of the earlier large-scale testbeds for human/ChatGPT discriminability. citeturn26view0turn21view0

## AI-generated image detection

### Frequency-domain analysis: why GANs leave spectral artifacts

A substantial line of work argues that convolutional generators—especially GAN architectures using transposed convolution or related upsampling—fail to reproduce the spectral statistics of natural images, yielding detectable artifacts in Fourier/DCT space. “Watch your Up-Convolution” attributes spectral mismatch to common convolutional upsampling operations and proposes frequency-based analysis for detection. citeturn31search4turn31search1

Similarly, “Leveraging Frequency Analysis for Deep Fake Image Recognition” reports that GAN-generated images exhibit consistent frequency artifacts across architectures/datasets/resolutions and argues these artifacts are structurally induced by upsampling modules used in contemporary GAN pipelines. citeturn31search0turn31search5

However, frequency cues are not a stable guarantee: “Think Twice Before Detecting GAN-Generated Fake Images From Their Spectral Domain Imprints” demonstrates that frequency artifacts can be mitigated via post-processing pipelines, causing sharp decreases in the effectiveness of spectrum-based detectors and warning the community against assuming spectral features are universally robust. citeturn34view3turn31search2

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["GAN frequency spectrum artifacts Fourier domain detection","Watch your up-convolution spectral distributions GAN","Diffusion reconstruction error DIRE visualization"],"num_per_query":1}

### CNN and ViT-based binary classifiers: UnivFD, CNNDetect, LASTED

**CNNDetect / CNNSpot-style detectors (Wang et al., CVPR 2020): “train on one generator, generalize to others.”**  
“CNN-Generated Images Are Surprisingly Easy to Spot… for Now” creates the ForenSynths benchmark (11 CNN generator models spanning diverse tasks, including deepfakes) and demonstrates that a conventional classifier trained on a single generator’s outputs (e.g., ProGAN) can generalize to other CNN-generation methods under careful pre/post-processing. citeturn30view1turn29search5

Strengths:
- Strong empirical evidence that many CNN/GAN generators share *systematic flaws* (at least for the evaluated era of models), enabling cross-model generalization. citeturn29search5turn30view1

Limitations:
- Later work shows severe generalization gaps when moving from GAN-era artifacts to diffusion-era generators (see below), implying that “universal” CNN detectors can be brittle across generator families. citeturn30view3turn34view0

**UnivFD / UniversalFakeDetect (Ojha et al., CVPR 2023): CLIP feature space + nearest neighbor / linear probing.**  
Ojha et al. argue that the standard paradigm “train a deep real-vs-fake classifier” can fail asymmetrically: the “real” class becomes a sink for anything not matching the trained fake patterns, including new generator families. They provide an explicit example where a ProGAN-trained classifier has near-chance performance against diffusion models, with fake accuracy as low as **3.05%** on LDM-generated images (i.e., it labels almost everything “real”). citeturn30view3turn30view0

Their proposed alternative is to **avoid learning a real-vs-fake separator in a narrow training regime**, and instead classify using a feature space not trained specifically for fake detection (e.g., a CLIP ViT encoder trained on internet-scale image-text pairs), using nearest-neighbor or a small linear probe. They report large improvements in generalization to unseen diffusion/autoregressive models (e.g., **+15.05 mAP and +25.90% accuracy** for nearest neighbor, in their evaluation). citeturn30view0turn29search0

Strengths:
- Targets the “sink-class” failure mode directly and emphasizes generalization across generator families. citeturn30view0turn30view3

Limitations:
- Dependence on large pretrained representation spaces raises questions about spurious cues and dataset biases (e.g., compression/resolution mismatches between real and fake sets), which later papers highlight as a major confound. citeturn39search0turn40view0

**LASTED (Wu et al., 2023): language-guided contrastive learning + identification framing.**  
LASTED proposes augmenting training images with carefully designed textual labels and training with joint image-text contrastive learning, then reframing detection as an *identification* problem rather than standard binary classification. The authors report substantial improvements in generalization to unseen generation models (e.g., **+22.66% accuracy and +15.24% AUC** relative to comparators in their reported setting). citeturn32search0turn34view2

Strengths:
- Explicitly exploits multimodal supervision (text labels) to help learn more general forensic features. citeturn32search0turn34view2

Limitations:
- Generalization depends on the diversity and realism of training generators and the stability of learned cues under post-processing and dataset shifts, which benchmarks like GenImage show can be severe. citeturn40view0turn41view0

### GAN fingerprinting and source attribution

Beyond real-vs-fake detection, several works show that generative models leave *model-specific fingerprints* enabling attribution.

- “Do GANs leave artificial fingerprints?” argues that each GAN leaves a unique fingerprint analogous to camera PRNU patterns, enabling source discrimination among GAN architectures. citeturn28search3  
- “Attributing Fake Images to GANs: Learning and Analyzing GAN Fingerprints” trains models to extract and analyze these fingerprints and reports stability/persistence properties enabling attribution. citeturn28search15turn28search11

Strengths:
- Supports forensics workflows beyond binary detection: **which generator produced this image?** citeturn28search15

Limitations:
- Attribution signals can be weakened by post-processing and by the evolution of architectures; minor changes in training can change fingerprints, and diffusion-based generators complicate the “fingerprint” analogy because their generation mechanisms differ. citeturn28search15turn34view0turn30view3

### Diffusion-specific detection: DIRE, AEROBLADE, and reconstruction-error families

Diffusion models differ from GANs in generation dynamics: instead of a single feed-forward generator pass, diffusion typically denoises from noise through iterative refinement (often in latent space for LDMs). This changes which artifacts are most salient, and several papers report that detectors built for GAN artifacts can fail on diffusion outputs. citeturn34view0turn30view3

**DIRE (Wang et al., ICCV 2023): Diffusion Reconstruction Error.**  
DIRE defines an image representation as the difference between an input image and its reconstruction by a pre-trained diffusion model. The core hypothesis is distributional: an image generated by diffusion is “on-manifold” for that diffusion process and can be reconstructed more accurately (low error), whereas a real image, after inversion and reconstruction, is pushed toward the diffusion model’s output distribution and thus reconstructs less faithfully (higher error). A simple classifier trained on DIRE features can then separate real vs diffusion-generated. citeturn34view0turn33search3

Strengths:
- Reported to generalize to unseen diffusion models and be robust to common perturbations, in the authors’ benchmark. citeturn34view0turn33search0

Limitations:
- Requires running an inversion+reconstruction pipeline for each tested image, which is computationally heavier than a single forward pass. citeturn34view0

**AEROBLADE (Ricker et al., CVPR 2024): autoencoder reconstruction error for latent diffusion.**  
AEROBLADE exploits a component specific to latent diffusion models—the autoencoder that maps between image space and latent space. It proposes training-free detection by measuring how accurately an image is reconstructed by a latent diffusion autoencoder (and variants of perceptual distances such as LPIPS). It explicitly evaluates robustness to JPEG compression and center cropping (with resizing), blur, and noise, motivated by social media processing. citeturn34view1turn35view2turn37view0

Strengths:
- **Training-free** deployment (no detector training) while achieving high AP/TPR@5%FPR in the authors’ evaluations across multiple LDM generators. citeturn35view1turn35view3  
- Can be adapted for **qualitative localization** of inpainted regions using reconstruction error maps. citeturn37view0

Limitations:
- Robustness depends on reconstruction distance choice and pre-/post-processing; the authors highlight dataset and storage-format biases (e.g., JPEG-vs-PNG mismatches) that can inadvertently create spurious detection cues. citeturn35view0turn37view0

### Robustness challenges and quantified degradation effects

Empirical evidence strongly suggests that many image detectors are sensitive to degradations that resemble real distribution channels (compression, resizing), which are common in social media reposting and messaging workflows. citeturn40view0turn34view1turn33search10

A particularly explicit quantification comes from the GenImage benchmark paper (NeurIPS 2023 Datasets & Benchmarks), which defines a “degraded image classification” task. After training detectors on a Stable Diffusion subset, the authors report accuracy under degradations such as low resolution and JPEG compression:

- For **ResNet-50**, accuracy drops from **96.2%** at LR(112) to **57.4%** at LR(64), and to **~51.9%** under JPEG(q=65) and **~51.2%** under JPEG(q=30) (near chance), demonstrating drastic sensitivity to compression/resolution shifts. citeturn41view0turn40view0  
- For **GramNet**, accuracy is **68.8%** under JPEG(q=65) and **53.4%** under JPEG(q=30). citeturn41view0turn40view0  
- **CNNSpot** in that evaluation is highly robust to JPEG (97.3% at q=65 and 97.3% at q=30) but fails under low resolution (50.0% at LR(112) and LR(64)), consistent with a detector that has learned robustness primarily for the specific degradations included in its training-time preprocessing (JPEG/blur). citeturn41view0turn40view0

These numbers highlight a deployment reality: “robustness” is often **conditional** on whether the detector was trained with the same degradations it will face at test time; robustness does not automatically transfer across distortion types. citeturn41view0turn21view0

### The GenAI vs. traditional image forensics gap

Traditional manipulation forensics often assumes an underlying camera capture process and looks for inconsistencies introduced by editing: JPEG re-compression traces, sensor noise (PRNU), splicing boundaries, and region-level inconsistencies. Constrained-CNN approaches were proposed to force learned features away from semantic content toward manipulation traces. citeturn27search14

AI-generated images, by contrast, may have **no camera sensor traces**, may be globally “consistent” in compression/noise statistics, and may lack localized boundary artifacts typical of splicing. This shifts the detection problem toward identifying generator-induced statistical patterns (frequency artifacts, reconstruction behavior, representation-space anomalies), and makes direct transfer from classical manipulation detection to AI-generation detection unreliable. citeturn30view3turn34view0turn42search8turn27search14

## Audio and video detection

### Deepfake speech detection

The ASVspoof initiative formalizes spoofed-speech detection as a countermeasure problem for automatic speaker verification (ASV). ASVspoof 2019’s evaluation plan defines two major conditions: **logical access (LA)**—spoofs generated via text-to-speech (TTS) and voice conversion (VC)—and **physical access (PA)**—replay attacks. citeturn42search5turn42search9

ASVspoof 2021 expands the scope. Its evaluation plan describes ASVspoof 2021 as the fourth in a biannual series and specifies three tasks: **LA**, **PA**, and a **deepfake (DF)** task. It notes that LA data includes transmission effects (telephony/VoIP coding and network impacts), and it distinguishes metrics: LA/PA are evaluated in a **tandem** ASV+countermeasure setting (min t-DCF), while DF uses a conventional spoofing metric (EER). citeturn42search6turn42search14turn42search10

By 2024-era community materials, ASVspoof workshops emphasize broader attack variability and explicitly list LA/PA/DF as central tasks, reflecting an evolution from controlled lab speech toward more realistic channels and attacks. citeturn42search11turn42search18

Feature families (typical categories, as reflected in ASVspoof-oriented literature):
- **Spectral representations** capture vocoder/TTS artifacts and channel inconsistencies (e.g., abnormal spectral envelopes, phase/coherence patterns, and codec distortions). These dominate modern countermeasures because most spoof methods introduce frequency-domain anomalies. citeturn42search6turn42search3
- **Prosodic and speaking-style cues** (rhythm, pitch trajectories, segment durations) can reveal unnatural speaking dynamics; however, they are often less reliable in noisy/telephony settings and can be partially corrected by advanced TTS/VC. citeturn42search3turn42search6
- **Vocal-tract and physiology-inspired modeling** tries to detect inconsistencies with human speech production, but such signals can be weak under compression and microphone variability. citeturn42search3turn42search6
- **Codec artifact detection** is increasingly salient because modern spoofing evaluation includes telephony/VoIP effects; detectors can inadvertently or intentionally exploit coding artifacts rather than generator artifacts, complicating interpretation. citeturn42search6turn42search10

### Deepfake video detection: frame cues, temporal cues, and benchmarks

**FaceForensics++** remains a canonical benchmark for facial manipulation detection. It provides large-scale manipulated facial imagery/video derived from multiple manipulation methods (DeepFakes, Face2Face, FaceSwap, NeuralTextures) across compression settings, enabling standardized evaluation and stressing how compression affects both realism and detectability. citeturn42search4turn42search8turn42search16

Detection families:
- **Frame-level detectors** treat each frame as an image classification problem and look for spatial artifacts (blending boundaries, texture inconsistencies, generator fingerprints). This is effective for face-swap pipelines but can ignore temporal coherence and motion cues. citeturn42search8turn43search11
- **Video-level detectors** incorporate temporal consistency. Physiological-signal approaches exploit cues that are hard to synthesize consistently over time:
  - Eye blinking: “In Ictu Oculi” proposes exposing fake face videos by detecting eye blinking patterns as a physiological signal that was poorly reproduced in then-current deepfake generation. citeturn43search5turn43search9  
  - Heart-rate / rPPG: Deepfake detection using remote photoplethysmography (rPPG) analyzes subtle skin color changes induced by blood flow; Hernandez-Ortega et al. propose a knowledge-transfer approach leveraging rPPG/heart-rate features for deepfake detection. citeturn43search4turn43search0

**DFDC (Deepfake Detection Challenge)** and successors broaden deepfake benchmarks beyond FaceForensics++ style manipulations; DFDC preview documentation highlights dataset construction for large-scale deepfake evaluation. citeturn42search12

ID-aware vs. ID-unaware detectors (conceptual distinction): in practice, many deployed detectors are **ID-unaware**, aiming to generalize across identities and focusing on manipulation traces rather than person-specific priors. Some research explores **ID-aware** framing (specializing detectors by subject or using identity consistency constraints), but surveys emphasize that identity dependence can harm transferability and fairness. citeturn43search15turn42search8

### New challenge: diffusion-based video generation and transfer failure from face-swap detectors

Diffusion-based or large-scale learned video generation (text-to-video and image-to-video) produces synthetic videos that are **not** simply face-swap manipulations; instead, the entire frame sequence may be generated with coherent motion priors. This changes the artifact landscape, and multiple sources suggest that detectors built for images or face-swaps may not transfer.

- “Beyond Deepfake Images: Detecting AI-Generated Videos” reports that synthetic image detectors do **not** reliably detect synthetic videos and argues this failure is not merely due to H.264 compression; rather, video generators leave distinct traces not captured by image detectors. citeturn43search11
- A 2026 training-free approach (STALL) explicitly motivates itself by stating that per-frame (image-based) detectors are fundamentally limited because they ignore temporal dynamics, and supervised video detectors generalize poorly to unseen generators. It introduces likelihood-based scoring over spatial and temporal evidence and proposes a new benchmark (ComGenVid) containing state-of-the-art generators. citeturn43search2turn43search6
- Institutional research communications (e.g., Columbia Engineering) describe diffusion-video detection tools (DIVID), suggesting ongoing early-stage efforts to build diffusion-video-specific detectors. citeturn43search7

Collectively, these sources support a key meta-point for modern “Sora-class” generation: **detection signals are modality- and generator-family-specific**, so detectors anchored in face swapping and frame artifacts can fail on fully generated videos with learned temporal priors, requiring explicitly spatiotemporal detection signals. citeturn43search11turn43search2

## Cross-modal challenges and meta-analysis

### Shared bottlenecks across modalities

Across text, image, audio, and video, the dominant bottlenecks converge on the same triad:

**Generalization**: detectors trained/tuned on one generator family or distribution often fail on new models or domains. This is quantified in text (RAID) and images (UnivFD’s GAN-to-diffusion collapse; GenImage cross-generator tasks) and is asserted as central in video detection work emphasizing unseen generators. citeturn21view0turn30view3turn40view0turn43search2

**Robustness to benign processing**: compression, resizing, and formatting shifts can drive detectors toward chance-level behavior, as shown in GenImage’s degraded-image results for JPEG and resolution changes and in Turnitin/OpenAI’s operational cautions for low-confidence ranges and short texts. citeturn41view0turn17view2turn20view0turn43search11

**Interpretability and localization**: users need actionable explanations (which spans/regions drive a decision). GPTZero emphasizes sentence-level predictions and mixed authorship; AEROBLADE uses reconstruction-error maps that can highlight inpainted regions; physiological video detectors give interpretable cues (blink or rPPG inconsistencies). Yet interpretability remains inconsistent across systems, particularly for black-box commercial detectors. citeturn13view0turn37view0turn43search5turn43search4

### False positive harm and real-world costs

False positives have concrete harms: wrongful accusations of academic misconduct or misinformation amplification can result from treating detector scores as authoritative.

- entity["company","Turnitin","edtech company, oakland, ca, us"]’s own documentation highlights that false positives exist, provides explicit sentence-level false positive estimates (~4%), and changed product behavior to suppress low (1–19%) AI-percentage outputs to avoid adverse consequences. citeturn17view0turn17view2
- Independent reporting notes Turnitin acknowledged higher-than-expected false positives relative to earlier claims and emphasizes that mixed human/AI transitions are especially error-prone, which is precisely the scenario most common in real classroom use (editing, polishing, partial assistance). citeturn14view3turn17view0
- entity["company","OpenAI","ai lab, san francisco, us"] similarly warns that its classifier should not be used as a primary decision tool and reports non-trivial false positives (9%) in its own evaluation, coupled with poor short-text and non-English reliability—conditions common in real-world writing. citeturn20view0

### Detection vs. generation arms race and structural asymmetry

Detectors are structurally disadvantaged because generators can:
- Change sampling/decoding parameters (text), apply post-processing filters (images), or add channel effects (audio/video) cheaply, while detectors must remain robust across all these perturbations. RAID shows substantial drops from simple settings like repetition penalties and from adversarial attacks such as invisible-character insertion, underscoring how cheaply an attacker can shift distributions. citeturn21view0turn23view2turn23view1
- Rewrite outputs to evade detection: OpenAI explicitly states its classifier can be evaded by editing and that it is unclear whether detection has a long-term advantage. citeturn20view0
- Move to new generator families (GAN → diffusion → video diffusion), where older detectors may fail catastrophically (e.g., GAN-trained image detectors labeling diffusion outputs as real; image detectors failing on synthetic videos). citeturn30view3turn43search11

### Siloing and the absence of unified cross-modal frameworks

Research is still largely siloed by modality: text detection relies on LM probability geometry and stylometry; image detection often uses representation-space or reconstruction cues; audio detection is shaped by ASVspoof tasks and channel effects; video detection increasingly stresses spatiotemporal likelihoods. Surveys and workshop materials emphasize that each modality has distinct artifact mechanisms and benchmark ecosystems, complicating a unified “one detector for all media” approach. citeturn27search3turn43search15turn42search11turn43search2

## References

```bibtex
Mitchell, Edward J.; Lee, Yoonho; Khazatsky, Alexander; Manning, Christopher D.; Finn, Chelsea.
“DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.”
arXiv preprint arXiv:2301.11305, 2023.

Bao, Liangzhen; Wang, Huan; (et al.).
“Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.”
arXiv preprint arXiv:2310.05130, 2023.

Hans, Abhimanyu; Schwarzschild, Avi; Cherepanova, Valeriia; Kazemi, Hamid; Saha, Aniruddha; Goldblum, Micah; Geiping, Jonas; Goldstein, Tom.
“Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text.”
arXiv preprint arXiv:2401.12070, 2024.

Yang, Xuhui; (et al.).
“DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.”
arXiv preprint arXiv:2305.17359, 2023.

Verma, Vivek; Fleisig, Eve; Tomlin, Nicholas; Klein, Dan.
“Ghostbuster: Detecting Text Ghostwritten by Large Language Models.”
arXiv/UC Berkeley technical report (public PDF), 2024.

Hu, Xiaomeng; Chen, Pin-Yu; Ho, Tsung-Yi.
“RADAR: Robust AI-Text Detection via Adversarial Learning.”
NeurIPS 2023; arXiv preprint arXiv:2307.03838, 2023.

Dugan, Liam; Hwang, Alyssa; Trhlik, Filip; Ludan, Josh Magnus; Zhu, Andrew; Xu, Hainiu; Ippolito, Daphne; Callison-Burch, Chris.
“RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors.”
arXiv preprint arXiv:2405.07940, 2024.

Macko, Dominik; Moro, Robert; Uchendu, Adaku; Lucas, Jason Samuel; Yamashita, Michiharu; Pikuliak, Matúš; Srba, Ivan; Le, Thai; Lee, Dongwon; Simko, Jakub; Bielikova, Maria.
“MULTITuDE: Large-Scale Multilingual Machine-Generated Text Detection Benchmark.”
Proceedings of EMNLP 2023; arXiv preprint arXiv:2310.13606, 2023.

Wang, Yuxia; Mansurov, Jonibek; Ivanov, Petar; Su, Jinyan; Shelmanov, Artem; Tsvigun, Akim; Whitehouse, Chenxi; Afzal, Osama Mohammed; Mahmoud, Tarek; Sasaki, Toru; Arnold, Thomas; Aji, Alham Fikri; Habash, Nizar; Gurevych, Iryna; Nakov, Preslav.
“M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection.”
arXiv preprint arXiv:2305.14902 (v2: 2024), 2023–2024.

Adam, George Alexandru; Cui, Alexander; Thomas, Edwin; Napier, Emily; Shmatko, Nazar; Schnell, Jacob; Tian, Jacob Junqi; Dronavalli, Alekhya; Tian, Edward; Lee, Dongwon.
“GPTZero: Robust Detection of LLM-Generated Texts.”
arXiv preprint arXiv:2602.13042, 2026.

OpenAI.
“New AI classifier for indicating AI-written text.”
OpenAI product post (discontinued July 20, 2023), 2023.

Chechitelli, Annie; Turnitin.
“Turnitin marks one year anniversary of its AI writing detector with millions of papers reviewed globally.”
Press release (PRNewswire), 2024.

Durall, Ricard; Keuper, Margret; Keuper, Janis.
“Watch your Up-Convolution: CNN Based Generative Deep Neural Networks are Failing to Reproduce Spectral Distributions.”
CVPR 2020; arXiv preprint arXiv:2003.01826, 2020.

Frank, Joel; Eisenhofer, Thorsten; Schönherr, Lea; Fischer, Asja; Kolossa, Dorothea; Holz, Thorsten.
“Leveraging Frequency Analysis for Deep Fake Image Recognition.”
ICML 2020 workshop proceedings (PMLR); arXiv preprint arXiv:2003.08685, 2020.

Dong, Cheng; (et al.).
“Think Twice Before Detecting GAN-Generated Fake Images From Their Spectral Domain Imprints.”
CVPR 2022, 2022.

Wang, Sheng-Yu; Wang, Oliver; Zhang, Richard; Owens, Andrew; Efros, Alexei A.
“CNN-Generated Images Are Surprisingly Easy to Spot… for Now.”
CVPR 2020; arXiv preprint arXiv:1912.11035, 2019–2020.

Ojha, Utkarsh; Li, Yuheng; Lee, Yong Jae.
“Towards Universal Fake Image Detectors That Generalize Across Generative Models.”
CVPR 2023; arXiv preprint arXiv:2302.10174, 2023.

Wu, Haiwei; Zhou, Jiantao; Zhang, Shile.
“Generalizable Synthetic Image Detection via Language-guided Contrastive Learning.”
arXiv preprint arXiv:2305.13800, 2023.

Marra, Francesco; Gragnaniello, Diego; Cozzolino, Davide; Verdoliva, Luisa.
“Do GANs leave artificial fingerprints?”
arXiv preprint arXiv:1812.11842, 2018.

Yu, Ning; Davis, Larry; Fritz, Mario.
“Attributing Fake Images to GANs: Learning and Analyzing GAN Fingerprints.”
ICCV 2019, 2019.

Wang, Zhendong; Bao, Jianmin; Zhou, Wengang; Wang, Weilun; Hu, Hezhen; Chen, Hong; Li, Houqiang.
“DIRE for Diffusion-Generated Image Detection.”
ICCV 2023; arXiv preprint arXiv:2303.09295, 2023.

Ricker, Jonas; Lukovnikov, Denis; Scharfenberger, Christian; (et al.).
“AEROBLADE: Training-Free Detection of Latent Diffusion Images Using Autoencoder Reconstruction Error.”
CVPR 2024; arXiv preprint arXiv:2401.17879, 2024.

Zhu, Ming; (et al.).
“A Million-Scale Benchmark for Detecting AI-Generated Image (GenImage).”
NeurIPS 2023 Datasets and Benchmarks Track (OpenReview), 2023.

Delgado, Héctor; (et al.).
“ASVspoof 2021 Evaluation Plan.”
arXiv preprint arXiv:2109.00535; ASVspoof initiative technical plan, 2021.

ASVspoof initiative.
“ASVspoof 2019 Evaluation Plan.”
ASVspoof initiative technical plan, 2019.

Li, Yuezun; Chang, Ming-Ching; Lyu, Siwei.
“In Ictu Oculi: Exposing AI Created Fake Videos by Detecting Eye Blinking.”
WIFS 2018; arXiv preprint arXiv:1806.02877, 2018.

Hernandez-Ortega, Javier; (et al.).
“DeepFakes Detection based on Heart Rate Estimation.”
CEUR Workshop Proceedings (paper PDF), 2021.

Rössler, Andreas; Cozzolino, Davide; Verdoliva, Luisa; Riess, Christian; Thies, Justus; Nießner, Matthias.
“FaceForensics++: Learning to Detect Manipulated Facial Images.”
ICCV 2019; arXiv preprint arXiv:1901.08971, 2019.

Dolhansky, Brian; Howes, Russ; Pflaum, Ben; Baram, Nicole; Canton Ferrer, Cristian.
“The Deepfake Detection Challenge (DFDC) Preview Dataset.”
arXiv preprint arXiv:1910.08854, 2019.

Ben Hayun, Omer; Betser, Roy; Levi, Meir Yossef; Kassel, Levi; Gilboa, Guy.
“Training-free Detection of Generated Videos via Spatial-Temporal Likelihoods (STALL).”
arXiv preprint arXiv:2603.15026, 2026.

“Beyond Deepfake Images: Detecting AI-Generated Videos.”
arXiv HTML (preprint), 2024.
```