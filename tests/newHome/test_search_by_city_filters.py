import time
from utils.selenium_utils import SeleniumUtils
from workflow.newHome.search_check_results import CheckSearchResults
from pages.newHome.newhome_list_page import NewhomeListPage
from utils.read_json_newhome import JsonReader
from pages.newHome.search_container import SearchContainer
from utils.test_utils import TestUtils
from pages.search_common import SearchCommon
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearchByCityAndFilters:
    testdata = JsonReader.get_search_suggested_cities_data()

    @allure.title("Newhome - search - 每个城市 和其对应的每个房型的搜索结果")
    @allure.description("verify: 在搜索结果列表页上的 每个房源的 城市地址和房型描述 必须满足搜索条件")
    @pytest.mark.parametrize("city", testdata)
    def test_search_by_city_with_building_type(self, config, city):
        # 1. 打开 新房 主页
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        # 2 等待 mapbox fully loaded，再点击搜索框
        search_container.wait_mapbox_loaded()
        search_common = SearchCommon(self.driver)
        search_common.click_in_search_box()
        # 3 保持热门城市下拉框 打开
        search_common.keep_search_suggest_menu_open()
        city_elements = search_container.get_suggest_cities_elements()
        dropdown_list = TestUtils.get_text_list(city_elements)
        # 4 如果测试数据/城市 在 下拉框内找不到，测试失败，退出，并打出信息
        if city not in dropdown_list:
            print("................test data Not in dropdown list: " + city)
            assert False
        # 5 点击测试的城市
        TestUtils.click_filter(city_elements, city)

        #  6 如果 "North York" & "Scarborough" - 用 Toronto 来验证地址
        if city == "North York" or city == "Scarborough":
            city = "Toronto"

        # 7 打开房型下拉框
        time.sleep(1)
        search_container.click_building_type_button()
        building_type_element_list = search_container.get_filter_dropdown_element_list()
        error_counter = 0
        # 8 把下拉框内的所有选项 一个个测一遍，"Apartment"除外
        for element in building_type_element_list:

            building_type = SeleniumUtils.get_text_by_element(element)
            print("............building type in test: " + building_type + ".......in: " + city)
            if building_type == "Apartment":
                break
            # 如果是第一个选项，就不再点击，因为已经打开了
            if element is not building_type_element_list[0]:
                search_container.click_building_type_button()
            element.click()
            search_container.wait_mapbox_loaded()
            time.sleep(1)

            # 9 检查列表页里所有的房源：地址和房型 必须符合 测试数据
            list_page = NewhomeListPage(self.driver)
            search_result_address_element_list = list_page.get_address_list()
            search_result_building_type_element_list = list_page.get_building_type_list()
            address_on_result = ""

            for address_element in search_result_address_element_list:
                address_on_result = SeleniumUtils.get_text_by_element(address_element)
                if city not in address_on_result:
                    print("..................error address in test: " + address_on_result)
                    error_counter += 1

            if building_type != "不限":
                for building_type_element in search_result_building_type_element_list:
                    building_type_on_result = SeleniumUtils.get_text_by_element(building_type_element)
                    if building_type not in building_type_on_result:
                        print(".................. error address in test: " + address_on_result)
                        error_counter += 1
        assert error_counter == 0
