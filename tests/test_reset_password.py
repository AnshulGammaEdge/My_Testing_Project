from playwright.sync_api import sync_playwright
import pytest
from pages.reset_pass_page import resetpass
from utils.logger import setup_logger

logger=setup_logger()

def test_password_reset(page,data):

    page.goto(data["url3"])
    logger.info(" url is opening now")
    rp=resetpass(page)

    rp.journey(data)

    rp.assertion()