from pages.newHome.search_container import SearchContainer
from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
import allure
import pytest
import time
import re


@pytest.mark.usefixtures("setup")
class TestSearch:
    testdata = JsonReader.get_filter_checkin_time_data()

    @allure.title("Newhome - search - filter - checkin time")
    @allure.description("verify: all returned house info must meet the condition of 'checkinTime'")
    @pytest.mark.parametrize("checkinTime", testdata)
    def test_search_by_building_type(self, config, checkinTime):
        if checkinTime == "不限" | checkinTime == "2020":
            return
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.wait_mapbox_loaded()
        search_container.click_checkin_time_button()
        checkinTime_elements = search_container.get_filter_dropdown_element_list()
        dropdown_list = SeleniumUtils.get_dropdown_text_list(checkinTime_elements)
        if checkinTime not in dropdown_list:
            print("................test data Not in dropdown list: " + checkinTime)
            assert False

        for element in checkinTime_elements:
            name = SeleniumUtils.get_text_by_element(element)
            if name == checkinTime:
                element.click()
                break

        time.sleep(3)
        result_list = search_container.get_search_result_checkin_time_list()
        print(str(len(result_list)) + " ... " + checkinTime)
        print("..............*************.........................")
        if '+' in checkinTime:
            checkinTime = int(checkinTime[0:4])
            for result in result_list:
                actual_checkinTime = SeleniumUtils.get_text_by_element(result)
                if actual_checkinTime != "":
                    actual_checkinTime = re.findall(r'[0-9]+', actual_checkinTime)
                    actual_checkinTime = int(actual_checkinTime[0])
                    if actual_checkinTime < checkinTime:
                        self.print_err_address(result)
                        assert False
        else:
            for result in result_list:
                actual_checkinTime = SeleniumUtils.get_text_by_element(result)
                if checkinTime not in actual_checkinTime:
                    print(".............Printing Error address..........................")
                    print("actual_checkinTime is:" + actual_checkinTime + "should be: " + checkinTime)
                    self.print_err_address(result)
                    assert False

        assert True

    def print_err_address(self, result):
        parent_elem = SeleniumUtils.get_parent_element(self, result)
        error_city_elem = SeleniumUtils.get_next_sibling_element(self, parent_elem)
        error_city = SeleniumUtils.get_text_by_element(error_city_elem)
        print("error city: " + error_city)
