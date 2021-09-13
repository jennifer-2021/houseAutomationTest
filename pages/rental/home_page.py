from pages.rental.rental_base_page import RentalBasePage
from locators.rental.locators_home_page import SetHomePageLocators
from utils.test_utils import TestUtils
from utils.selenium_utils import SeleniumUtils
from time import sleep


class HomePage(RentalBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 区域位置 button
    def click_area_position(self):
        self.wait_element(*SetHomePageLocators.select_area_button).click()

    def get_search_index_list(self):
        return self.driver.find_elements(*SetHomePageLocators.search_index_list)

    def get_search_province_list(self):
        return self.driver.find_elements(*SetHomePageLocators.search_province_list)

    def get_search_city_list(self):
        return self.driver.find_elements(*SetHomePageLocators.search_city_list)

    def select_province(self, province):
        element_list = self.get_search_province_list()
        TestUtils.click_filter(element_list, province)

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
