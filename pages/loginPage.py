from playwright.sync_api import expect

class loginPage:

    def __init__(self,page):
        self.page=page
        self.username="#user-name"
        self.password="#password"
        self.login_btn="button"
        self.cart="#add-to-cart-sauce-labs-backpack"
        self.shopping_link=".shopping_cart_link"
        self.verification="Sauce Labs Backpack" 
    

    def login(self,data):
        self.page.locator(self.username).fill(data["user"])
        self.page.locator(self.password).fill(data["pass"])
        self.page.get_by_role(self.login_btn, name="Login").click()


    def journey(self):
        self.page.locator(self.cart).click()
        self.page.locator(self.shopping_link).click()
    
    def assertion(self):
        ver=self.page.get_by_text("Sauce Labs Backpack", exact=True)
        expect(ver).to_be_visible()