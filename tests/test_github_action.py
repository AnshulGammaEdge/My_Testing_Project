import pytest
from playwright.sync_api import expect

def test_github(page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_role("link",name="Blog").click()
    var=page.locator("h3.post-title entry-title")
    expect(var).to_be_visible()