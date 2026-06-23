from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.newtabpage import newtab

logger=setup_logger()

@pytest.mark.pop
def test_New_Tab(page,data):
    
    page.goto(data["url2"])
    nt=newtab(page)
    nt.journey()
    
    
