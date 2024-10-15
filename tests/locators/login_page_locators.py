from selenium.webdriver.common.by import By

class LoginPageLocators:
    username = (By.XPATH, '//input[@name="loginfmt"]')
    next = (By.XPATH, '//input[@type="submit"]')
    password = (By.XPATH, '//input[@name="passwd"]')
    signin = (By.XPATH, '//input[@type="submit"]')
    welcomepage = (By.XPATH, '//h1[@class="headingClass"]')