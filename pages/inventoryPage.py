
from playwright.sync_api import Page
from time import sleep

class inventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.tShirt = page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.backpackAdd = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.onesie = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        self.bikeLight = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.jacket = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
        self.tShirtRed = page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]")
        self.cartlink = page.locator("[data-test=\"shopping-cart-link\"]")
        
    def AddToCart(self, *args):
        for arg in args:
            if arg.is_visible():
                arg.click()
            else:
                break
    def goToCard(self):
        self.cartlink.click()
    
        