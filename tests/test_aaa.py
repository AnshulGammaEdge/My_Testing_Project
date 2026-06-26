from playwright.sync_api import sync_playwright, Playwright,expect

def test_browser(page):
   
    page.goto("https://www.amazon.in")
    page.wait_for_timeout(3000)

    search_box = page.get_by_placeholder("Search Amazon.in")
    search_box.fill("Casual Shoes for Men")
    search_box.press("Enter")
    
    page.wait_for_timeout(3000)

    varify_e=page.locator("span.a-size-base.a-color-base").filter(has_text="Campus").first
    expect(varify_e).to_be_visible()
    page.wait_for_timeout(3000)




    
