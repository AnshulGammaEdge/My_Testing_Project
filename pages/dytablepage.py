from utils.dy_table import click_action_by_name

class dytable:

    def __init__(self,page):
        self.page=page
        self.dy_table_l="#taskTable"

    def journey(self):
        table_loc = self.page.locator(self.dy_table_l)
        click_action_by_name(table_loc, "0.29 MB/s")