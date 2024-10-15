from tests.pages.page import Page
from tests.utils.exceptions import LoginPageException
from tests.locators.login_page_locators import LoginPageLocators

class LoginPage(Page):
    def enter_username(self, username):
        self.enter_text(LoginPageLocators.username, username)

    def enter_password(self, password):
        self.enter_text(LoginPageLocators.password, password)

    def click_next(self):
        self.click(LoginPageLocators.next)

    def click_signin(self):
        self.click(LoginPageLocators.signin)

    def is_button_visible(self):
        return self.is_visible(LoginPageLocators.next)

    def verify_login_success(self):
        try:
            assert self.is_button_visible() is False, "Login was not successful."
        except AssertionError as e:
            raise LoginPageException("Failed to login with provided credentials") from e

    def verify_welcome_page(self):
        try:
            self.wait_for_element(LoginPageLocators.welcomepage)
            return self.get_element_text(LoginPageLocators.welcomepage)
        except AssertionError as e:
            #TODO welcome page not visible exception must be replaced here
            raise e
