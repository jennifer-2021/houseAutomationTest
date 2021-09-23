from pages.search_common import SearchCommon
from pages.HouseHomePage.home_select_city import HouseHomePage
from utils.read_json_house_home import JsonReader
import allure
import pytest


@pytest.mark.usefixtures("home_page_setup")
class TestHotNavigations:

    navidata = JsonReader.get_catalog_data()
    @allure.title("房屋首页 - 测试hot navigation链接跳转正确")
    @allure.description(" 点击hot navigation，验证： 链接跳转正确")
    @pytest.mark.parametrize("catalog", navidata)
    def test_hot_navigations(self, catalog):
        # 1 close the modal window
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        # 2 select an hot navi (catalog)
        house_home_page = HouseHomePage(self.driver)
        house_home_page.select_catalogs(catalog)
        



