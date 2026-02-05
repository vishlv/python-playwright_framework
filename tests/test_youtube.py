import pytest

@pytest.fixture(page)
def test_youtube_title(page):
    page.goto("https://www.youtube.com")
    assert "YouTube" in page.title()