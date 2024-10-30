from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.exceptions import ElementNotFoundException, NavigationException
from selenium.webdriver.common.action_chains import ActionChains
import logging
from selenium.common.exceptions import (TimeoutException, ElementNotInteractableException,
                                        ElementClickInterceptedException, WebDriverException)
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.logger = logging.getLogger(type(self).__name__)

    def wait_for_element(self, locator):
        self.logger.info(f"Waiting for element: {locator}")
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f"Element found: {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Error waiting for element: {locator}. Error: {e}, exc_info=True")
            raise ElementNotFoundException(locator)

    # def click(self, by_locator):
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()
    #         self.logger.info(f"Clicked on element with locator: {by_locator}")
    #     except Exception as e:
    #         self.logger.error(f"Error clicking on element with locator: {by_locator}. Error: {e}", exc_info=True)
    def click(self, by_locator):
        try:
            # Wait for the element to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(by_locator)
            )
            # Try using ActionChains to ensure the click works even in headless mode
            ActionChains(self.driver).move_to_element(element).click().perform()
            self.logger.info(f"Clicked on element with locator: {by_locator}")
        except ElementClickInterceptedException as e:
            self.logger.error(f"Element with locator: {by_locator} was not clickable. Retrying... Error: {e}",
                              exc_info=True)
            self.driver.execute_script("arguments[0].click();", element)  # Use JS as a fallback
            self.logger.info(f"Clicked using JavaScript on element with locator: {by_locator}")
        except TimeoutException as e:
            self.logger.error(f"Element with locator: {by_locator} was not found in time. Error: {e}", exc_info=True)
        except WebDriverException as e:
            self.logger.error(f"WebDriver exception occurred. Error: {e}", exc_info=True)
        except Exception as e:
            self.logger.error(f"Unexpected error while clicking element with locator: {by_locator}. Error: {e}",
                              exc_info=True)

    def enter_text(self, by_locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            element.send_keys(text)
            self.logger.info(f"Entered text '{text}' in element with locator: {by_locator}")
        except Exception as e:
            self.logger.error(f"Error entering text in element with locator: {by_locator}. Error: {e}", exc_info=True)

    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(by_locator)
            )
            if element.is_displayed() and element.is_enabled():
                self.logger.info(f"Element with locator: {by_locator} is visible and interactable")
                return True
            else:
                self.logger.warning(f"Element with locator: {by_locator} is present but not interactable")
                return False

        except (TimeoutException, ElementNotInteractableException) as e:
            self.logger.error(f"Element with locator: {by_locator} is not visible or interactable. Error: {e}",
                              exc_info=True)
            return False

        except Exception as e:
            self.logger.error(
                f"Unexpected error occurred while checking visibility of element with locator: {by_locator}. Error: {e}",
                exc_info=True)
            return False

    # def get_element_text(self, by_locator):
    #     try:
    #         element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
    #         text = element.text
    #         self.logger.info(f"Text retrieved from element with locator: {by_locator} is {text}")
    #         return text
    #     except Exception as e:
    #         self.logger.error(f" Error retrieving text from element with locator: {by_locator}. Error: {e}", exc_info=True)
    #         # return ""

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(by_locator)
            )
            # Use JavaScript to fetch text content in case of rendering issues
            text = self.driver.execute_script("return arguments[0].textContent;", element).strip()
            self.logger.info(f"Text retrieved from element with locator: {by_locator} is '{text}'")
            return text
        except Exception as e:
            self.logger.error(f"Error retrieving text from element with locator: {by_locator}. Error: {e}",
                              exc_info=True)
            return ""

    def navigate_to(self, url):
        try:
            self.driver.get(url)
            self.logger.info(f"Navigated to {url}")
        except Exception as e:
            self.logger.error(f" Failed to navigate to {url}, Error: {e}", exc_info=True)
            raise NavigationException(f"Failed to navigate to {url}") from e

    def hover_over_element(self, by_locator):
        try:
            element = self.wait_for_element(by_locator)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info(f"Hovered over element with locator: {by_locator}")
        except Exception as e:
            self.logger.error(f"Error hovering over element with locator: {by_locator}")
            raise e


    def get_page_title(self):
        try:
            page_title = self.driver.title
            return page_title
        except Exception as e:
            self.logger.error(f"Error in fetching the title of the page")
            raise e
