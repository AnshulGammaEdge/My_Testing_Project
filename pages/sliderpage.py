class slider:
    def __init__(self,page):
        self.page=page
        self.slider_w=".ui-slider-range"
    
    def journey(self):
        self.page.mouse.wheel(0,1800)
        slide = self.page.locator(self.slider_w)
        box = slide.bounding_box()
        print(box)
        self.page.wait_for_timeout(4000)
        self.page.mouse.move(box["x"], box["y"])
        self.page.mouse.down()
        self.page.wait_for_timeout(4000)
        self.page.mouse.move(box["x"] + 100, box["y"])
        self.page.wait_for_timeout(4000)
        self.page.mouse.up()
