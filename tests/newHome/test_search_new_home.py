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
        all_result_in_city = True
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.click_in_search_box()
        search_container.keep_search_suggest_menu_open()
        cities = search_container.get_suggest_cities_elements()

        for city in cities:
            name = SeleniumUtils.get_text_by_element(city)
            if name == searchCity:
                city.click()
                break

        search_container.wait_mapbox_loaded()
        result_list = search_container.get_search_result_address_list()
        print(str(len(result_list)) + " ... " + searchCity)
        print("..............*************.........................")
        for result in result_list:
            addr = SeleniumUtils.get_text_by_element(result)
            if searchCity not in addr:
                print(addr + "search for city: " + searchCity)
                print(".............Error address..........................")
                all_result_in_city = False
                break

        assert all_result_in_city
