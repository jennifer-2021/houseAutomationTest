from pages.rental.rental_base_page import RentalBasePage
from locators.rental.locators_home_page import SetHomePageLocators
from utils.test_utils import TestUtils
from utils.selenium_utils import SeleniumUtils
from time import sleep


class HomePage(RentalBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # index - catalogs
    def select_catalog(self, catalog):
        element_list = self.driver.find_elements(*SetHomePageLocators.catalog_index_list)
        TestUtils.click_filter(element_list, catalog)

    # 区域位置 button
    def click_area_position(self):
        self.wait_element(*SetHomePageLocators.select_area_button).click()

    def click_subway_catalog(self):
        self.wait_element(*SetHomePageLocators.search_subway_catalog).click()

    def click_university_catalog(self):
        self.wait_element(*SetHomePageLocators.search_university_catalog).click()

    def click_search_by_map_catalog(self):
        self.wait_element(*SetHomePageLocators.search_by_map_catalog).click()

    def submit_search_by_map(self):
        self.wait_element(*SetHomePageLocators.map_search_submit).click()
        sleep(1)

    def dismiss_search_by_map(self):
        self.wait_element(*SetHomePageLocators.map_search_dismiss).click()

    def get_search_index_list(self):
        return self.driver.find_elements(*SetHomePageLocators.search_index_list)

    def get_search_province_list(self):
        return self.driver.find_elements(*SetHomePageLocators.search_province_list)

    def get_search_city_list(self):
        return self.driver.find_elements(*SetHomePageLocators.search_city_list)

    def select_province(self, province):
        element_list = self.get_search_province_list()
        TestUtils.click_filter(element_list, province)

    def get_all_provinces(self):
        element_list = self.get_search_province_list()
        return TestUtils.get_text_list(element_list)

    def get_all_cities(self):
        element_list = self.get_search_city_list()
        return TestUtils.get_text_list(element_list)

    def is_search_panel_open(self):
        try:
            self.wait_element(*SetHomePageLocators.search_city_col)
            return True
        except:
            return False

    def select_city(self, city):

        if not self.is_search_panel_open():
            self.click_area_position()

        element_list = self.get_search_city_list()
        TestUtils.click_filter(element_list, city)
        sleep(3)

    # return list[str]
    def get_10_20_ads_address(self):
        addr_list = []
        element_list = self.driver.find_elements(*SetHomePageLocators.ads_10_20_address)
        list = TestUtils.get_text_list(element_list)
        for addr in list:
            addr = addr.split("(")[0]
            addr_list.append(addr.rstrip())
        return addr_list

    # return list[str]
    def get_rental_list_address(self):
        addr_list = []
        element_list = self.driver.find_elements(*SetHomePageLocators.rental_list_address)
        list = TestUtils.get_text_list(element_list)
        for addr in list:
            addr = addr.split(" (")[0]
            addr_list.append(addr.rstrip())
        return addr_list
