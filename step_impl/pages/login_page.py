from selenium.webdriver.common.by import By
from utilities.base_ui import BaseUI


class LoginPageLocators:
    EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    DISPLAY_COMPANY_NAME = (By.CSS_SELECTOR, "span.pl-sm.truncate.ng-binding")


class LoginPage(BaseUI):
    URL = format(BaseUI.BASE_UI_URL)

    # Method for fill Email Address Field
    def fill_email_address_field(self, email_address):
        self.custom_wait()
        self.set(LoginPageLocators.EMAIL_ADDRESS_FIELD, email_address)

    # Method for fill Password Field
    def fill_password_field(self, password):
        self.set(LoginPageLocators.PASSWORD_FIELD, password)

    # Method for Click on Login Button
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    # Method for Navigate to URL
    def visit(self):
        self.driver.get(self.URL)

    # Method for get the Profile Display Name
    def get_company_name(self):
        self.custom_wait()
        return self.get(LoginPageLocators.DISPLAY_COMPANY_NAME)

    # Method for get the page title
    def get_page_title(self):
        return self.driver.title
