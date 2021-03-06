from pages.newHome.search_container import SearchContainer
from pages.newHome.newhome_list_page import NewhomeListPage
from utils.selenium_utils import SeleniumUtils
from utils.test_utils import TestUtils
from utils.read_json_newhome import JsonReader
import allure
import pytest
import time
from workflow.newHome.search_check_results import CheckSearchResults
from pages.search_common import SearchCommon



@pytest.mark.usefixtures("setup")
class TestSearch:
    testdata = JsonReader.get_filter_checkin_time_data()

    @allure.title("Newhome - search - filter - checkin time")
    @allure.description("verify: all returned house info must meet the condition of 'checkinTime'")
    @pytest.mark.parametrize("checkinTime", testdata)
    def test_search_by_building_type(self, config, checkinTime):
        if checkinTime == "不限" or checkinTime == "2020":
            return
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        search_container.wait_mapbox_loaded()
        search_container.click_checkin_time_button()
        checkinTime_elements = search_container.get_filter_dropdown_element_list()
        dropdown_list = TestUtils.get_text_list(checkinTime_elements)
        if checkinTime not in dropdown_list:
            print("................test data Not in dropdown list: " + checkinTime)
            assert False

        TestUtils.click_filter(checkinTime_elements, checkinTime)

        time.sleep(3)
        list_page = NewhomeListPage(self.driver)
        result_list = list_page.get_checkin_time_list()
        print(str(len(result_list)) + " ... " + checkinTime)
        print("..............*************.........................")

        check_result = CheckSearchResults(self.driver)
        error_counter = check_result.checkin_time_on_list(result_list, checkinTime)

        assert error_counter == 0
