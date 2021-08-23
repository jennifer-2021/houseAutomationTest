from pages.newHome.search_container import SearchContainer
from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
import allure
import pytest
import time
import re


@pytest.mark.usefixtures("setup")
class TestSuggestedCityAndFilter:

    @allure.title("新房 - 热门城市")
    @allure.description("verify: 热门城市 的下拉框的内容正确")
    def test_filter_suggested_city(self, config):
        testdata = JsonReader.get_search_suggested_cities_data()
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.click_in_search_box()
        city_element_list = search_container.get_suggest_cities_elements()
        city_list = []
        for element in city_element_list:
            city = SeleniumUtils.get_text_by_element(element)
            city_list.append(city)
        print("..........actual drop down list..............")
        print(city_list)
        assert testdata == city_list

    @allure.title("新房 - 筛选条件 - 房型")
    @allure.description("verify: 房型 的下拉框的内容正确")
    def test_filter_by_building_type(self, config):
        testdata = JsonReader.get_filter_building_type_data()
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.click_building_type_button()
        building_type_element_list = search_container.get_filter_dropdown_element_list()
        building_type_list = []
        for element in building_type_element_list:
            building_type = SeleniumUtils.get_text_by_element(element)
            building_type_list.append(building_type)
        print("..........actual drop down list..............")
        print(building_type_list)
        assert testdata == building_type_list

    @allure.title("新房 - 筛选条件 - 入住时间")
    @allure.description("verify: 入住时间 的下拉框的内容正确")
    def test_filter_checkin_time(self, config):
        testdata = JsonReader.get_filter_checkin_time_data()
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.click_checkin_time_button()
        checkin_time_element_list = search_container.get_filter_dropdown_element_list()
        checkin_time_list = []
        for element in checkin_time_element_list:
            checkin_time = SeleniumUtils.get_text_by_element(element)
            checkin_time_list.append(checkin_time)
        print("..........actual drop down list..............")
        print(checkin_time_list)
        assert testdata == checkin_time_list

    @allure.title("新房 - 筛选条件 - 价格")
    @allure.description("verify: 价格 的下拉框的内容正确")
    def test_filter_price(self, config):
        testdata = JsonReader.get_filter_min_price_data()
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.click_price_button()
        price_element_list = search_container.get_min_price_list()
        price_list = []
        for element in price_element_list:
            price = SeleniumUtils.get_text_by_element(element)
            price_list.append(price)
        print("..........actual drop down list..............")
        print(price_list)
        assert testdata == price_list
