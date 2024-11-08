from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from pages.inventoryPage import inventoryPage
from pages.cartPage import CartPage
from time import sleep

def test_correct_login_and_password(page: Page):
    log = LoginPage(page)
    log.goto()
    log.login("standard_user", "secret_sauce")
    inv = inventoryPage(page)
    inv.AddToCart(inv.backpackAdd,inv.tShirtRed)
    inv.goToCard()
    cart = CartPage(page)
    cart.gotocheckout()
    cart.yourinformation("danul", "password","123")
    
    sleep(10)
