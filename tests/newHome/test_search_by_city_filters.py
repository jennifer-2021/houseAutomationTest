import time
from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
from pages.newHome.search_container import SearchContainer
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearchByCityAndFilters:
    testdata = JsonReader.get_filter_min_price_data()

    @allure.title("Newhome - search - 每个城市 和其对应的每个房型的搜索结果")
    @allure.description("verify: 搜索结果列表页上的 每个房源的 城市地址和房型 必须满足搜索条件")
    @pytest.mark.parametrize("minPrice", testdata)
    def test_search_by_city_with_building_type (self, config, minPrice):
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        # wait for mapbox fully loaded
        search_container.wait_mapbox_loaded()
        # click button to open filter - price / drop down list
        search_container.click_price_button()
        min_price_element_list = search_container.get_min_price_list()
        # get all text from the drop down list
        dropdown_list = SeleniumUtils.get_dropdown_text_list(min_price_element_list)