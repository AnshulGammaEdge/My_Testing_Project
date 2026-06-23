import time
class newtab:

    def __init__(self,page):
        self.page=page
        self.search="input.wikipedia-search-button"
        self.result="div.wikipedia-search-results"
        self.link='a[href="https://en.wikipedia.org/wiki/Brock_Lesnar"]'

    
    def journey(self):
        with self.page.expect_popup() as obj :

            self.page.locator("input.wikipedia-search-input").fill("Brock Lesner")
            self.page.locator(self.search).click()
            self.page.locator(self.result).click()
            link=self.page.locator(self.link)
            link.wait_for(state="visible")
            link.click()
            nw=obj.value
            timestamp=int(time.time())
            nw.screenshot(path=f"screenshots/brock{timestamp}.png")

