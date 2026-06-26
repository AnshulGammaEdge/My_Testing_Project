from playwright.sync_api import sync_playwright,Playwright,expect
import pytest

def test_abc(playwright):
    browser=playwright.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.ajio.com/",wait_until="domcontentloaded")
    page.locator("svg").nth(1).click()
    search_box=page.get_by_placeholder("Search AJIO")
    search_box.fill("Shoes for boys")
    search_box.press("Enter")
