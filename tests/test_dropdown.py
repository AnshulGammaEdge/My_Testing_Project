from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.dropdownpage import dropdown
@pytest.mark.pop
def test_drop_down(page,data):

    
    page.goto(data["url2"])
    dD=dropdown(page)
    dD.journey()
    
    