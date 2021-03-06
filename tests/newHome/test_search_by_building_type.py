import time
from workflow.newHome.search_check_results import CheckSearchResults
from pages.newHome.newhome_list_page import NewhomeListPage
from pages.search_common import SearchCommon
from utils.read_json_newhome import JsonReader
from pages.newHome.search_container import SearchContainer
from utils.test_utils import TestUtils
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearchByBuildingType:
    testdata = JsonReader.get_filter_building_type_data()

    @allure.title("Newhome - search - filter - building type")
    @allure.description("verify: all returned house building type must contain the value of var 'buildingType'")
    @pytest.mark.parametrize("buildingType", testdata)
    def test_search_by_building_type(self, config, buildingType):
        if buildingType == "不限" or buildingType == "Apartment":
            return
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_common = SearchCommon(self.driver)
        search_common.close_modal()
        search_container.wait_mapbox_loaded()
        search_container.click_building_type_button()
        buildingType_elements = search_container.get_filter_dropdown_element_list()
        dropdown_list = TestUtils.get_text_list(buildingType_elements)
        if buildingType not in dropdown_list:
            print("................test data Not in dropdown list: " + buildingType)
            assert False

        TestUtils.click_filter(buildingType_elements, buildingType)

        time.sleep(3)
        list_page = NewhomeListPage(self.driver)
        result_list = list_page.get_building_type_list()
        print(str(len(result_list)) + " ... " + buildingType)
        print("..............*************.........................")
        check_reuslt = CheckSearchResults(self.driver)
        error_counter = check_reuslt.check_building_type(result_list, buildingType)

        assert error_counter == 0
