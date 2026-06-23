class popwin:

    def __init__(self,page):
        self.page=page
        self.popupwin_open="#PopUp"
        self.span='button[class="navbar-toggler"]'
        self.about="About"
        self.new_win="a.dropdown-item"
        self.sel="About Selenium"

    
    def journey(self):
        with self.page.expect_popup() as obj:
            self.page.locator(self.popupwin_open).click()
            nw=obj.value
            # self.page.pause()
            nw.locator(self.span).click()
            #nw.pause()
            nw.get_by_text(self.about, exact=True).click()
            target=nw.locator(self.new_win).filter(has_text=self.sel)
            target.click()

