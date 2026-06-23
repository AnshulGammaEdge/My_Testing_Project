from playwright.sync_api import sync_playwright, expect
from utils.logger import setup_logger

logger=setup_logger()

class resetpass:
    
    def __init__(self,page):
        self.page=page
        self.pass_field="#email"
        self.submit_btn_name="Retrieve password"
        self.assertion_ver="An e-mail has been sent to you which explains how to reset your password."
    
    def journey(self,data):

        self.page.locator(self.pass_field).fill(data["reset_pass"])
        logger.info("Password for reset process has filled")
        self.page.get_by_role("button", name=self.submit_btn_name).click()
    
    def assertion (self):
        var=self.page.get_by_text(self.assertion_ver, exact=True)
        expect(var).to_be_visible()
        logger.info("assertion successful, password reset process has completed")





        