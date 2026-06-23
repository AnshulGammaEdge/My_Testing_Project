class roombooking:
    def __init__(self,page):
        self.page=page
        self.check_in="label[for='checkin'] + div input"
        self.check_out="label[for='checkout'] + div input"
        self.check_calender="gridcell"

    def check_in_out_date(self):
        #check in date
        date_input = self.page.locator(self.check_in)
        date_input.click()
        date_input.press("Control+A")
        date_input.press("Backspace")
        date_input.type("25/06/2026")
        date_input.press("Enter")

        #check out date
        date_input = self.page.locator(self.check_out)
        date_input.click()
        date_input.press("Control+A")
        date_input.press("Backspace")
        date_input.type("28/06/2026")
        date_input.press("Enter")

        self.page.get_by_role("button", name="Check Availability").click()
        self.page.wait_for_timeout(5000)
    
    def room_book_process(self):
        self.page.get_by_role("link", name="Book now").nth(2).click()
        self.page.wait_for_timeout(3000)
        self.page.locator("#doReservation").click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_placeholder("Firstname").fill("John")
        self.page.wait_for_timeout(3000)
        self.page.get_by_placeholder("Lastname").fill("Wick")
        self.page.wait_for_timeout(3000)
        self.page.get_by_placeholder("Email").fill("abc@gamil.com")
        self.page.wait_for_timeout(3000)
        self.page.get_by_placeholder("Phone").fill("987654321123")
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("button", name="Reserve Now").click()
        self.page.wait_for_timeout(3000)



