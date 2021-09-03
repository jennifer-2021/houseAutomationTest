from utils.selenium_utils import SeleniumUtils
from pages.mls.mls_base_page import MlsBasePage
from locators.mls.locators_mls_details import SetMlsDetailsLocators
from utils.test_utils import TestUtils


class MlsDetailsPage(MlsBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_mls_number(self):
        element = self.wait_element(*SetMlsDetailsLocators.mls_name)
        return element.get_attribute('value')