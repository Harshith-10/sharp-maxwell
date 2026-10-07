import os

def test_html_structure():
    assert os.path.exists("presentation.html"), "presentation.html does not exist"
    with open("presentation.html", "r", encoding="utf-8") as f:
        html = f.read()

    assert "<!DOCTYPE html>" in html
    assert "class=\"deck-viewport\"" in html
    assert "id=\"deckStage\"" in html
    assert "Stardos+Stencil" in html
    assert "Barlow+Condensed" in html
    assert "Inter:" in html
    assert "katex.min.css" in html
    assert "katex.min.js" in html
    assert "auto-render.min.js" in html
    assert "SlidePresentation" in html
    assert "--color-bone" in html
    assert "--color-black" in html
    assert "--color-orange" in html
    assert "--color-teal" in html
