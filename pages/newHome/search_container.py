from pages.newHome.locators_search_container import SetSearchHouseLocators
from pages.base_page import BasePage
from utils.selenium_utils import SeleniumUtils


class SearchContainer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # click inside the search box to open suggest dropdown list
    def click_in_search_box(self):
        self.wait_element(*SetSearchHouseLocators.search_box).click()
        self.wait_element(*SetSearchHouseLocators.search_box_suggest_menu)

    # return a list of cities
    def get_suggest_cities_elements(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_box_suggest_cities)

    def get_search_result_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_result_list)

    def set_search_box_input(self, searchKey):
        self.wait_element(*SetSearchHouseLocators.search_box).send_keys(searchKey)
        return self

    def click_search_box_button(self):
        self.driver.find_element(*SetSearchHouseLocators.search_button).click()

    def get_filter_box(self):
        utils = SeleniumUtils(self.driver)
        return utils.get_text(*SetSearchHouseLocators.filter_box_city)

    def keep_search_suggest_menu_open(self):
        elem = self.wait_element(*SetSearchHouseLocators.search_box_suggest_menu)
        self.driver.execute_script("arguments[0].setAttribute('style', " + "'display: block')", elem)
        return self
