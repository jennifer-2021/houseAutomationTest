from pages.base_page import BasePage
import time
from utils.selenium_utils import SeleniumUtils
from pages.newHome.locators_newhome_details import SetDetailsPageLocators


class NewhomeDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_real_estate_name(self):
        element = self.wait_element(*SetDetailsPageLocators.real_estate_name)
        return SeleniumUtils.get_text_by_element(element)


