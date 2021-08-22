import time

from pages.newHome.search_container import SearchContainer
from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearch:
    testdata = JsonReader.get_search_suggested_cities_data()

    @allure.title("Newhome - search box suggested cities")
    @allure.description("verify: all returned house address must contain the value of var 'searchCity'")
    @pytest.mark.parametrize("searchCity", testdata)
    def test_search_by_suggested_cities(self, config, searchCity):
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.click_in_search_box()
        search_container.keep_search_suggest_menu_open()
        city_elements = search_container.get_suggest_cities_elements()
        dropdown_list = SeleniumUtils.get_dropdown_text_list(city_elements)
        if searchCity not in dropdown_list:
            print("................test data Not in dropdown list: " + searchCity)
            assert False

        for city in city_elements:
            name = SeleniumUtils.get_text_by_element(city)
            if name == searchCity:
                city.click()
                break

        search_container.wait_mapbox_loaded()
        time.sleep(1)
        if name == 'Vaughan':
            time.sleep(5)
        result_list = search_container.get_search_result_address_list()
        list_length = len(result_list)

        # result_list = search_container.get_search_result_address_list()
        print(str(list_length) + " ... " + searchCity)
        print("..............*************.........................")
        for result in result_list:
            addr = SeleniumUtils.get_text_by_element(result)
            if searchCity not in addr:
                print(addr + "search for city: " + searchCity)
                print(".............Error address..........................")
                assert False

        assert True
