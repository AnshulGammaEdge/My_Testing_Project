from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.dragdroppage import dragdrop
logger=setup_logger()

@pytest.mark.pop
def test_drag_drop(page,data):
   
    page.goto(data["url2"])
    dd=dragdrop(page)
    dd.journey()
    
    

