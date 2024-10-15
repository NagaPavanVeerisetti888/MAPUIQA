from selenium.common import TimeoutException
from tests.locators.data_quality_management_locators import DataQualityManagementLocators
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.page import Page

class DataQualityManagementPage(Page):
    def is_DQM_Page_Open(self):
         self.is_visible(DataQualityManagementLocators.DQMPageBanner)


