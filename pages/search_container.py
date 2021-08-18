from pages.locators_search_container import SetSearchHouseLocators
from pages.base_page import BasePage
from utils.selenium_utils import SeleniumUtils


class SearchContainer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_search_box_dropdown_list(self):
        self.wait_element(*SetSearchHouseLocators.search_box).click()

    def set_search_box_input(self, searchKey):
        self.wait_element(*SetSearchHouseLocators.search_box).send_keys(searchKey)

    def click_search_box_button(self):
        self.driver.find_element(*SetSearchHouseLocators.search_button).click()

    def get_filter_box(self):
        utils = SeleniumUtils(self.driver)
        return utils.get_text(*SetSearchHouseLocators.filter_box_city)

    def keep_open_search_suggest_menu(self):
        self.wait_element(*SetSearchHouseLocators.search_box_suggest_menu)
