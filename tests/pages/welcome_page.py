from tests.locators.welcome_page_locators import WelcomePageLocators
from tests.pages.page import Page

class WelcomePage(Page):
    def click_MapLakeview(self):
        self.click(WelcomePageLocators.MapLakeViewButton)