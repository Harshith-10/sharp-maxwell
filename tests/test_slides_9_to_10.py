from bs4 import BeautifulSoup

def test_slides_9_to_10():
    with open("presentation.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    slides = soup.find_all("section", class_="slide")
    assert len(slides) >= 10, f"Expected at least 10 slides, got {len(slides)}"

    # Slide 9: Telemetry trace (index 9)
    img_telemetry = slides[9].find("img")
    assert img_telemetry is not None
    assert "fig_telemetry.png" in img_telemetry["src"]
    s9_text = slides[9].text
    assert "0.75" in s9_text
    assert "IMPASSE" in s9_text.upper()

    # Slide 10: Socratic & Skill Passport (index 10)
    s10_text = slides[10].text.upper()
    assert "SOCRATIC" in s10_text
    assert "SKILL PASSPORT" in s10_text
    assert "DIJKSTRA" in s10_text
