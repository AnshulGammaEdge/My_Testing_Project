class popup:

    def __init__(self,page):
        self.page=page
        #self.alert_click="Simple Alert"
        #self.confirm_click="Confirmation Alert"
        self.prompt="Prompt Alert"
    
    def journey(self):
        #self.page.on("dialog",lambda dialog : dialog.accept())
        #self.page.get_by_role("button", name=self.alert_click).click()
        #self.page.on("dialog",lambda dialog : dialog.dismiss())

        #self.page.get_by_role("button", name=self.confirm_click).click()
        self.page.on("dialog",lambda dialog : dialog.accept("John Cena"))
        self.page.get_by_role("button", name=self.prompt).click()


        # target=self.page.get_by_role("button", name=self.prompt)
        # print(target.text_content())


        