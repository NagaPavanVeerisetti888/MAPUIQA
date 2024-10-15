import pytest
import yaml
from selenium import webdriver
from tests.pages.login_page import LoginPage
import logging
import time


def load_config():
    # TODO need to fix the config.yaml path issue
    with open(r"tests/config.yaml", "r") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture(scope="session")
def browser(config):
    browser_type = config['browser']['type']
    if browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox":
        driver = webdriver.Firefox
    elif browser_type == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception(f"Unsupported browser: {browser_type}")

    driver.maximize_window()
    yield driver
    logging.info("Quitting browser")
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def login(browser, config):
    logging.info("Starting login process")
    page = LoginPage(browser)
    app_config = config['app']
    browser.get(app_config['url'])
    page.enter_username(app_config['username'])
    page.click_next()
    page.enter_password(app_config['password'])
    page.click_signin()
    time.sleep(5)
    # assert page.verify_welcome_page() == "Welcome to Lakeview"
    logging.info("Login Successful")