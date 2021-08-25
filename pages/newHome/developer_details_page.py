from pages.base_page import BasePage
import time
from utils.selenium_utils import SeleniumUtils
from pages.newHome.locators_developer_details import SetDeveloperPageLocators


class DeveloperPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_developer_name(self):
        element = self.wait_element(*SetDeveloperPageLocators.developer_name)
        return SeleniumUtils.get_text_by_element(element)
