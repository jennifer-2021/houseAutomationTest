import time

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

    # get school filter - grade list
    def get_grade_filter_element_list(self):
        return self.driver.find_elements(*SetMlsMapLocators.school_filter_grade_list)

    # get school filter - score list
    def get_score_element_list(self):
        return self.driver.find_elements(*SetMlsMapLocators.school_filter_score_list)

    # click school filter - submit button
    def click_open_school_filter(self):
        self.wait_element(*SetMlsMapLocators.school_filter_toggle).click()

    # click school filter - submit button
    def click_school_filter_submit(self):
        self.wait_element(*SetMlsMapLocators.school_filter_submit).click()

    # get school search result - grade list[str]
    def get_grade_elementary_result_list(self):
        element_list = self.get_grade_elementary_element_list()
        return TestUtils.get_text_list(element_list)

    # get school search result - grade list[element]
    def get_grade_elementary_element_list(self):
        return self.driver.find_elements(*SetMlsMapLocators.school_elementary_label)

    # get school search result - grade list[element]
    def get_grade_middle_element_list(self):
        return self.driver.find_elements(*SetMlsMapLocators.school_elementary_label)

    # get school search result - grade list[element]
    def get_high_school_element_list(self):
        return self.driver.find_elements(*SetMlsMapLocators.school_high_school_label)

    # get school search result - grade list[str]
    def get_grade_middle_result_list(self):
        element_list = self.get_grade_middle_element_list()
        return TestUtils.get_text_list(element_list)

    # get school search result - grade list[str]
    def get_score_result_list(self):
        element_list = self.driver.find_elements(*SetMlsMapLocators.school_filter_score_label)
        return TestUtils.get_text_list(element_list)

    # school filter - select a grade
    def select_school_grade(self, grade):
        self.click_open_school_filter()
        element_list = self.get_grade_filter_element_list()
        TestUtils.click_filter(element_list, grade)
        self.click_school_filter_submit()
        time.sleep(1)

    # school filter - select a score
    def select_school_score(self, score):
        self.click_open_school_filter()
        element_list = self.get_score_element_list()

        TestUtils.click_filter_by_attribute(element_list, score, "label")
        self.click_school_filter_submit()
        time.sleep(1)
