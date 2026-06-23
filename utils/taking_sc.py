import time
import os

class utils:

    def __init__(self,page):
        self.page=page
    
    def take_sc(self):
        ts=int(time.time())
        self.page.screenshot(path=f"screenshots/test_screenshot_{ts}.png")