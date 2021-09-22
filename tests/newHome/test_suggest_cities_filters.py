from pages.newHome.search_container import SearchContainer
from utils.selenium_utils import SeleniumUtils
from utils.read_json_newhome import JsonReader
from utils.test_utils import TestUtils
from pages.search_common import SearchCommon
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSuggestedCityAndFilter:

    @allure.title("新房 - 热门城市")
    @allure.description("verify: 热门城市 的下拉框的内容正确")
    def test_filter_suggested_city(self, config):
        testdata = JsonReader.get_search_suggested_cities_data()
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        search_common.clear_search_box()
        search_common.click_in_search_box()
        city_element_list = search_container.get_suggest_cities_elements()
        city_list = TestUtils.get_text_list(city_element_list)

        print("..........actual drop down list..............")
        print(city_list)
        assert testdata == city_list

    @allure.title("新房 - 筛选条件 - 房型")
    @allure.description("verify: 房型 的下拉框的内容正确")
    def test_filter_by_building_type(self, config):
        testdata = JsonReader.get_filter_building_type_data()
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        search_container.click_building_type_button()
        building_type_element_list = search_container.get_filter_dropdown_element_list()
        building_type_list = TestUtils.get_text_list(building_type_element_list)

        print("..........actual drop down list..............")
        print(building_type_list)
        assert testdata == building_type_list

    @allure.title("新房 - 筛选条件 - 入住时间")
    @allure.description("verify: 入住时间 的下拉框的内容正确")
    def test_filter_checkin_time(self, config):
        testdata = JsonReader.get_filter_checkin_time_data()
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        search_container.click_checkin_time_button()
        checkin_time_element_list = search_container.get_filter_dropdown_element_list()
        checkin_time_list = TestUtils.get_text_list(checkin_time_element_list)

        print("..........actual drop down list..............")
        print(checkin_time_list)
        assert testdata == checkin_time_list

    @allure.title("新房 - 筛选条件 - 价格")
    @allure.description("verify: 价格 的下拉框的内容正确")
    def test_filter_price(self, config):
        testdata = JsonReader.get_filter_min_price_data()
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        search_container.click_price_button()
        price_element_list = search_container.get_min_price_list()
        price_list = TestUtils.get_text_list(price_element_list)

        print("..........actual drop down list..............")
        print(price_list)
        assert testdata == price_list
