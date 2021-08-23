import time
from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
from pages.newHome.search_container import SearchContainer
import allure
import pytest
from pages.newHome.search_check_results import CheckSearchResults


@pytest.mark.usefixtures("setup")
class TestSearchByPrice:
    testdata = JsonReader.get_filter_min_price_data()

    @allure.title("Newhome - search - filter - price range")
    @allure.description("verify: all returned house price must meet the filter 'price' ")
    @pytest.mark.parametrize("minPrice", testdata)
    def test_search_by_building_type(self, config, minPrice):
        if minPrice == "不限":
            return
        # 1 打开 新房首页
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        # 2 等待 mapbox fully loaded
        search_container.wait_mapbox_loaded()
        # 3 点击 价格 button， 显示所有价格后，把它们的页面元素放到 min_price_element_list 里面
        search_container.click_price_button()
        min_price_element_list = search_container.get_min_price_list()
        # 4 把所有的价格提取出来，放到 dropdown_list
        dropdown_list = SeleniumUtils.get_dropdown_text_list(min_price_element_list)
        # 5 如果 测试数据 minPrice 没有在 下拉框里，测试失败，打印错误价格，退出
        if minPrice not in dropdown_list:
            print("................test data Not in dropdown list: " + minPrice)
            assert False

        # 6 点击测试价格，作为起初价格 - min price
        CheckSearchResults.click_filter(min_price_element_list, minPrice)

        # 7 最高价格显示后，把把它们的页面元素放到 max_price_element_list 里面
        max_price_element_list = search_container.get_max_price_list()
        # 8 提出最高价格 的第一个值 - integer 格式
        max_price_text = SeleniumUtils.get_text_by_element(max_price_element_list[1])
        max_price_int = SeleniumUtils.get_start_price(max_price_text)
        # 9 把价格最低价转换成 Integer: i.e $1,000,000 to 1000000
        minPrice = SeleniumUtils.get_start_price(minPrice)

        # 10 点击第二个值 （第一个为：不限）
        max_price_element_list[1].click()

        time.sleep(3)
        # 11 在搜索结果列表页，把所有房源的价格 的元素 放到 result_element_list
        result_element_list = search_container.get_search_result_price_list()
        # 12 验证 每个房源显示的价格范围 是否符合测试数据， 如果验证失败，跳出，并打印出房源地址
        check_result = CheckSearchResults(self.driver)
        price_in_range = check_result.check_price(result_element_list, minPrice, max_price_int)
        if not price_in_range:
            assert False

        assert True
