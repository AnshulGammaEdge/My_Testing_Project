from playwright.sync_api import sync_playwright
import pytest

def test_brosite(playwright):
    browser = playwright.chromium.launch(headless=True)

    page = browser.new_page()
    page.goto("https://2captcha.com/demo/recaptcha-v2")
    page.wait_for_timeout(5000)
    #page.locator('textarea[aria-expanded="false"]').fill("brock lesner")
    page.wait_for_timeout(5000)


    print(page.title())

    browser.close()