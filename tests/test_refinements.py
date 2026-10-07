import re
from bs4 import BeautifulSoup

def test_user_refinements():
    with open("presentation.html", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    slides = soup.find_all("section", class_="slide")
    assert len(slides) == 15

    # 1. Slide 1 and Slide 15: "DP" icon removed
    s1_html = str(slides[0])
    s15_html = str(slides[14])
    assert ">DP<" not in s1_html, "Slide 1 should not contain 'DP' square icon"
    assert ">DP<" not in s15_html, "Slide 15 should not contain 'DP' square icon"

    # Supervisor badge & Ms. N. Ramya in first and last slides
    assert "MS. N. RAMYA" in s1_html.upper()
    assert "(Supervisor)" in s1_html
    assert "MS. N. RAMYA" in s15_html.upper()
    assert "(Supervisor)" in s15_html

    # Footer checks:
    # First and last slide have DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING in bottom left
    s1_footer = slides[0].find("div", class_="footer-chrome").text
    s15_footer = slides[14].find("div", class_="footer-chrome").text
    assert "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING" in s1_footer
    assert "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING" in s15_footer

    # No "• IARE" in any slide footer
    for i, s in enumerate(slides):
        footer = s.find("div", class_="footer-chrome")
        assert footer is not None, f"Slide {i+1} missing footer-chrome"
        assert "• IARE" not in footer.text, f"Slide {i+1} still contains '• IARE' in footer: {footer.text}"

    # Slide 1 top left has INSTITUTE OF AERONAUTICAL ENGINEERING
    s1_topbar_left = slides[0].find("div", class_="topbar-left").text
    assert "INSTITUTE OF AERONAUTICAL ENGINEERING" in s1_topbar_left
    assert "IARE CSE RESEARCH SEMINAR" not in s1_topbar_left

    # 2. Slide 3: Bullet points wrapped in rounded shapes
    s3 = slides[2]
    s3_subcards = s3.find_all("div", style=lambda s: s and "border-radius: 16px" in s and "background: rgba(0, 0, 0, 0.22)" in s)
    assert len(s3_subcards) >= 6, f"Expected 6 rounded sub-cards in Slide 3, got {len(s3_subcards)}"

    # 3. Slide 5: Formula font size increased
    s5_html = str(slides[4])
    assert "font-size: 28px" in s5_html and "\\pi_{\\text{System One}}" in s5_html

    # 4. Slide 9: Right cards have larger font size (25px)
    s9_html = str(slides[8])
    assert "font-size: 25px" in s9_html
    assert "font-size: 28px" in s9_html

    # 5. Slide 10: Rich sub-cards and prompt directives
    s10 = slides[9]
    s10_text = s10.text
    assert "GRAPH-BASED COMPETENCY MAPPING" in s10_text
    assert "SPACED-DECAY RETENTION ENGINE" in s10_text
    assert "IMMUTABLE LIFELONG MICRO-CREDENTIALS" in s10_text
    assert "OUTPUT QUESTION" in s10_text

    # 6. Slide 14: All 3 tablets have structured sub-cards
    s14 = slides[13]
    s14_text = s14.text
    assert "SUB-40MS REFLEX ENGINE" in s14_text
    assert "IMPASSE-GATED SOCRATIC LLM" in s14_text
    assert "NEUROMORPHIC EDGE DEPLOYMENT" in s14_text
    assert "DYNAMIC VS. STATIC ACCREDITATION" in s14_text
    assert "DECAY-AWARE REFRESHER CADENCE" in s14_text
