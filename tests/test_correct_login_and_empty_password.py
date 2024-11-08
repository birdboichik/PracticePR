from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage

def test_correct_login_and_empty_password(page: Page):
    log = LoginPage(page)
    log.goto()
    log.login("standard_user", "")
    expect(log.error).to_contain_text("Epic sadface: Password is required")