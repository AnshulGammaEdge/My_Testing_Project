class pagination:
    def __init__(self,page):
        self.page=page
        self.pageination_ele="#pagination"
        self.list="li"
        self.ver="3"
        self.access_row="#productTable tbody tr"
        self.row_no=3
        self.checkbox="input[type='checkbox']"
    
    def journey(self):
        pagena=self.page.locator(self.pageination_ele)
        pagena.locator(self.list).filter(has_text=self.ver).click()
        row = self.page.locator(self.access_row).nth(self.row_no)   # index starts from 0
        row.locator(self.checkbox).check()