import time
from utils.selenium_utils import SeleniumUtils
from utils.read_json_newhome import JsonReader
from pages.newHome.search_container import SearchContainer
import allure
import pytest
from workflow.newHome.search_check_results import CheckSearchResults
from pages.newHome.newhome_list_page import NewhomeListPage


@pytest.mark.usefixtures("setup")
class TestSearchByAllFilters:
    testdata = JsonReader.get_search_city_with_filters()

    @allure.title("Newhome - 测试搜索结果 - 条件：城市 & 房型 & 入住时间 & 价格")
    @allure.description("verify: 在搜索结果列表页上的 每个房源的 城市 & 房型 & 入住时间 & 价格 必须满足搜索条件")
    @pytest.mark.parametrize("testObject", testdata)
    def test_search_all_conditions(self, config, testObject):
        city = testObject["city"]
        buildingType = testObject["buildingType"]
        checkinTime = testObject["checkinTime"]
        minPrice = testObject["minPrice"]
        maxPrice = testObject["maxPrice"]
        # 1. 打开 新房 主页
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        # 2 点击搜索框
        search_container.click_in_search_box()
        # 3 保持热门城市下拉框 打开
        search_container.keep_search_suggest_menu_open()
        city_elements = search_container.get_suggest_cities_elements()
        dropdown_list = SeleniumUtils.get_text_list(city_elements)
        # 4 如果测试数据/城市 在 下拉框内找不到，测试失败，退出，并打出信息
        if city not in dropdown_list:
            print("................test data Not in dropdown list: " + city)
            assert False
        # 5 点击测试的城市
        CheckSearchResults.click_filter(city_elements, city)
        search_container.wait_mapbox_loaded()

        #  6 如果 "North York" & "Scarborough" - 用 Toronto 来验证地址
        if city == "North York" or city == "Scarborough":
            city = "Toronto"

        # 7 打开房型下拉框
        time.sleep(1)
        search_container.click_building_type_button()
        building_type_element_list = search_container.get_filter_dropdown_element_list()
        # 8 在下拉框内点击房型
        CheckSearchResults.click_filter(building_type_element_list, buildingType)
        search_container.wait_mapbox_loaded()

        # 9 在下拉框内点击入住时间
        search_container.click_checkin_time_button()
        checkin_time_element_list = search_container.get_filter_dropdown_element_list()
        CheckSearchResults.click_filter(checkin_time_element_list, checkinTime)
        search_container.wait_mapbox_loaded()

        # 10 在下拉框内点击价格
        search_container.click_price_button()
        price_min_element_list = search_container.get_min_price_list()
        CheckSearchResults.click_filter(price_min_element_list, minPrice)

        # 10.2 点击最高价格
        price_max_element_list = search_container.get_max_price_list()
        CheckSearchResults.click_filter(price_max_element_list, maxPrice)
        search_container.wait_mapbox_loaded()

        # 11 检查列表页里所有的房源：地址和房型 必须符合 测试数据
        list_page = NewhomeListPage(self.driver)
        address_element_list = list_page.get_address_list()
        building_type_element_list = list_page.get_building_type_list()
        checkin_time_element_list = list_page.get_checkin_time_list()
        price_element_list = list_page.get_price_list()

        unexpected_result = CheckSearchResults.check_city(address_element_list, city)

        check_result = CheckSearchResults(self.driver)
        unexpected_result += check_result.check_building_type(building_type_element_list, buildingType)

        unexpected_result += check_result.checkin_time_on_list(checkin_time_element_list, checkinTime)

        minPrice = SeleniumUtils.get_price_int(minPrice)
        maxPrice = SeleniumUtils.get_price_int(maxPrice)
        unexpected_result += check_result.check_price(price_element_list, minPrice, maxPrice)

        assert unexpected_result == 0
