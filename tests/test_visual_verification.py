import os
import re
from bs4 import BeautifulSoup

def test_full_presentation_integrity():
    assert os.path.exists("presentation.html")
    with open("presentation.html", "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    slides = soup.find_all("section", class_="slide")
    assert len(slides) == 15, f"Expected 15 slides, found {len(slides)}"
    assert "THANK YOU" in slides[14].text.upper()

    # Check that both images are present and reference valid local files
    images = soup.find_all("img")
    srcs = [img["src"] for img in images]
    assert "fig_telemetry.png" in srcs, "fig_telemetry.png not embedded"
    assert "fig_benchmarks.png" in srcs, "fig_benchmarks.png not embedded"
    for src in ["fig_telemetry.png", "fig_benchmarks.png"]:
        assert os.path.exists(src), f"Image file {src} missing from directory"

    # Check KaTeX scripts and style
    assert "katex.min.css" in html
    assert "renderMathInElement" in html
    assert "renderMath" in html

    # Check fixed-stage 16:9 rules
    assert "1920px" in html
    assert "1080px" in html
    assert "deck-viewport" in html
    assert "deck-stage" in html

    # Check Stencil & Tablet design tokens
    assert "--color-bone" in html
    assert "--color-black" in html
    assert "--color-orange" in html
    assert "--color-teal" in html
    assert "--color-magenta" in html
    assert "--color-mustard" in html
    assert "Stardos+Stencil" in html
    assert "Barlow+Condensed" in html

    # Verify each slide has rich content and appropriate labels
    for i, slide in enumerate(slides):
        assert slide.has_attr("data-label"), f"Slide {i+1} missing data-label"
        text = slide.text.strip()
        assert len(text) > 40, f"Slide {i+1} has insufficient content ({len(text)} chars)"

    # Verify mathematical formulas are present
    assert "\\Delta\\tau_k" in html or "\\Delta \\tau" in html
    assert "\\tanh" in html
    assert "\\pi_{\\text{System One}}" in html or "\\pi_" in html
    assert "J(\\pi" in html

    # Verify no template/dev placeholders
    forbidden = ["TODO", "TBD", "PLACEHOLDER", "OPTION A", "STYLE PREVIEW"]
    for word in forbidden:
        assert word not in html.upper(), f"Found forbidden artifact word: {word}"
