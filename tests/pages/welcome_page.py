from tests.locators.welcome_page_locators import WelcomePageLocators
from tests.pages.page import Page

class WelcomePage(Page):
    def click_MapLakeview(self):
        #TODO need to remove the print statements after debugging
        print(f"I am here to debug the code.")
        title = self.get_page_title()
        print(f"Title of the page is : {title}")
        if title == 'MAP Mortgage Asset Positions':
            print(f"This is before the click on Maplakeview")
            banner = self.get_element_text(WelcomePageLocators.WelcomeBanner)
            print(f"This is the banner we got: {banner}")
            if banner == 'Welcome Page':
                self.click(WelcomePageLocators.DataQualityManagement)
                print(f"This is after the click on Maplakeview")
            else:
                print(f"driver couldn't find the locator.")
