import pytest
from playwright.sync_api import expect, Page


@pytest.mark.parametrize(
    "user, password",
    [
        ("standard_user", "secret_sauce"),
        ("locked_out_user", "secret_sauce")
    ]
)
def test_login(page: Page, user, password):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill(user)
    page.locator("#password").fill(password)

    page.get_by_role("button", name="Login").click()

    page.wait_for_timeout(2000)


@pytest.mark.xyz
def test_winHnadling(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    with page.expect_popup() as nw:
        page.get_by_role("button", name="New Tab").click()

    nt = nw.value

    nt.get_by_role("link", name="Online Training").click()

    ver = nt.locator("h1.hero-title")

    expect(ver).to_be_visible()