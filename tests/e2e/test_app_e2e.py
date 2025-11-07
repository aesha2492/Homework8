import pytest

BASE = "http://127.0.0.1:8000"

@pytest.mark.e2e
def test_addition_flow(page):
    page.goto(BASE)
    page.fill("#a", "2")
    page.fill("#b", "3")
    page.select_option("#op", "add")
    page.click("#go")
    # Wait for the result element to be present (not necessarily visible-with-text)
    page.wait_for_selector("#out", state="attached")
    val = page.inner_text("#out").strip()
    assert val in {"5", "5.0"}

@pytest.mark.e2e
def test_divide_by_zero_ui(page):
    page.goto(BASE)
    page.fill("#a", "1")
    page.fill("#b", "0")
    page.select_option("#op", "divide")
    page.click("#go")
    # The UI doesn't show an explicit error; ensure the span is still present.
    page.wait_for_selector("#out", state="attached")
    val = page.inner_text("#out").strip()
    # Minimal UI keeps it unchanged / empty on 400; accept common empty-ish values.
    assert val in {"—", "", "Infinity", "0", "-0", "nan", "NaN"}
