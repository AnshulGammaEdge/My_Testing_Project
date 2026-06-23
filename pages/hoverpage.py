class hover:

    def __init__(self,page):
        self.page=page
        self.btn_hover="Point Me"
        self.link_click="Mobiles"
    
    def journey(self):
        self.page.get_by_role("button", name=self.btn_hover).hover()
        self.page.get_by_role("link", name=self.link_click).click()