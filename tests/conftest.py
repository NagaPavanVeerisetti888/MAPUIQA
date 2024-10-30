import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    headless = config['browser'].get('headless', True)
    try:
        logging.debug(f"Setting up the browser: {browser_type}, headless: {headless}")
        if browser_type == "chrome":
            options = Options()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
        elif browser_type == "firefox":
            driver = webdriver.Firefox
        elif browser_type == "edge":
            driver = webdriver.Edge()
        else:
            raise Exception(f"Unsupported browser: {browser_type}")

        driver.maximize_window()
        yield driver
    except Exception as e:
        logging.error("An error occurred while setting up the browser", exc_info=True)
        raise e
    finally:
        logging.info("quitting browser")
        driver.quit()


@pytest.fixture(scope="session", autouse=True)
def login(browser, config):
    logging.info("Starting login process")
    try:
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
    except Exception as e:
        logging.error("An error occurred during the login.", exc_info=True)
        raise e
