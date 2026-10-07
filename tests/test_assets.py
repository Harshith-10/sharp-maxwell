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
