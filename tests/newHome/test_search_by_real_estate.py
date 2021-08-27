from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
from pages.newHome.search_container import SearchContainer
from pages.newHome.real_estate_details_page import NewhomeDetailsPage
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearchByRealEstate:
    testdata = JsonReader.get_real_estate_data()

    @allure.title("新房 - 搜索 - 按楼盘")
    @allure.description("验证结果: 进入楼盘详情页，实际楼盘名与期待结果一样")
    @pytest.mark.parametrize("real_estate", testdata)
    def test_search_by_real_estate(self, config, real_estate):
        # 1. 打开 新房 主页
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)

        # 2 搜索框 - 输入楼盘名 - 点击搜索
        main_window = self.driver.current_window_handle
        search_container.set_search_box_input(real_estate)
        search_container.click_real_estate_suggest()

        # 3 检查楼盘详情页：楼盘名称
        SeleniumUtils.switch_to_window(self, main_window)
        details_page = NewhomeDetailsPage(self.driver)
        actual_page_title = details_page.get_real_estate_name()
        if actual_page_title != real_estate:
            print("........actual: " + actual_page_title + "... expected: " + real_estate)
            print("....actual url: " + self.driver.current_url)
            assert False

        assert True


