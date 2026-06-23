class keyboard:
    def __init__(self,page):
        self.page=page
        self.ele="#field1"





    def journey(self):
        tar=self.page.locator(self.ele)
        tar.press("Control+A")
        tar.press("Control+C")
        tar2=self.page.locator("#field2")
        tar2.press("Control+V")
    