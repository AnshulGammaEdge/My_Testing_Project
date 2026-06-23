from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.painationepage import pagination

logger=setup_logger()

@pytest.mark.pop
def test_pagen(page,data):
    

    page.goto(data["url2"])
    p=pagination(page)
    p.journey()
    
    

