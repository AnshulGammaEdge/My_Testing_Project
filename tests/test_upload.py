from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.uploadpage import upload
logger=setup_logger()

@pytest.mark.pop
def test_upload(page,data):
   
    page.goto(data["url2"])
    u=upload(page)
    u.journey()
    

    

