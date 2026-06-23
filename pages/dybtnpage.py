class dybtn:

    def __init__(self,page):
        self.page=page
        self.start_btn="START"
        self.stop_btn="STOP"



    def journey(self):
        self.page.get_by_role("button", name=self.start_btn).click()
        self.page.get_by_role("button", name=self.stop_btn).click()
        target=self.page.get_by_role("button", name=self.start_btn)
        print(target.text_content())