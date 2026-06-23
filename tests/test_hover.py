from playwright.sync_api import sync_playwright
import pytest
from utils.logger import setup_logger
from pages.hoverpage import hover
logger=setup_logger()

@pytest.mark.pop
def test_hover(page,data):
    
    page.goto(data["url2"])
    h=hover(page)
    h.journey()

   

    