from utils.selenium_utils import SeleniumUtils
from pages.mls.mls_base_page import MlsBasePage
from locators.mls.locators_mls_list import SetMlsListLocators
from locators.mls.locators_mls_map import SetMlsMapLocators
from utils.test_utils import TestUtils


class MlsListMap(MlsBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # days_on_market_options
    def get_days_on_market_element_list(self):
        return self.driver.find_elements(*SetMlsMapLocators.days_on_market_list)

    # click days_on_market_options button
    def click_days_on_market_option_button(self, transaction):
        if transaction == "出售" or transaction == "出租":
            self.wait_element(*SetMlsMapLocators.days_on_market_button).click()
        else:
            self.wait_element(*SetMlsMapLocators.sold_days_on_market_button).click()

    # select
    def select_transaction_type(self, transaction):
        element_list = self.driver.find_elements(*SetMlsMapLocators.transaction_checkbox_list)
        TestUtils.click_filter(element_list, transaction)

    # get days_on_market list - return list[str]
    def get_days_on_market_option_list(self, transaction):
        self.click_days_on_market_option_button(transaction)
        element_list = self.get_days_on_market_element_list()
        return TestUtils.get_text_list(element_list)
