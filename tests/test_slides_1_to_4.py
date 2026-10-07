from bs4 import BeautifulSoup

def test_slides_1_to_4():
    with open("presentation.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    slides = soup.find_all("section", class_="slide")
    assert len(slides) >= 4, f"Expected at least 4 slides, got {len(slides)}"

    # Slide 1: Cover
    s1_text = slides[0].text.upper()
    assert "SHIFTING FROM ONE-TIME EDUCATION" in s1_text
    assert "CONTINUOUS GROWTH" in s1_text
    assert "HARSHITH D." in s1_text
    assert "AERONAUTICAL ENGINEERING" in s1_text

    # Slide 2: Crisis
    s2_text = slides[1].text.upper()
    assert "SKILL HALF-LIFE" in s2_text or "SKILL OBSOLESCENCE" in s2_text
    assert "2.5" in slides[1].text
    assert "SDG" in s2_text

    # Slide 3: Dilemma
    s3_text = slides[2].text.upper()
    assert "INTELLIGENT TUTORING DILEMMA" in s3_text or "TUTORING DILEMMA" in s3_text
    assert "BAYESIAN KNOWLEDGE TRACING" in s3_text or "BKT" in s3_text
    assert "MONOLITHIC" in s3_text or "LLM" in s3_text

    # Slide 4: Dual-Process
    s4_text = slides[3].text.upper()
    assert "DUAL-PROCESS" in s4_text
    assert "SYSTEM ONE" in s4_text
    assert "SYSTEM TWO" in s4_text
