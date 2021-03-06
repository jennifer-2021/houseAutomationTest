from pages.mls.mls_list_map_section import MlsListMap
from utils.selenium_utils import SeleniumUtils
import allure
import pytest
from pages.search_common import SearchCommon
from pages.mls.search_mls_container import SearchMlsContainer
from utils.test_utils import TestUtils

expected_mls_details_page_title = "房产"
city = "Richmond Hill"


@pytest.mark.usefixtures("mls_setup")
class TestMapSchoolFilter:

    @allure.title("二手房 Map - house single point")
    @allure.description("地图上 点击 any point, open details page, verify page is opened by asserting the page title")
    def test_house_single_point_on_map(self):
        # 1 open mls home page
        # 2 click each transaction status
        main_window = self.driver.current_window_handle
        mls_map = MlsListMap(self.driver)
        mls_map.click_house_on_map()
        mls_map.click_modal_go_to_details()
        SeleniumUtils.switch_to_window(self, main_window)

        # 3 verify
        title = self.driver.title
        assert expected_mls_details_page_title in title

    @allure.title("二手房 Map - house multi point")
    @allure.description("地图上 点击 any multi point, open 1st details page, verify: page is opened")
    def atest_house_multi_points_on_map(self):
        # 1 open mls home page
        # 2 click each transaction status
        main_window = self.driver.current_window_handle
        search_box = SearchCommon(self.driver)
        search_box.click_in_search_box()
        # 3 get and click the actual cities in search drop down list
        search_mls_container = SearchMlsContainer(self.driver)
        suggest_city_element_list = search_mls_container.get_suggest_cities_elements()
        TestUtils.click_filter(suggest_city_element_list, city)

        mls_map = MlsListMap(self.driver)
        try:
            mls_map.click_multi_house_on_map()
            mls_map.click_1st_house_on_modal()
            SeleniumUtils.switch_to_window(self, main_window)
        except:
            print(" ... warning: 地图上没有聚合点(一个点有至少2个房源)")
        # 3 verify
        title = self.driver.title
        assert expected_mls_details_page_title in title
