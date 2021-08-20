import time

from utils.selenium_utils import SeleniumUtils
from pages.newHome.search_container import SearchContainer
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearchByBuildingType:
    testdata = ["Condo", "Townhouse", "House"]

    @allure.title("Newhome - search - filter - building type")
    @allure.description("This test is to verify all building types return correct results")
    @pytest.mark.parametrize("buildingType", testdata)
    def test_search_by_building_type(self, config, buildingType):
        all_results_in_buildingType = True
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.click_building_type_button()
        buildingType_elements = search_container.get_building_type_element_list()
        for element in buildingType_elements:
            name = SeleniumUtils.get_text_by_element(element)
            if name == buildingType:
                element.click()
                break

        time.sleep(6)
        result_list = search_container.get_search_result_building_type_list()
        print(str(len(result_list)) + " ... " + buildingType)
        print("..............*************.........................")
        for result in result_list:
            building_info = SeleniumUtils.get_text_by_element(result)
            if buildingType not in building_info:
                parent_elem = SeleniumUtils.get_parent_element(self, result)
                error_city_elem = SeleniumUtils.get_next_sibling_element(self, parent_elem)
                error_city = SeleniumUtils.get_text_by_element(error_city_elem)
                print(building_info + "search for city: " + error_city)
                print(".............Error address..........................")
                all_results_in_buildingType = False
                break

        assert all_results_in_buildingType
