from selenium.webdriver.common.by import By

class WelcomePageLocators:
    #TODO Optimize the below locator
    MapLakeViewButton = (By.XPATH, "(//div[contains(@class, 'card boxStyle pointer')])[1]")
    UsernameBadge = (By.XPATH, "//span[contains(@class, 'cstm-name')]")