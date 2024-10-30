import time
import pytest
from tests.locators.welcome_page_locators import WelcomePageLocators
from tests.pages.login_page import LoginPage
import logging
from selenium import webdriver
from tests.utils.logging_config import logging
from tests.pages.welcome_page import WelcomePage
from tests.pages.login_page import LoginPage
from tests.pages.data_quality_management_page import DataQualityManagementPage
from tests.locators.data_quality_management_locators import DataQualityManagementLocators


def test_mouse_hover(browser, config):
   """
   Testcase id: 26869
   Description: Ability to hover over the pages.
   """
   logging.info("Starting testcase id 26869.")
   # TODO optimise the below code and just use assert method here.
   page = WelcomePage(browser)
   page.click_MapLakeview()
   page.is_visible(DataQualityManagementLocators.DQMPageBanner)
   page.hover_over_element(DataQualityManagementLocators.AgencyColumn)
   assert page.is_visible(DataQualityManagementLocators.ToolTip)


def test_username_visible(browser, config):
   """
   Testcase id: 29092
   Description: Ability to visualize the Username and User Image in top right corner.
   """
   logging.info("Starting testcase id 29092.")
   page = WelcomePage(browser)
   username = page.get_element_text(WelcomePageLocators.UsernameBadge)
   app_config = config['app']['username']
   assert app_config.split('@')[0] == username.replace(' ', '')
