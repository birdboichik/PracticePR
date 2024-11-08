from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage

def test_empty_login_and_password(page: Page):
    log = LoginPage(page)
    log.goto()
    log.login("", "")
    expect(log.error).to_contain_text("Epic sadface: Username is required")