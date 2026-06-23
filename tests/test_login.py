from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from pages.loginPage import loginPage
from utils.taking_sc import utils


def test_login(page,data):
    page.goto(data["url"])
    p=loginPage(page)
    u=utils(page)
    ##page.pause()
    p.login(data)
    u.take_sc()
    p.journey()
    p.assertion()
    
   
    

    