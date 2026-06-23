class dropdown:

    def __init__(self,page):
        self.page=page
        self.combobox="#comboBox"
        self.dropdown="#dropdown"
        self.option="div.option"
        self.value="Item 12"
    
    def journey(self):
        self.page.locator(self.combobox).click()
        dd=self.page.locator(self.dropdown)
        dd.scroll_into_view_if_needed()
        target= dd.locator(self.option).filter(has_text=self.value)
        #target.pause()
        target.click()
        self.page.wait_for_timeout(5000)

        