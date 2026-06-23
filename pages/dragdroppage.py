class dragdrop:

    def __init__(self,page):
        self.page=page
        self.drag="Drag me to my target"
        self.target="#droppable"

    def journey(self):
        dr=self.page.get_by_text(self.drag, exact=True)
        dp=self.page.locator(self.target)
        dr.drag_to(dp)

        