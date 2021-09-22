import time
from utils.test_utils import TestUtils
from utils.selenium_utils import SeleniumUtils
from utils.read_json_newhome import JsonReader
from pages.newHome.search_container import SearchContainer
from pages.newHome.newhome_list_page import NewhomeListPage
from pages.search_common import SearchCommon
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearchByAddress:
    testdata = JsonReader.get_address_data()

    @allure.title("新房 - 搜索 - 按地址")
    @allure.description(
        "验证结果: 1. 如果返回空页面，则验证失败 2. 如果返回的房源和期待的测试结果不同，打印出错房源所有信息，继续验证所有的房源，最后跳出。注意：如果有新的房源，也会报错，只需加上新的房源就可以")
    @pytest.mark.parametrize("addressObject", testdata)
    def test_search_by_address(self, config, addressObject):
        address = addressObject["address"]
        expected = addressObject["expected"]
        # 1. 打开 新房 主页
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)

        # 2 搜索框 - 输入地址 - 点击搜索
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        search_common.set_search_box_input(address)
        search_common.click_search_box_button()
        time.sleep(5)

        # 3 检查列表页里所有的房源：楼盘名称
        list_page = NewhomeListPage(self.driver)
        result_element_list = list_page.get_real_estate_list()
        if len(result_element_list) == 0:
            print("...........actual result: 0..............")
            assert False
        unexpected_result = 0
        actual_list = TestUtils.get_text_list(result_element_list)
        for expect in expected:
            if expect not in actual_list:
                print("...this real estate should be on the page, but not...." + expect)
                unexpected_result = unexpected_result + 1

        assert (unexpected_result == 0)



