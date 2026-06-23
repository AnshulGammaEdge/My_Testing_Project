
import pytest
import time
from utils.logger import setup_logger
from pages.kewboardpage import keyboard
logger=setup_logger()

@pytest.mark.pop
def test_keyb(page,data):
    page.goto(data["url2"])
    k=keyboard(page)
    k.journey()

    

