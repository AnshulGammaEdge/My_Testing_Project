from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.getrolepage import getrole
logger=setup_logger()


@pytest.mark.pop
def test_get_role(page,data):
    page.goto(data["url2"])
    gr=getrole(page)
    gr.journey(data)
        

    