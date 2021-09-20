from pages.HouseHomePage.home_base_page import HomeBasePage
from locators.HouseHomePage.locators_house_home_page import SetHouseHomePageLocators
from utils.test_utils import TestUtils
from time import sleep


class HouseHomePage(HomeBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_select_city_button(self):
        try:
            self.wait_element(*SetHouseHomePageLocators.select_area_modal)
        except:
            self.wait_element(*SetHouseHomePageLocators.select_city_open_button).click()

    def get_province_element_list(self):
        return self.driver.find_elements(*SetHouseHomePageLocators.province_list)

    def get_city_element_list(self):
        return self.driver.find_elements(*SetHouseHomePageLocators.city_list)

    def select_province(self, province):
        element_list = self.get_province_element_list()
        TestUtils.click_filter(element_list, province)

    def select_city(self, city):
        element_list = self.get_city_element_list()
        TestUtils.click_filter(element_list, city)
        sleep(1)

    def get_city_en_list(self):
        en_list = []
        element_list = self.get_city_element_list()
        list = TestUtils.get_text_list(element_list)
        for city in list:
            city = city.split("<div")[0]
            en_list.append(city)
        return en_list

    def get_province_en_list(self):
        element_list = self.get_province_element_list()
        return TestUtils.get_text_list(element_list)

    def select_catalogs(self, catalog):
        element_list = self.wait_element(*SetHouseHomePageLocators.hot_nav_list)
        TestUtils.click_filter(element_list, catalog)