from playwright.sync_api import sync_playwright
import pytest

def test_brosite(playwright):
    browser = playwright.chromium.launch(
        executable_path=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        headless=False
    )

    page = browser.new_page()
    page.goto("https://2captcha.com/demo/recaptcha-v2")
    page.wait_for_timeout(5000)
    #page.locator('textarea[aria-expanded="false"]').fill("brock lesner")
    page.wait_for_timeout(5000)


    print(page.title())

    browser.close()