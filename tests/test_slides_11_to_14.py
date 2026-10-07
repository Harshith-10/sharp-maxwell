from bs4 import BeautifulSoup

def test_slides_11_to_14():
    with open("presentation.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    slides = soup.find_all("section", class_="slide")
    assert len(slides) == 14, f"Expected exactly 14 slides, got {len(slides)}"

    # Slide 11: Benchmarks
    s11 = slides[10]
    img_benchmarks = s11.find("img")
    assert img_benchmarks is not None
    assert "fig_benchmarks.png" in img_benchmarks["src"]
    s11_text = s11.text
    assert "61.6%" in s11_text
    assert "84.6%" in s11_text
    assert "85.3%" in s11_text
    assert "78.9%" in s11_text

    # Slide 12: Comparison Matrix Table
    s12 = slides[11]
    s12_text = s12.text.upper()
    assert "STATIC CURRICULUM" in s12_text
    assert "DP-ALS" in s12_text
    assert "RULE-BASED ITS" in s12_text
    pills = s12.find_all(class_=lambda c: c and "pill" in c)
    assert len(pills) >= 4, f"Expected at least 4 status pills in matrix, got {len(pills)}"

    # Slide 13: Standards
    s13 = slides[12]
    s13_text = s13.text.upper()
    assert "SDG 4" in s13_text
    assert "WASHINGTON ACCORD" in s13_text
    assert "WK2" in s13_text or "PO1" in s13_text

    # Slide 14: Conclusion
    s14 = slides[13]
    s14_text = s14.text.upper()
    assert "CONTINUOUS LIFELONG GROWTH" in s14_text or "LIFELONG GROWTH" in s14_text
    assert "NEUROMORPHIC" in s14_text or "FEDERATED" in s14_text
