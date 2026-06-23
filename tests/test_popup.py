from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.popuppage import popup
logger=setup_logger()

@pytest.mark.pop
def test_popup(page,data):
    
    page.goto(data["url2"])
    pop=popup(page)
    pop.journey()
    
    
