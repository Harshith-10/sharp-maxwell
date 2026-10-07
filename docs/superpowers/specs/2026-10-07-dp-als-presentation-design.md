# DP-ALS Research Paper Presentation: Design Specification

**Topic:** Presentation for Research Paper: *Shifting from One-Time Education to Continuous Growth: A Dual-Process Cognitive Architecture Integrating System One Decision Models and Generative Socratic Tutors for Adaptive Lifelong Learning*  
**Authors:** Harshith D., Aman Goud D., Surya Teja P., and Ramya N. (Department of Computer Science and Engineering, Institute of Aeronautical Engineering, Hyderabad, India)  
**Date:** 2026-10-07  
**Design Template:** Stencil & Tablet (`frontend-slides/bold-template-pack/templates/stencil-tablet`)  
**Output Target:** Standalone HTML presentation (`presentation.html` / `dp-als-presentation.html`)

---

## 1. Executive Summary & Goals

The goal of this presentation is to deliver a comprehensive, high-density, reading-first seminar lecture deck covering the theoretical, mathematical, architectural, and empirical findings of the DP-ALS research paper. The presentation leverages the **Stencil & Tablet** aesthetic—an archival, tactile, industrial-poster design system featuring Stardos Stencil display typography, Barlow Condensed heavy chrome, Inter body copy, and a saturated retro-print earth palette against bone and black fields.

The deck integrates:
- All core cognitive theories (Dual-Process Theory, Cognitive Load Theory, Flow Theory).
- Exact mathematical formulations rendered via KaTeX (Telemetry vector, POMDP latent belief state, productive struggle index, System One objective function).
- Systems architecture diagrams and Algorithm 1 coordination loop.
- High-fidelity visual embeddings of `fig_telemetry.png` (time-series trace) and `fig_benchmarks.png` (empirical benchmarks).
- Full comparative matrix across 4 architectures.
- Washington Accord (WK2–WK9, PO1–PO11) and UN Sustainable Development Goals (SDG 4, 8, 9, 10) alignment.

---

## 2. Visual & Architectural System: Stencil & Tablet

### 2.1 Color Palette
- `--color-bone`: `#E2DCC9` (Default page field for content and analytical slides)
- `--color-black`: `#000000` (Dark canvas for cover, section transitions, and quantitative hero slides)
- `--color-ink`: `#0A0A0A` (Near-black text on light surfaces)
- `--color-paper`: `#F4EFE0` (Lighter cream for tables, timelines, and diagram frames)
- `--color-sienna`: `#A06A3C` (Earthy brown-orange accent)
- `--color-magenta`: `#C73B7A` (Saturated retro pink-red accent)
- `--color-orange`: `#EE7A2E` (Signature vibrant accent)
- `--color-teal`: `#2D7E73` (Cool counterpart accent)
- `--color-blue`: `#3F73B7` (Process blue accent)
- `--color-mustard`: `#D8A93B` (Action bars and status callouts)
- `--color-olive`: `#6F7A2E` (Secondary accent)

### 2.2 Typography Scale
- **Display Headlines & Numerals:** `Stardos Stencil, serif` (Weight 700, All Uppercase, characteristic ink breaks).
  - Cover Hero: `120px`–`140px`
  - Section / Page Headlines: `68px`–`88px`
  - Tablet Mega Numerals: `140px`–`220px`
  - Card Titles: `28px`–`34px`
- **Metadata, Chrome, & Pills:** `Barlow Condensed, sans-serif` (Weight 600–900, All Uppercase, tracking `0.06em`–`0.14em`).
  - Topbar labels: `28px`–`32px`
  - Footer chrome: `20px`–`22px`
  - Status pills: `18px` (999px border radius)
- **Body & Prose:** `Inter, sans-serif` (Weight 400–500, Sentence Case, size `18px`–`22px`, line-height `1.45`).
- **Mathematical Rendering:** KaTeX CDN integration (`katex.min.css`, `katex.min.js`, `auto-render.min.js`) with configured delimiters for inline `$...$` / `\(...\)` and display `$$...$$` / `\[...\]`.

### 2.3 Canvas & Fixed-Stage Scaling
- Fixed 16:9 canvas authored at `1920×1080` inside `.deck-stage`.
- Scaled uniformly using `transform: translate(x, y) scale(factor)` where `factor = Math.min(innerWidth / 1920, innerHeight / 1080)`.
- Letterboxing/pillarboxing preserves geometric integrity on any screen or viewport.
- Slide navigation controlled via keyboard (`ArrowLeft`, `ArrowRight`, `Space`, `PageUp`, `PageDown`), touch swipe gestures, and direct slide indicators.
- Built-in inline editing enabled via top-left hotzone or pressing `E`.

---

## 3. Slide Deck Specification (14 Slides)

### Slide 01: Cover / Title
- **Background:** Black (`#000000`), Text: Bone (`#E2DCC9`).
- **Header Eyebrow:** `IARE CSE RESEARCH SEMINAR • DUAL-PROCESS COGNITIVE ARCHITECTURE`
- **Main Title:** `SHIFTING FROM ONE-TIME EDUCATION TO CONTINUOUS GROWTH`
- **Subtitle:** `A Dual-Process Cognitive Architecture Integrating System One Decision Models and Generative Socratic Tutors for Adaptive Lifelong Learning`
- **Cover Lockup:** 56px orange accent mark, author list (Harshith D., Aman Goud D., Surya Teja P., Ramya N.), Department of Computer Science & Engineering, Institute of Aeronautical Engineering, Hyderabad.

### Slide 02: The Structural Crisis: Accelerated Skill Decay
- **Background:** Bone (`#E2DCC9`).
- **Eyebrow & Headline:** `01. MOTIVATION / THE SKILL HALF-LIFE CRISIS`
- **Layout:** 3-column tablet cards:
  1. *Sienna Tablet (Numeral `2.5` yr):* Rapid Skill Obsolescence. In IT and data sectors, skill half-life has shrunk to 2.5–5.0 years.
  2. *Orange Tablet (Numeral `40` yr):* Episodic Front-Loaded Credentialing. Traditional degrees front-load learning at ages 18–25 for a 40-year career with zero continuous adaptation.
  3. *Mustard Tablet (Numeral `04` SDGs):* Systemic Educational Disconnect. Violates UN SDGs 4, 8, 9, and 10; causing workforce dislocation and widening socio-economic inequality.

### Slide 03: The Intelligent Tutoring Dilemma
- **Background:** Bone (`#E2DCC9`).
- **Top Callout:** Mustard Action Bar: `PEDAGOGICAL BOTTLENECK • CLASSICAL DETERMINISM VS. GENERATIVE OVER-ASSISTANCE`
- **Layout:** 2 large comparison tablets:
  1. *Teal Tablet (Classical Rule-Based ITS / BKT):* Bayesian Knowledge Tracing & IRT operate at low latency (<50ms) but rely on brittle heuristics, lack semantic synthesis, and fail to provide personalized metaphors.
  2. *Magenta Tablet (Monolithic Generative LLM Tutors):* Transformer LLMs support rich Socratic reasoning, but suffer high latency (0.42s–700s), prohibitive token costs (48.2k tokens/h), and over-explanation that prematurely halts productive struggle and breaks cognitive flow.

### Slide 04: Theoretical Foundation: Dual-Process Cognitive Architecture
- **Background:** Black (`#000000`), Text: Bone.
- **Eyebrow & Headline:** `02. THEORY / KAHNEMAN'S DUAL-PROCESS COGNITION IN PEDAGOGY`
- **Layout:** 2 giant contrasting tablets:
  1. *Orange Tablet (Numeral `01` — System One):* Fast, autonomous, reactive reflex engine. Operates at sub-40ms latency, continuously parsing learner micro-telemetry (keystrokes, timing, scroll jitter) without interrupting immersion.
  2. *Teal Tablet (Numeral `02` — System Two):* Slow, deliberate, asynchronous Socratic tutor. Engaged selectively only when an impasse is mathematically confirmed or deep conceptual remediation is necessary.
- **Bottom Callout:** The Human Expert Analogy: An expert human teacher does not deliberate over every gesture—they react reflexively and deliberate only upon true student impasse.

### Slide 05: System One Reflex Engine: Edge Decision Head
- **Background:** Bone (`#E2DCC9`).
- **Eyebrow & Headline:** `03. ARCHITECTURE / SYSTEM ONE DECISION HEAD`
- **Layout:** 3 structured technical cards:
  1. *Card 1 (Model Selection & Edge Deployment):* Fastino 340M-parameter GLiNER2.5-Decide open-weight encoder. Deployed near the learner for ultra-low latency.
  2. *Card 2 (Non-Autoregressive Single Pass):* Takes serialized telemetry vector and typed schema questions, returning structured decision probabilities and confidence scores without token-by-token generation overhead.
  3. *Card 3 (Latency Performance & Hardware Targets):* Target $<40\text{ ms}$. Benchmark results: $38.3\text{ ms}$ (V100 GPU), $43\text{–}47\text{ ms}$ (T4/L4/A100), simulated end-to-end round trip $28.4 \pm 4.2\text{ ms}$.

### Slide 06: Mathematical Formulation: POMDP & State Space
- **Background:** Bone (`#E2DCC9`).
- **Eyebrow & Headline:** `04. MATHEMATICS / LATENT COGNITIVE STATE & POMDP FILTERING`
- **Layout:** 2 analytical panels featuring live KaTeX rendered formulas:
  1. *Panel 1: Telemetry Vector & Latent State Space:*
     - Telemetry: $x_t = [\Delta\tau_k,\, H_k,\, \sigma_{\text{scroll}},\, e_{\text{syntax}},\, t_{\text{dwell}},\, r_{\text{churn}}]^T \in \mathbb{R}^d$
     - Latent State: $s_t = [C_t,\, F_t,\, M_t,\, P_t]^T \in [0, 1]^3 \times [-1, 1]$
  2. *Panel 2: Bayesian Belief Update & Struggle Index:*
     - POMDP Belief: $b(s_t) \propto P(x_t \mid s_t) \int_{\mathcal{S}} \mathcal{T}(s_t \mid s_{t-1}, a_{t-1})\, b(s_{t-1})\, ds_{t-1}$
     - Productive Struggle: $P_t = \tanh\left(\omega_1 M_t - \omega_2 (C_t - C^*)\right)$, with optimal challenge zone $C^* \approx 0.65$.

### Slide 07: Discrete Action Space & Optimization Objective
- **Background:** Bone (`#E2DCC9`).
- **Eyebrow & Headline:** `05. POLICY / 5 DISCRETE ACTIONS & REWARD OPTIMIZATION`
- **Layout:** 5 process cards for actions $\mathcal{A} = \{a_0, a_1, a_2, a_3, a_4\}$ plus bottom Objective Card:
  - $a_0$: Passive Flow (zero UI disruption, learner in flow)
  - $a_1$: Ambient Nudge (subtle non-blocking syntax/typo highlight)
  - $a_2$: IRT Adaptation (calibrating next problem difficulty to ability $\hat{\theta}_t$)
  - $a_3$: Dispatch System Two (asynchronous Socratic LLM RPC)
  - $a_4$: Cognitive Rest (micro-pause / spaced repetition retrieval)
- **Objective Card:** KaTeX formula for cumulative return:
  $$J(\pi_{\text{System One}}) = \mathbb{E}\left[\sum_{t=0}^T \gamma^t (\Delta M_t + \alpha_1 F_t) - \lambda \mathbf{1}_{\{a_t=a_3\}} \Phi_{\text{cost}} - \alpha_2 D_t\right]$$

### Slide 08: Cyber-Physical Architecture & Algorithm 1
- **Background:** Black (`#000000`), Text: Bone.
- **Eyebrow & Headline:** `06. PIPELINE / END-TO-END TELEMETRY & ALGORITHM 1`
- **Layout:** 3-stage pipeline cards + Algorithm 1 priority execution flow:
  1. *Stage 1: Client Telemetry Worker (50ms):* Privacy-first JS worker computing statistical entropy, timing offsets, and scroll accelerations. Zero keystrokes stored.
  2. *Stage 2: Edge WebSocket Gateway:* 26-byte binary payload ($0.56\text{ KB/s}$), sub-40ms POMDP belief update and micro-nudge return.
  3. *Stage 3: Async Socratic Dispatch:* Cooldown timer $T_{\text{cool}}$ and pending lock prevents request flooding while LLM is generating.

### Slide 09: Real-Time Telemetry in Action (`fig_telemetry.png`)
- **Background:** Bone (`#E2DCC9`).
- **Eyebrow & Headline:** `07. VISUAL TRACE / REAL-TIME COGNITIVE LOAD & FLOW SESSION`
- **Layout:** Two-column split:
  - *Left (60% width):* Crisp embedded `fig_telemetry.png` inside a paper matte card.
  - *Right (40% width):* 2 annotation tablets:
    - *Teal Tablet:* Micro-nudge phase ($t < 180\text{s}$). System One tracks $C_t$ and $F_t$, deploying actions $a_1$ and $a_2$ to keep struggle productive without interrupting flow.
    - *Orange Tablet:* Socratic Dispatch ($t \approx 210\text{s}$). When cognitive load breaches threshold $\tau_{\text{impasse}} = 0.75$, action $a_3$ fires once, routing diagnostic context to System Two.

### Slide 10: System Two Socratic Remediation & Skill Passport
- **Background:** Bone (`#E2DCC9`).
- **Eyebrow & Headline:** `08. REMEDIATION / SOCRATIC CONTEXT INJECTION & SKILL PASSPORT`
- **Layout:** 2 deep cards (Magenta & Blue):
  1. *Magenta Card (System Two Prompt Template):* Appendix B structured injection: Learner Profile, Target Competency (e.g. Dijkstra, WK3/PO1), State diagnostics ($C_t = 0.82$, $F_t = 0.12$, $P_t = -0.65$), Directive: *Do NOT provide solution code; formulate a 2-sentence Socratic analogy grounded in logistics routing.*
  2. *Blue Card (Lifelong Graph & Skill Passport):* Immutable, graph-based competency tracking with spaced decay functions, awarding micro-credentials mapped to Washington Accord competencies.

### Slide 11: Empirical Benchmarks: 10,000 Learners (`fig_benchmarks.png`)
- **Background:** Black (`#000000`), Text: Bone.
- **Eyebrow & Headline:** `09. RESULTS / MONTE CARLO BENCHMARKS ACROSS 10,000 LEARNERS`
- **Layout:** Top half: embedded `fig_benchmarks.png`; Bottom half: 4 massive Stencil stat tablets:
  1. *Orange Tablet:* `-61.6%` Time-to-Mastery ($18.6\text{ h}$ vs. $48.5\text{ h}$ static)
  2. *Teal Tablet:* `-85.3%` Cognitive Impasse ($6.2\%$ vs. $42.1\%$ static, $19.5\%$ LLM)
  3. *Mustard Tablet:* `-84.6%` Token Consumption ($7,400$ vs. $48,200\text{ tokens/h}$)
  4. *Magenta Tablet:* `78.9%` Flow Preservation (vs. $31.4\%$ static, $52.1\%$ LLM)

### Slide 12: Architecture Comparison Matrix
- **Background:** Bone (`#E2DCC9`).
- **Eyebrow & Headline:** `10. COMPARISON / ARCHITECTURE BENCHMARK MATRIX`
- **Layout:** Stencil & Tablet paper card matrix table featuring Table I data with authentic status pills:
  - Columns: Architecture, Time-to-Mastery (TTM), Impasse Rate, LLM Tokens / Hour, Flow Preservation.
  - Rows:
    - *Static Curriculum:* 48.5 h | 42.1% (Magenta Pill) | 0 tokens (Teal Pill) | 31.4% (Magenta Pill)
    - *Rule-Based ITS (BKT/IRT):* 39.2 h | 31.8% (Mustard Pill) | 120 tokens (Teal Pill) | 44.6% (Mustard Pill)
    - *LLM-Only (System Two):* 28.4 h | 19.5% (Mustard Pill) | 48,200 tokens (Magenta Pill) | 52.1% (Mustard Pill)
    - *DP-ALS (Ours):* 18.6 h (Teal Pill) | 6.2% (Teal Pill) | 7,400 tokens (Teal Pill) | 78.9% (Teal Pill)

### Slide 13: Accreditation & Global Standards Alignment
- **Background:** Bone (`#E2DCC9`).
- **Eyebrow & Headline:** `11. ACCREDITATION / UN SDGS & WASHINGTON ACCORD MAPPING`
- **Layout:** 2 wide tablet cards:
  1. *Orange Tablet (UN Sustainable Development Goals):*
     - SDG 4 (Quality & Lifelong Education): Inclusive adaptive pacing across age cohorts.
     - SDG 8 (Decent Work): Rapid workforce reskilling matching technical skill half-lives.
     - SDG 9 (Sustainable AI Infrastructure): 84.6% compute reduction supporting green AI.
     - SDG 10 (Reduced Inequalities): 0.56 KB/s low-bandwidth telemetry for constrained links.
  2. *Teal Tablet (Washington Accord & IEA Graduate Attributes):*
     - WK2 / PO1, PO2: POMDP mathematical filtering and cognitive modeling.
     - WK3, WK5 / PO3: Dual-process systems engineering and resource-efficient architecture.
     - WK6, WK7 / PO5, PO6: Edge inference, streaming telemetry, societal impact.
     - WK9 / PO7, PO11: GDPR/FERPA client privacy and lifelong Skill Passport.

### Slide 14: Conclusion & Pedagogical Horizons
- **Background:** Black (`#000000`), Text: Bone.
- **Eyebrow & Headline:** `12. CONCLUSION / TOWARD CONTINUOUS LIFELONG GROWTH`
- **Layout:** 3 tablet cards + bottom conference closing lockup:
  1. *Tablet 1 (Core Takeaway):* Resolving the ITS dichotomy by unifying low-latency edge reflex models with generative Socratic reasoning.
  2. *Tablet 2 (Future Frontiers):* On-device neuromorphic System 1 deployments, federated cross-institution telemetry aggregation, cohort fairness audits.
  3. *Tablet 3 (Lifelong Horizon):* Shifting institutional education from front-loaded static degrees to dynamic, verified Skill Passports.

---

## 4. Quality & Verification Gates
- [x] Fixed 16:9 1920×1080 stage with zero content reflow across viewports.
- [x] Complete inline CSS & JS in a single HTML file.
- [x] KaTeX CDN inclusion and script loading with auto-render.
- [x] Local image assets (`fig_telemetry.png`, `fig_benchmarks.png`) properly framed and unclipped.
- [x] Full keyboard navigation, touch support, and inline editing (`E` key / hover).
- [x] Zero metadata/debug text on slide faces.
