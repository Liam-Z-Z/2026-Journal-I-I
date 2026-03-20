# Component 12 — AIGC Detection Methods

- **Section:** §5.1
- **Model:** OpenAI
- **Topic:** AIGC Detection Methods Across All Modalities

---

## Prompt

You are helping me write a section of an academic survey on "Security and Safety of AI-Generated Content." This section (Section 5.1) comprehensively covers detection methods for AI-generated content across all modalities. This is a technical countermeasures section — describe how each method works, its strengths, and its limitations.

Please produce a comprehensive, technically detailed research document covering:

**1. AI-GENERATED TEXT DETECTION**

- Zero-shot / statistical methods:
  - DetectGPT (Mitchell et al., 2023): probability curvature estimation — explain the mechanism (perturbation-based log probability analysis).
  - Fast-DetectGPT: improvements and efficiency gains.
  - DNA-GPT, Binoculars, and other zero-shot approaches.
  - Watermark-based detection (cross-reference to Section 5.2).
- Trained classifiers:
  - RoBERTa-based detectors (OpenAI's original detector — note it was withdrawn).
  - GPTZero: architecture and approach.
  - Turnitin AI detection: deployment scale and reported accuracy.
  - RADAR, Ghostbuster, and other notable classifiers.
- Key challenges:
  - Paraphrase attacks: how paraphrasing evades detection and by how much.
  - Cross-model generalization: detector trained on GPT-3.5 output fails on GPT-4 or Claude output.
  - Multilingual detection: performance degradation on non-English text.
  - Human-AI collaborative text: partial AI assistance is hardest to detect.
  - Detector staleness: performance degrades as new models are released.
  - Short text: detection accuracy on tweets, comments, short paragraphs.
- Benchmarks: RAID, MULTITuDE, M4, HC3 — describe what each evaluates and key findings.

**2. AI-GENERATED IMAGE DETECTION**

- Frequency-domain analysis: GAN spectral artifacts — explain why GANs leave characteristic frequency signatures.
- CNN and ViT-based binary classifiers: UnivFD, CNNDetect, LASTED.
- GAN fingerprinting: each GAN architecture leaves a unique "fingerprint" — how this is exploited for source attribution.
- Diffusion-specific detection:
  - DIRE (Diffusion Reconstruction Error) — explain the mechanism.
  - AEROBLADE and other reconstruction-based methods.
  - Why diffusion model artifacts differ from GAN artifacts.
- Robustness challenges: quantify accuracy drops after JPEG compression, cropping, resizing, social media re-encoding (cite specific numbers).
- The GenAI vs. traditional forensics gap: how generated images differ from manipulated (spliced, inpainted) images.

**3. AUDIO AND VIDEO DETECTION**

- Deepfake speech detection:
  - ASVspoof challenge series (2019, 2021, 2024) — evolution and key findings.
  - Feature categories: spectral features, prosodic features, vocal tract modeling.
  - Codec artifact detection for neural codec model outputs.
- Deepfake video detection:
  - Frame-level detection: analyzing individual frames for artifacts.
  - Video-level detection: temporal consistency analysis, physiological signal detection (blinking, heartbeat).
  - FaceForensics++ benchmark and its successors.
  - ID-unaware vs. ID-aware detection approaches.
- New challenge: diffusion-based video generation (Sora-class models) produces fundamentally different artifacts than face-swap deepfakes — existing detectors may not transfer. Cite early research on this problem.

**4. CROSS-MODAL CHALLENGES AND META-ANALYSIS**

- Common bottlenecks across all modalities: generalization, robustness, interpretability.
- False positive harm: the real-world cost of wrongly accusing human creators of using AI. Cite documented cases.
- The detection vs. generation arms race: why detectors must continuously adapt and are structurally disadvantaged.
- Absence of unified cross-modal detection frameworks: current work is siloed by modality.
- The fundamental asymmetry: detection is harder than generation.

Provide complete references — full paper titles, all author names, publication venues, years, arXiv IDs. Prioritize top venues and include benchmark performance numbers where available.
