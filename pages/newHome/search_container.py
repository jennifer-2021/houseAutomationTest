import time

from pages.newHome.locators_search_container import SetSearchHouseLocators
from pages.base_page import BasePage
from utils.selenium_utils import SeleniumUtils


class SearchContainer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # click inside the search box to open suggest dropdown list
    def click_in_search_box(self):
        self.wait_mapbox_loaded()
        self.wait_element(*SetSearchHouseLocators.search_box).click()
        self.wait_element(*SetSearchHouseLocators.search_box_suggest_menu)

    # return a list of cities
    def get_suggest_cities_elements(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_box_suggest_city_list)

    # all houses address on the list page
    def get_search_result_address_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_result_address_list)

    # all houses address on the list page
    def get_result_real_estate_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_result_real_estate_list)

    # all houses building type on the list page
    def get_search_result_building_type_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_result_building_type_list)

    # all houses checkin time on the list page
    def get_search_result_checkin_time_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_result_checkin_time_list)

    # all houses price on the list page
    def get_search_result_price_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_result_price_list)

    def set_search_box_input(self, searchKey):
        self.wait_element(*SetSearchHouseLocators.search_box).send_keys(searchKey)
        return self

    def click_search_box_button(self):
        self.driver.find_element(*SetSearchHouseLocators.search_button).click()

    # keep search box - drop down list open
    def keep_search_suggest_menu_open(self):
        elem = self.wait_element(*SetSearchHouseLocators.search_box_suggest_menu)
        self.driver.execute_script("arguments[0].setAttribute('style', " + "'display: block')", elem)
        return self

    # click 'building type' button
    def click_building_type_button(self):
        self.wait_element(*SetSearchHouseLocators.filter_building_type_button).click()

    # filter - drop down - element list for both 'building type' & 入住时间
    def get_filter_dropdown_element_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.filter_drop_down_list)

    def wait_mapbox_loaded(self):
        time.sleep(3)
        self.wait_element(*SetSearchHouseLocators.map_box_points)
        time.sleep(3)

    def click_checkin_time_button(self):
        self.wait_element(*SetSearchHouseLocators.filter_check_in_time).click()

    # click 'building type' button
    def click_price_button(self):
        self.wait_element(*SetSearchHouseLocators.filter_price_range_button).click()

    # get 'min price' drop down element list
    def get_min_price_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.filter_min_price_list)

    # get 'max price' drop down element list
    def get_max_price_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.filter_max_price_list)


