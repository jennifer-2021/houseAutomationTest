from pages.search_common import SearchCommon
from pages.mls.search_mls_container import SearchMlsContainer
from utils.selenium_utils import SeleniumUtils
from pages.mls.mls_details_page import MlsDetailsPage
from utils.read_json_mls import JsonReader
from utils.test_utils import TestUtils
import allure
import pytest


@pytest.mark.usefixtures("mls_setup")
class TestSearch:
    testdata = JsonReader.get_mls_suggested_cities_data()

    @allure.title("二手房 - 搜索框热门城市")
    @allure.description("验证: 点击每个热门城市，根据返回的页面url,确认城市名称，location_id")
    @pytest.mark.parametrize("cityObject", testdata)
    def test_suggested_cities(self, config, cityObject):
        # 1 open mls home page
        city = cityObject["city"]
        expected = cityObject["url"]
        search_mls_container = SearchMlsContainer(self.driver)
        # 2 click on search box to open the drop down list
        search_common = SearchCommon(self.driver)
        search_common.click_in_search_box()
        # 3 get and click the actual cities in search drop down list
        suggest_city_element_list = search_mls_container.get_suggest_cities_elements()
        TestUtils.click_filter(suggest_city_element_list, city)
        # 4 verify url
        search_mls_container.wait_mapbox_loaded()
        url = self.driver.current_url
        actual_result = TestUtils.parse_url_get_dict(url)
        print("actual result..." + str(actual_result))
        print("expected..." + str(expected))
        assert expected == actual_result

    searchKeydata = JsonReader.get_mls_search_data()

    @allure.title("二手房 - 搜索框 - 按地址，邮编")
    @allure.description("验证: 按地址，邮编搜索，根据返回的页面url,确认地址，邮编")
    @pytest.mark.parametrize("searchObject", searchKeydata)
    def test_search_by_keys(self, config, searchObject):
        address = searchObject["address"]
        expected = searchObject["url"]
        # 1 open mls home page
        search_mls_container = SearchMlsContainer(self.driver)
        # 2 click on search box to open the drop down list
        search_common = SearchCommon(self.driver)
        search_common.set_search_box_input(address)
        search_mls_container.click_activated_suggest()
        search_mls_container.wait_mapbox_loaded()
        # 3 verify url
        url = self.driver.current_url
        actual_result = TestUtils.parse_url_get_dict(url)
        print("actual result..." + str(actual_result))
        print("expected..." + str(expected))
        assert expected == actual_result

    searchByMlsdata = JsonReader.get_search_by_mls_data()

    @allure.title("二手房 - 搜索框 - 按mls")
    @allure.description("验证: 按mls搜索，确认打开房源页面")
    @pytest.mark.parametrize("mls", searchByMlsdata)
    def test_search_by_keys(self, config, mls):
        # 1 open mls home page
        search_mls_container = SearchMlsContainer(self.driver)
        main_window = self.driver.current_window_handle
        # 2 click on search box to open the drop down list
        search_common = SearchCommon(self.driver)
        search_common.set_search_box_input(mls)
        search_mls_container.click_activated_suggest()
        SeleniumUtils.switch_to_window(self, main_window)
        mls_details = MlsDetailsPage(self.driver)
        actual = mls_details.get_mls_number()
        print("....... actual mls number: " + actual)

        assert actual == mls


