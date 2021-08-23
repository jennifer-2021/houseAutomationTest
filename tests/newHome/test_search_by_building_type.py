import time

from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
from pages.newHome.search_container import SearchContainer
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
        search_container.wait_mapbox_loaded()
        search_container.click_building_type_button()
        buildingType_elements = search_container.get_filter_dropdown_element_list()
        dropdown_list = SeleniumUtils.get_dropdown_text_list(buildingType_elements)
        if buildingType not in dropdown_list:
            print("................test data Not in dropdown list: " + buildingType)
            assert False

        for element in buildingType_elements:
            name = SeleniumUtils.get_text_by_element(element)
            if name == buildingType:
                element.click()
                break

        time.sleep(3)
        result_list = search_container.get_search_result_building_type_list()
        print(str(len(result_list)) + " ... " + buildingType)
        print("..............*************.........................")
        for result in result_list:
            building_info = SeleniumUtils.get_text_by_element(result)
            if buildingType not in building_info:
                print(".............Printing Error address..........................")
                parent_elem = SeleniumUtils.get_parent_element(self, result)
                error_city_elem = SeleniumUtils.get_next_sibling_element(self, parent_elem)
                error_city = SeleniumUtils.get_text_by_element(error_city_elem)
                print(building_info + "search for city: " + error_city)

                assert False

        assert True
