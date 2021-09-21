from pages.search_common import SearchCommon
from workflow.newHome.search_check_results import CheckSearchResults
from pages.newHome.newhome_list_page import NewhomeListPage
from pages.newHome.search_container import SearchContainer
from utils.selenium_utils import SeleniumUtils
from utils.test_utils import TestUtils
from utils.read_json_newhome import JsonReader
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearch:
    testdata = JsonReader.get_search_suggested_cities_data()

    @allure.title("Newhome - search box suggested cities")
    @allure.description("verify: all returned house address must contain the value of var 'searchCity'")
    @pytest.mark.parametrize("searchCity", testdata)
    def atest_search_by_suggested_cities(self, config, searchCity):
        if searchCity == "North York" or searchCity == "Scarborough":
            searchCity = "Toronto"
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_common = SearchCommon(self.driver)
        search_common.click_in_search_box()
        search_common.keep_search_suggest_menu_open()
        city_elements = search_container.get_suggest_cities_elements()
        dropdown_list = TestUtils.get_text_list(city_elements)
        if searchCity not in dropdown_list:
            print("................test data Not in dropdown list: " + searchCity)
            assert False
        # 选择一个筛选项
        TestUtils.click_filter(city_elements, searchCity)
        list_page = NewhomeListPage(self.driver)
        list_page.wait_mapbox_loaded()
        # 拿到列表页里所有的地址elements
        result_list = list_page.get_address_list()
        list_length = len(result_list)
        print(str(list_length) + " ... " + searchCity)
        print("..............*************.........................")
        # 调用 check_city（）来验证结果
        error_counter = CheckSearchResults.check_city(result_list, searchCity)

        assert (error_counter == 0)
