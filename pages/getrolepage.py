class getrole:

    def __init__(self,page):
        self.page=page
        self.action_btn="Primary Action"
        self.username="Username:"
        self.checkbox="Accept terms"


    def journey(self,data):
        
        self.page.get_by_role("button", name=self.action_btn).click()
        self.page.get_by_label(self.username).fill(data["role_user"])
        self.page.get_by_role("checkbox", name=self.checkbox).check()
        self.page.wait_for_timeout(5000)
