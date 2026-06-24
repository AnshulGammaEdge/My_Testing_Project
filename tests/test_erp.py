from playwright.sync_api import sync_playwright,expect

def test_erp(playwright):
    browser=playwright.chromium.launch(headless=True)
    page=browser.new_page()
    page.goto("https://www.netsuite.com/portal/in/home.shtml")
    


    """new_pop_up=page.locator("#popupFPT")

    if new_pop_up.count()> 0 and new_pop_up.is_visible():
        new_pop_up.locator("button.btn-close.btn-close-white").click()
    
    page.wait_for_timeout(5000)

     # Handle modal-products popup
    modal_popup = page.locator("#modal-products")

    if modal_popup.is_visible():
        modal_popup.locator("button.btn-close").click()"""

    #page.pause()
    with page.expect_popup() as obj:
        
        page.get_by_role("link", name="Discover More").click()
        x=obj.value
        var=x.locator("ul.story-specs__list--sub.list-unstyled").get_by_role("link", name="NetSuite OneWorld")
        #var=x.locator("a[href*='portal/products/global-business-management.shtml']").first
        
        var.scroll_into_view_if_needed()
        expect(var).to_be_visible(timeout=10000)
        var.click()
        x.wait_for_timeout(5000)
        ct=x.locator("#customers-tab")
        #ct.scroll_into_view_if_needed()
        #x.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        x.mouse.wheel(0, 6000)
        
        #x.pause()
        ct.click()
        x.locator("ul.list-unstyled").get_by_role("link", name="Brex, the Fintech Star, Looks Back on Its Switch from QuickBooks to NetSuite").click
        x.wait_for_timeout(2000)
        x.screenshot(path="screenshots/oracle.png")
    browser.close()