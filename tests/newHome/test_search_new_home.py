import time
from pages.newHome.search_container import SearchContainer
from utils.selenium_utils import SeleniumUtils
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearch:
    testdata = ["Toronto", "Vancouver", "Calgary", "Edmonton", "Montreal", "Montreal", "Markham", "Richmond Hill",
                "Vaughan", "Mississauga", "Newmarket", "Oakville"]

    @allure.title("Newhome - search box suggested cities")
    @allure.description("This test is to verify all suggested cities return correct results")
    @pytest.mark.parametrize("searchCity", testdata)
    def test_search_by_suggested_cities(self, config, searchCity):
        time.sleep(1)
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
        # in order to handle: page load twice, static wait used here
        time.sleep(6)
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
