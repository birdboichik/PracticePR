from playwright.sync_api import Page
from time import sleep

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout = page.locator("[data-test=\"checkout\"]")
        self.firstname = page.locator("[data-test=\"firstName\"]")
        self.lastname = page.locator("[data-test=\"lastName\"]")
        self.postalCode = page.locator("[data-test=\"postalCode\"]")
        self.continuee = page.locator("[data-test=\"continue\"]")
        
    def gotocheckout(self):
        self.checkout.click()
        
    def yourinformation(self, firstname: str, lastname: str, postalcode: str):
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.postalCode.fill(postalcode)
        self.continuee.click()