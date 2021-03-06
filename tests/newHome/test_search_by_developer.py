from utils.selenium_utils import SeleniumUtils
from utils.read_json_newhome import JsonReader
from pages.newHome.search_container import SearchContainer
from pages.search_common import SearchCommon
from pages.newHome.developer_details_page import DeveloperPage
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearchByDeveloper:
    testdata = JsonReader.get_developer_data()

    @allure.title("新房 - 搜索 - 按开发商")
    @allure.description("验证结果: 进入楼盘详情页，实际开发商与期待结果一样")
    @pytest.mark.parametrize("developer", testdata)
    def test_search_by_real_estate(self, config, developer):
        # 1. 打开 新房 主页
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)

        # 2 搜索框 - 输入开发商名 - 点击进入详情页
        main_window = self.driver.current_window_handle
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        search_common.set_search_box_input(developer)
        search_container.click_suggest()

        # 3 检查开发商详情页：开发商名称
        SeleniumUtils.switch_to_window(self, main_window)
        developer_page = DeveloperPage(self.driver)
        actual_developer = developer_page.get_developer_name()
        actual_developer = actual_developer.strip()

        if actual_developer != developer:
            print("........actual: " + actual_developer + "... expected: " + developer)
            print("....actual url: " + self.driver.current_url)
            assert False

        assert True
