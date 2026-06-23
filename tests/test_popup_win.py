from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.popwinpage import popwin
logger=setup_logger()
@pytest.mark.pop
def test_popup_win(page,data):
    
    page.goto(data["url2"])
    pw=popwin(page)
    pw.journey()
    

