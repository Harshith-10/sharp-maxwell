from bs4 import BeautifulSoup

def test_slides_5_to_8():
    with open("presentation.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    slides = soup.find_all("section", class_="slide")
    assert len(slides) >= 8, f"Expected at least 8 slides, got {len(slides)}"

    # Slide 5: System One
    s5_text = slides[4].text.upper()
    assert "GLINER2.5-DECIDE" in s5_text
    assert "340M" in s5_text
    assert "40 MS" in s5_text or "40MS" in s5_text

    # Slide 6: POMDP Math
    s6_text = slides[5].text
    assert "POMDP" in s6_text.upper()
    assert "\\Delta\\tau_k" in s6_text or "\\Delta \\tau" in s6_text or "\\tau" in s6_text
    assert "\\tanh" in s6_text
    assert "0.65" in s6_text

    # Slide 7: Action Space
    s7_text = slides[6].text.upper()
    assert "DISCRETE ACTIONS" in s7_text or "ACTION SPACE" in s7_text
    assert "PASSIVE FLOW" in s7_text
    assert "SYSTEM TWO" in s7_text or "SYSTEM 2" in s7_text

    # Slide 8: Cyber-Physical Architecture
    s8_text = slides[7].text.upper()
    assert "CYBER-PHYSICAL" in s8_text or "PIPELINE" in s8_text
    assert "50 MS" in s8_text or "50MS" in s8_text
    assert "WEBSOCKET" in s8_text
