import time

from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
from pages.newHome.search_container import SearchContainer
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearchByBuildingType:
    testdata = JsonReader.get_filter_min_price_data()

    @allure.title("Newhome - search - filter - price range")
    @allure.description("verify: all returned house price must meet the filter 'price' ")
    @pytest.mark.parametrize("minPrice", testdata)
    def test_search_by_building_type(self, config, minPrice):
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        # wait for mapbox fully loaded
        search_container.wait_mapbox_loaded()
        # click button to open filter - price / drop down list
        search_container.click_price_button()
        min_price_element_list = search_container.get_min_price_list()
        # get all text from the drop down list
        dropdown_list = SeleniumUtils.get_dropdown_text_list(min_price_element_list)
        if minPrice not in dropdown_list:
            print("................test data Not in dropdown list: " + minPrice)
            assert False

        # click and set min-price
        for element in min_price_element_list:
            name = SeleniumUtils.get_text_by_element(element)
            if name == minPrice:
                element.click()
                break

        # find and set the 1st max-price
        max_price_element_list = search_container.get_max_price_list()
        # get max-price text and Integer format
        max_price_text = SeleniumUtils.get_text_by_element(max_price_element_list[1])
        max_price_int = SeleniumUtils.get_start_price(max_price_text)
        # get minPrice in Integer format: i.e $1,000,000 to 1000000
        minPrice = SeleniumUtils.get_start_price(minPrice)

        # click 2nd to-price on drop down list
        max_price_element_list[1].click()

        # wait for search result list page to fully loaded
        time.sleep(3)
        # on search result page - get all house price elements as a list
        result_element_list = search_container.get_search_result_price_list()
        # check each actual price - compare with test data - minPrice
        for element in result_element_list:
            text = SeleniumUtils.get_text_by_element(element)
            actual_start_price = SeleniumUtils.get_start_price(text)
            if '-' in text:
                actual_to_price = SeleniumUtils.get_to_price(text)
                if actual_start_price > max_price_int:
                    self.print_err_address(element, text)
                    assert False
                if actual_to_price < minPrice:
                    self.print_err_address(element, text)
                    assert False
            else:
                if actual_start_price < minPrice:
                    self.print_err_address(element, text)
                    assert False
                if actual_start_price > max_price_int:
                    self.print_err_address(element, text)
                    assert False

        assert True

    def print_err_address(self, anchor_element, text):
        print("......error：...actual price: " + text)
        error_city_elem = SeleniumUtils.get_previous_sibling_element(self, anchor_element)
        error_city = SeleniumUtils.get_text_by_element(error_city_elem)
        print("error city: " + error_city)
