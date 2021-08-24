import time
from pages.newHome.search_check_results import CheckSearchResults
from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
from pages.newHome.search_container import SearchContainer
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearchByAddress:
    testdata = JsonReader.get_address_data()

    @allure.title("新房 - 搜索 - 按地址")
    @allure.description("验证结果: 1. 如果返回空页面，则验证失败 2. 如果返回的房源和期待的测试结果不同，打印出错房源所有信息，继续验证所有的房源，最后跳出。注意：如果有新的房源，也会报错，只需加上新的房源就可以")
    @pytest.mark.parametrize("addressObject", testdata)
    def test_search_by_address(self, config, addressObject):
        address = addressObject["address"]
        expected = addressObject["expected"]
        # 1. 打开 新房 主页
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.open_home_page(config)
        # 2 搜索框 - 输入地址 - 点击搜索
        search_container.set_search_box_input(address)
        search_container.click_search_box_button()
        search_container.wait_mapbox_loaded()

        # 3 检查列表页里所有的房源：楼盘名称
        result_element_list = search_container.get_result_real_estate_list()
        if len(result_element_list) == 0:
            print("...........actual result: 0..............")
            assert False
        unexpected_result = 0
        for element in result_element_list:
            name = SeleniumUtils.get_text_by_element(element)
            if name not in expected:
                self.print_error_message(name, element)
                unexpected_result = unexpected_result + 1

        assert (unexpected_result == 0)

    # 4 打印出错房源所有信息
    def print_error_message(self, real_estate_name, anchor_element):
        developer_element = SeleniumUtils.get_next_sibling_element(self, anchor_element)
        info_element = SeleniumUtils.get_next_sibling_element(self, developer_element)
        building_type_element = SeleniumUtils.get_first_child_element(self, info_element)
        address_element = SeleniumUtils.get_next_sibling_element(self, info_element)
        developer = SeleniumUtils.get_text_by_element(developer_element)
        building_type = SeleniumUtils.get_text_by_element(building_type_element)
        address = SeleniumUtils.get_text_by_element(address_element)
        print("..................error real-estate info...................")
        print(real_estate_name)
        print(developer)
        print(building_type)
        print(address)
