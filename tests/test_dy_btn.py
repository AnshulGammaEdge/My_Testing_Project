from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.dybtnpage import dybtn
logger=setup_logger()


@pytest.mark.pop
def test_dy_btn(page,data):
    
    page.goto(data["url2"])
    dyb=dybtn(page)
    dyb.journey()

   
