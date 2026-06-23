from playwright.sync_api import sync_playwright
import pytest
import time
from utils.logger import setup_logger
from pages.dytablepage import dytable

logger=setup_logger()


@pytest.mark.pop
def test_dyTable(page,data):
    
    page.goto(data["url2"])
    d=dytable(page)
    d.journey()

    

