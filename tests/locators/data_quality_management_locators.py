from selenium.webdriver.common.by import By


class DataQualityManagementLocators:
    DQMPageBanner = (By.XPATH, "(//*[contains(text(), 'Data Quality Management')])[2]")
    AgencyColumn = (By.XPATH, "//span[contains(text(),'AGENCY')]")
    ToolTip = (By.XPATH, '//div[@class="k-tooltip"]')
