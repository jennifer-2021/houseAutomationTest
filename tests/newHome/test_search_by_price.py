import time
from utils.selenium_utils import SeleniumUtils
from pages.search_common import SearchCommon
from utils.read_json_newhome import JsonReader
from pages.newHome.search_container import SearchContainer
from utils.test_utils import TestUtils
from pages.newHome.newhome_list_page import NewhomeListPage
import allure
import pytest
from workflow.newHome.search_check_results import CheckSearchResults


@pytest.mark.usefixtures("setup")
class TestSearchByPrice:
    testdata = JsonReader.get_filter_min_price_data()

    @allure.title("Newhome - search - filter - price range")
    @allure.description("verify: all returned house price must meet the filter 'price' ")
    @pytest.mark.parametrize("minPrice", testdata)
    def test_search_by_building_type(self, config, minPrice):
        if minPrice == "不限" or minPrice == "$100,000" or minPrice == "$200,000":
            return
        # 1 打开 新房首页
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        # 2 等待 mapbox fully loaded
        search_container.wait_mapbox_loaded()
        # 3 点击 价格 button， 显示所有价格后，把它们的页面元素放到 min_price_element_list 里面
        search_container.click_price_button()
        min_price_element_list = search_container.get_min_price_list()
        # 4 把所有的价格提取出来，放到 dropdown_list
        dropdown_list = TestUtils.get_text_list(min_price_element_list)
        # 5 如果 测试数据 minPrice 没有在 下拉框里，测试失败，打印错误价格，退出
        if minPrice not in dropdown_list:
            print("................test data Not in dropdown list: " + minPrice)
            assert False

        # 6 点击测试价格，作为起初价格 - min price
        TestUtils.click_filter(min_price_element_list, minPrice)

        # 7 最高价格显示后，把把它们的页面元素放到 max_price_element_list 里面
        max_price_element_list = search_container.get_max_price_list()
        # 8 提出最高价格 的第一个值 - integer 格式
        max_price_text = SeleniumUtils.get_text_by_element(max_price_element_list[1])
        max_price_int = TestUtils.get_price_int(max_price_text)
        # 9 把价格最低价转换成 Integer: i.e $1,000,000 to 1000000
        minPrice = TestUtils.get_price_int(minPrice)

        # 10 点击第二个值 （第一个为：不限）
        max_price_element_list[1].click()

        time.sleep(3)
        # 11 在搜索结果列表页，把所有房源的价格 的元素 放到 result_element_list
        list_page = NewhomeListPage(self.driver)
        result_element_list = list_page.get_price_list()
        # 12 验证 每个房源显示的价格范围 是否符合测试数据， 如果验证失败，跳出，并打印出房源地址
        check_result = CheckSearchResults(self.driver)
        error_counter = check_result.check_price(result_element_list, minPrice, max_price_int)

        assert error_counter == 0
