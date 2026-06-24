class popwin:

    def __init__(self, page):
        self.page = page
        self.popupwin_open = "#PopUp"
        self.span = "span.navbar-toggler-icon"
        self.about = "#navbarDropdown"
        self.class_sel = "a.dropdown-item"
        self.sel = "About Selenium"

    def journey(self):

        with self.page.expect_popup() as popup:
            self.page.locator(self.popupwin_open).dblclick()

        t_0 = popup.value

        print(t_0.url)

        t_0.wait_for_load_state("networkidle")
        t_0.bring_to_front()

        t_0.locator(self.span).click()
        t_0.locator(self.about).click()
        t_0.locator(self.class_sel).filter(has_text=self.sel).click()