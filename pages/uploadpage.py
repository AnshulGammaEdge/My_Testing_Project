class upload:

    def __init__(self,page):
        self.page=page
        self.upload_file="#multipleFilesInput"
        self.upload_btn="Upload Multiple Files"

    def journey(self):
        up=self.page.locator(self.upload_file)
        up.set_input_files(["screenshots/brock.png","screenshots/oracle.png"])
        self.page.get_by_role("button", name=self.upload_btn).click()
