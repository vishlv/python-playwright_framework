from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)

    def perform_login(self, username, password):
        try:
            self.fill(LoginPageLocators.USERNAME_FIELD, username)
            self.fill(LoginPageLocators.PASSWORD_FIELD, password)
            self.click(LoginPageLocators.LOGIN_BTN)
            try:
                expect(self.page.locator(LoginPageLocators.ERROR_MESSAGE_FOR_INVALID_CREDS)).not_to_be_visible()
                expect(self.page.get_by_text("Dashboard")).to_be_visible()
                return True
            except AssertionError:
                print("Credentials are invalid")
                return False
        except TimeoutError as p:
            print(f"error occured {p}")
            return False
            
    
        