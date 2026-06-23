from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.sliderpage import slider
logger=setup_logger()


@pytest.mark.pop
def test_custom_slider(page,data):

    page.goto(data["url2"])
    s=slider(page)
    s.journey()
