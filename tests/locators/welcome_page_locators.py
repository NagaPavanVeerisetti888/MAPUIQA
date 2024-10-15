from selenium.webdriver.common.by import By

class WelcomePageLocators:
    #TODO Optimize the below locator
    WelcomeBanner = (By.XPATH, "//h1[contains(text(), 'Welcome Page')]")
    MapLakeViewButton = (By.XPATH, "(//div[contains(@class, 'card boxStyle pointer')])[1]")
    DataQualityManagement = (By.XPATH, '//a[@href="/DataQualityManagement/"]')
    UsernameBadge = (By.XPATH, "//span[contains(@class, 'cstm-name')]")
