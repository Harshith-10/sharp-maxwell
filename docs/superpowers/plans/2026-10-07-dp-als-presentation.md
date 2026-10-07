# DP-ALS Presentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a 14-slide standalone HTML presentation (`presentation.html`) for the research paper *Shifting from One-Time Education to Continuous Growth: A Dual-Process Cognitive Architecture Integrating System One Decision Models and Generative Socratic Tutors for Adaptive Lifelong Learning* using the Stencil & Tablet design system, fixed 1920×1080 stage architecture, KaTeX mathematical typesetting, and embedded high-resolution figures.

**Architecture:** Single zero-dependency HTML file containing inline CSS and JavaScript. Includes `viewport-base.css` fixed 16:9 stage scaling (`deckStage`), keyboard/touch navigation, Stencil & Tablet theme tokens (Stardos Stencil display, Barlow Condensed chrome, Inter body, saturated retro-print palette on bone/black), KaTeX CDN for mathematical typesetting, and embedded local images (`fig_telemetry.png`, `fig_benchmarks.png`).

**Tech Stack:** HTML5, CSS3, ES6 JavaScript, Google Fonts (Stardos Stencil, Barlow Condensed, Inter), KaTeX (v0.16.9 CDN), Local PNG assets.

**Spec:** [`docs/superpowers/specs/2026-10-07-dp-als-presentation-design.md`](file:///home/harshu/Documents/antigravity/sharp-maxwell/docs/superpowers/specs/2026-10-07-dp-als-presentation-design.md)

## Global Constraints

- Standalone single-file HTML delivery (`presentation.html`) with all styling and controller scripts inline.
- Authored at fixed 1920×1080 canvas size, scaled uniformly to browser viewport with zero content reflow or mobile layout wrapping.
- Complete inclusion of `viewport-base.css` with `.slide.active` / `.slide.visible` opacity/visibility management.
- Authentic Stencil & Tablet design: Stardos Stencil (700, uppercase) for all headlines and numerals; Barlow Condensed (600–900, uppercase, tracking `0.06em`–`0.14em`) for chrome, pills, and metadata; Inter (sentence case) for body copy.
- Math equations must render through KaTeX (`$...$` inline, `$$...$$` display).
- Image paths must point directly to local assets: `fig_telemetry.png` and `fig_benchmarks.png`.
- No internal workflow or template metadata on slide faces.

---

### Task 1: Environment & Asset Verification

**Files:**
- Test: `tests/test_assets.py`

**Interfaces:**
- Consumes: `fig_benchmarks.png`, `fig_telemetry.png`, `frontend-slides/viewport-base.css`
- Produces: Verified file presence, dimension confirmation, and test runner setup.

- [ ] **Step 1: Write asset verification test script**

```python
# tests/test_assets.py
import os
from PIL import Image

def test_assets_exist_and_readable():
    assert os.path.exists("fig_benchmarks.png"), "fig_benchmarks.png missing"
    assert os.path.exists("fig_telemetry.png"), "fig_telemetry.png missing"
    assert os.path.exists("frontend-slides/viewport-base.css"), "viewport-base.css missing"

    with Image.open("fig_benchmarks.png") as img:
        assert img.size == (3500, 1075), f"Unexpected benchmarks size: {img.size}"

    with Image.open("fig_telemetry.png") as img:
        assert img.size == (3000, 1100), f"Unexpected telemetry size: {img.size}"
```

- [ ] **Step 2: Run test to verify assets**

Run: `python3 -m pytest tests/test_assets.py -v`  
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add tests/test_assets.py
git commit -m "test: add asset and dependency verification test"
```

---

### Task 2: Core HTML Scaffold, Fixed Stage Controller & KaTeX Engine

**Files:**
- Create: `presentation.html`
- Create: `tests/test_scaffold.py`

**Interfaces:**
- Consumes: `frontend-slides/viewport-base.css`, Stencil & Tablet tokens from design spec
- Produces: Full HTML structure, theme variables, `SlidePresentation` controller with auto-scaling, keyboard navigation, inline editor hotzone, KaTeX loader, and slide counter.

- [ ] **Step 1: Write test for HTML structure, scripts, and base styles**

```python
# tests/test_scaffold.py
import re

def test_html_structure():
    with open("presentation.html", "r", encoding="utf-8") as f:
        html = f.read()

    assert "<!DOCTYPE html>" in html
    assert "class=\"deck-viewport\"" in html
    assert "id=\"deckStage\"" in html
    assert "Stardos+Stencil" in html
    assert "Barlow+Condensed" in html
    assert "katex.min.css" in html
    assert "katex.min.js" in html
    assert "auto-render.min.js" in html
    assert "SlidePresentation" in html
    assert "--color-bone" in html
    assert "--color-black" in html
```

- [ ] **Step 2: Run test to verify it fails before creating `presentation.html`**

Run: `python3 -m pytest tests/test_scaffold.py -v`  
Expected: FAIL (file not found)

- [ ] **Step 3: Implement HTML scaffold, base styles, KaTeX initialization, and presentation controller**

Implement `presentation.html` with:
- `<head>`: Fonts (`Stardos Stencil`, `Barlow Condensed`, `Inter`), KaTeX CSS + JS + auto-render.
- `<style>`: Theme tokens, full `viewport-base.css` verbatim, tablet layout utilities (`.tablet`, `.card-color`, `.action-bar`, `.matrix-table`, `.pill-status`, `.reveal`).
- `<body>`: `<div class="deck-viewport"><main class="deck-stage" id="deckStage">...</main></div>`
- `<script>`: `SlidePresentation` controller class with uniform transform scaling, keyboard arrows, touch swipe, slide counter, and inline editing (`E` key / hover hotzone).

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_scaffold.py -v`  
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add presentation.html tests/test_scaffold.py
git commit -m "feat: scaffold presentation HTML with fixed stage, Stencil & Tablet styles, and KaTeX"
```

---

### Task 3: Author Slides 01–04 (Cover, Motivation, Dilemma, Dual-Process Theory)

**Files:**
- Modify: `presentation.html`
- Create: `tests/test_slides_1_to_4.py`

**Interfaces:**
- Consumes: Task 2 scaffold
- Produces: Rendered slides 1 to 4 with Stardos typography, tablet layouts, and content matching spec.

- [ ] **Step 1: Write test for slides 1–4 content**

```python
# tests/test_slides_1_to_4.py
from bs4 import BeautifulSoup

def test_slides_1_to_4():
    with open("presentation.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    slides = soup.find_all("section", class_="slide")
    assert len(slides) >= 4

    # Slide 1: Cover
    assert "SHIFTING FROM ONE-TIME EDUCATION" in slides[0].text.upper()
    assert "HARSHITH D." in slides[0].text.upper()

    # Slide 2: Crisis
    assert "SKILL HALF-LIFE" in slides[1].text.upper()
    assert "2.5" in slides[1].text

    # Slide 3: Dilemma
    assert "INTELLIGENT TUTORING DILEMMA" in slides[2].text.upper()
    assert "BAYESIAN KNOWLEDGE TRACING" in slides[2].text.upper() or "BKT" in slides[2].text

    # Slide 4: Dual-Process
    assert "DUAL-PROCESS" in slides[3].text.upper()
    assert "SYSTEM ONE" in slides[3].text.upper()
    assert "SYSTEM TWO" in slides[3].text.upper()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_slides_1_to_4.py -v`  
Expected: FAIL

- [ ] **Step 3: Implement Slides 1 through 4 in `presentation.html`**

- Slide 1: Black field, 130px Stardos cover title, orange mark, IARE Dept of CSE lockup, authors.
- Slide 2: Bone field, 3 tablet cards (Sienna 2.5 yr, Orange 40 yr, Mustard UN SDGs 4/8/9/10).
- Slide 3: Bone field, Mustard action bar, two comparison tablets (Teal: Classical ITS/BKT vs Magenta: Monolithic LLM).
- Slide 4: Black field, two contrasting mega-tablets (Orange `01` System One Reflex vs Teal `02` System Two Deliberation) + human expert analogy callout.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_slides_1_to_4.py -v`  
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add presentation.html tests/test_slides_1_to_4.py
git commit -m "feat: author slides 1 through 4 (Cover, Motivation, Dilemma, Dual-Process Theory)"
```

---

### Task 4: Author Slides 05–08 (System 1 Reflex Engine, POMDP Math, Action Space, Pipeline)

**Files:**
- Modify: `presentation.html`
- Create: `tests/test_slides_5_to_8.py`

**Interfaces:**
- Consumes: Task 2 scaffold, KaTeX math typesetting
- Produces: Rendered slides 5 to 8 with mathematical formulas ($x_t$, $s_t$, $b(s_t)$, $P_t$, $J(\pi)$), GLiNER2.5 technical specifications, 5 discrete actions, and Algorithm 1 execution flow.

- [ ] **Step 1: Write test for slides 5–8 content and KaTeX formulas**

```python
# tests/test_slides_5_to_8.py
from bs4 import BeautifulSoup

def test_slides_5_to_8():
    with open("presentation.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    slides = soup.find_all("section", class_="slide")
    assert len(slides) >= 8

    # Slide 5: System One
    assert "GLINER2.5-DECIDE" in slides[4].text.upper()
    assert "340M" in slides[4].text

    # Slide 6: POMDP Math
    slide6_text = slides[5].text
    assert "POMDP" in slide6_text.upper()
    assert "\\Delta\\tau_k" in slide6_text or "\\Delta \\tau" in slide6_text
    assert "\\tanh" in slide6_text

    # Slide 7: Action Space
    assert "DISCRETE ACTIONS" in slides[6].text.upper()
    assert "PASSIVE FLOW" in slides[6].text.upper()

    # Slide 8: Architecture
    assert "CYBER-PHYSICAL" in slides[7].text.upper() or "PIPELINE" in slides[7].text.upper()
    assert "50 MS" in slides[7].text.upper()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_slides_5_to_8.py -v`  
Expected: FAIL

- [ ] **Step 3: Implement Slides 5 through 8 in `presentation.html`**

- Slide 5: Bone field, 3 technical cards: Fastino 340M GLiNER2.5-Decide encoder, non-autoregressive single-pass schema classification, and $<40\text{ ms}$ latency profile ($38.3\text{ ms}$ V100, $28.4\pm 4.2\text{ ms}$ simulated round-trip).
- Slide 6: Bone field, 2 analytical formula panels: Telemetry vector $x_t \in \mathbb{R}^d$, latent cognitive state $s_t = [C_t, F_t, M_t, P_t]^T$, POMDP recursive Bayesian filtering $b(s_t)$, and productive struggle index $P_t = \tanh(\omega_1 M_t - \omega_2 (C_t - C^*))$.
- Slide 7: Bone field, 5-node process sequence for actions $a_0$ to $a_4$, plus bottom objective function card $J(\pi_{\text{System One}})$.
- Slide 8: Black field, 3-stage pipeline flow: Client Worker (50ms binary frames, GDPR privacy), Edge Reflex Gateway (<40ms), and Async Socratic RPC with cooldown $T_{\text{cool}}$ lock.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_slides_5_to_8.py -v`  
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add presentation.html tests/test_slides_5_to_8.py
git commit -m "feat: author slides 5 through 8 (System 1 Engine, POMDP Math, Action Space, Pipeline)"
```

---

### Task 5: Author Slides 09–10 (Real-Time Telemetry with `fig_telemetry.png`, Socratic Engine)

**Files:**
- Modify: `presentation.html`
- Create: `tests/test_slides_9_to_10.py`

**Interfaces:**
- Consumes: `fig_telemetry.png`, Task 2 scaffold
- Produces: Rendered slides 9 and 10 with embedded `fig_telemetry.png`, annotation tablets, System Two Socratic context template, and Skill Passport.

- [ ] **Step 1: Write test for slides 9–10 content and image embedding**

```python
# tests/test_slides_9_to_10.py
from bs4 import BeautifulSoup

def test_slides_9_to_10():
    with open("presentation.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    slides = soup.find_all("section", class_="slide")
    assert len(slides) >= 10

    # Slide 9: Telemetry trace
    img_telemetry = slides[8].find("img")
    assert img_telemetry is not None
    assert "fig_telemetry.png" in img_telemetry["src"]
    assert "0.75" in slides[8].text

    # Slide 10: Socratic & Skill Passport
    assert "SOCRATIC" in slides[9].text.upper()
    assert "SKILL PASSPORT" in slides[9].text.upper()
    assert "DIJKSTRA" in slides[9].text.upper()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_slides_9_to_10.py -v`  
Expected: FAIL

- [ ] **Step 3: Implement Slides 9 and 10 in `presentation.html`**

- Slide 9: Bone field, two-column layout: Left: embedded `fig_telemetry.png` in styled paper matte container; Right: 2 annotation tablets (Teal: Micro-nudge phase with $a_1/a_2$, Orange: Socratic trigger at $C_t \ge \tau_{\text{impasse}} = 0.75$).
- Slide 10: Bone field, 2 deep cards: Magenta: Appendix B Socratic Context Injection Template (Learner profile, Dijkstra competency node, diagnostic trace, strict pedagogical directive); Blue: Immutable graph-based Skill Passport with spaced-decay functions and micro-credentials.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_slides_9_to_10.py -v`  
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add presentation.html tests/test_slides_9_to_10.py
git commit -m "feat: author slides 9 and 10 (Telemetry trace with fig_telemetry.png, Socratic remediation, Skill Passport)"
```

---

### Task 6: Author Slides 11–14 (Empirical Benchmarks with `fig_benchmarks.png`, Matrix, Standards, Conclusion)

**Files:**
- Modify: `presentation.html`
- Create: `tests/test_slides_11_to_14.py`

**Interfaces:**
- Consumes: `fig_benchmarks.png`, Task 2 scaffold
- Produces: Rendered slides 11 through 14 completing the 14-slide deck.

- [ ] **Step 1: Write test for slides 11–14 content, benchmark metrics, and matrix table**

```python
# tests/test_slides_11_to_14.py
from bs4 import BeautifulSoup

def test_slides_11_to_14():
    with open("presentation.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    slides = soup.find_all("section", class_="slide")
    assert len(slides) == 14

    # Slide 11: Benchmarks
    img_benchmarks = slides[10].find("img")
    assert img_benchmarks is not None
    assert "fig_benchmarks.png" in img_benchmarks["src"]
    assert "61.6%" in slides[10].text
    assert "84.6%" in slides[10].text
    assert "85.3%" in slides[10].text
    assert "78.9%" in slides[10].text

    # Slide 12: Matrix
    assert "STATIC CURRICULUM" in slides[11].text.upper()
    assert "DP-ALS" in slides[11].text.upper()
    pills = slides[11].find_all(class_=lambda c: c and "pill" in c)
    assert len(pills) >= 4

    # Slide 13: Standards
    assert "SDG 4" in slides[12].text.upper()
    assert "WASHINGTON ACCORD" in slides[12].text.upper()

    # Slide 14: Conclusion
    assert "CONTINUOUS LIFELONG GROWTH" in slides[13].text.upper()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_slides_11_to_14.py -v`  
Expected: FAIL

- [ ] **Step 3: Implement Slides 11 through 14 in `presentation.html`**

- Slide 11: Black field, Top: embedded `fig_benchmarks.png`; Bottom: 4 massive Stencil stat tablets (-61.6% TTM, -85.3% Impasse, -84.6% Tokens, 78.9% Flow).
- Slide 12: Bone field, Stencil & Tablet paper card matrix table featuring Table I data (Static, BKT ITS, LLM-only, DP-ALS) with color-coded status pills (Teal, Mustard, Magenta).
- Slide 13: Bone field, 2 wide tablet cards: Orange: UN SDGs 4, 8, 9, 10; Teal: Washington Accord (WK2–WK9, PO1–PO11).
- Slide 14: Black field, 3 closing tablet cards: Core takeaways, future frontiers (neuromorphic System 1, federated telemetry, fairness audits), and closing institutional lockup.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_slides_11_to_14.py -v`  
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add presentation.html tests/test_slides_11_to_14.py
git commit -m "feat: author slides 11 through 14 (Benchmarks with fig_benchmarks.png, Matrix, Standards, Conclusion)"
```

---

### Task 7: Comprehensive Verification & Visual Headless Testing

**Files:**
- Create: `tests/test_visual_verification.py`

**Interfaces:**
- Consumes: Complete `presentation.html`, `fig_telemetry.png`, `fig_benchmarks.png`
- Produces: Automated headless browser check verifying 14 slides, stage transform scaling, KaTeX equation rendering, image aspect ratios, and slide navigation.

- [ ] **Step 1: Write comprehensive verification script**

```python
# tests/test_visual_verification.py
import re
from bs4 import BeautifulSoup

def test_full_presentation_integrity():
    with open("presentation.html", "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    slides = soup.find_all("section", class_="slide")
    assert len(slides) == 14, f"Expected 14 slides, found {len(slides)}"

    # Check that both images are present and reference valid local files
    images = soup.find_all("img")
    srcs = [img["src"] for img in images]
    assert "fig_telemetry.png" in srcs
    assert "fig_benchmarks.png" in srcs

    # Check KaTeX scripts and style
    assert "katex.min.css" in html
    assert "renderMathInElement" in html

    # Check viewport-base rules
    assert "1920px" in html
    assert "1080px" in html
    assert "transform-origin: 0 0;" in html or "transform-origin: center center;" in html

    # Check all 14 slides have top chrome (except cover/divider) and titles
    for i, slide in enumerate(slides):
        assert len(slide.text.strip()) > 30, f"Slide {i+1} has insufficient content"
```

- [ ] **Step 2: Run test to verify entire presentation passes**

Run: `python3 -m pytest tests/ -v`  
Expected: ALL PASS

- [ ] **Step 3: Commit**

```bash
git add tests/test_visual_verification.py
git commit -m "test: comprehensive verification of full 14-slide presentation deck"
```
