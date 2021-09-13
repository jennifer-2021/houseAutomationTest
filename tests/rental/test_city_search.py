from pages.mls.search_mls_container import SearchMlsContainer
from utils.read_json_rental import JsonReader
from pages.rental.home_page import HomePage
import allure
import pytest


@pytest.mark.usefixtures("rental_setup")
class TestSearchCity:
    testdata = JsonReader.get_city_data()

    @allure.title("Rental - search city in each province")
    @allure.description("Select a province -  验证: city drop down list should match expected cities in rental.json")
    @pytest.mark.parametrize("cityObject", testdata)
    def test_city_options_in_province(self, cityObject):
        province = cityObject["province"]
        expected_city = cityObject["city"]
        # 1 open rental home page
        # 2 click 区域位置, and iterate each province and its cities

        home_page = HomePage(self.driver)
        home_page.click_area_position()
        home_page.select_province(province)
        actual_cities = home_page.get_all_cities()
        assert expected_city == actual_cities

    provincedata = JsonReader.get_province_data()

    @allure.title("Rental - search city in each province")
    @allure.description("Select a province - iterate and search each city 验证: all returned rental location text")
    @pytest.mark.parametrize("cityObject", testdata)
    def test_search_for_city(self, cityObject):
        province = cityObject["province"]
        city = cityObject["city"]
        if city == "不限":
            return
        # 1 open rental home page
        # 2 click 区域位置, and iterate each province and its cities

        home_page = HomePage(self.driver)
        home_page.click_area_position()
        home_page.select_province(province)
        for one_test_city in city:
            if one_test_city == "不限":
                continue

            home_page.select_city(one_test_city)
            print("......test_city: " + one_test_city)
            # verify: all returned rentals' location match the expected city text
            ads_10_20_address_list = home_page.get_10_20_ads_address()
            print("......ads_10_20_address_list: " + str(ads_10_20_address_list))
            for actual_address in ads_10_20_address_list:
                assert one_test_city in actual_address
            rental_address_list = home_page.get_rental_list_address()
            print(".....rental list..." + str(rental_address_list))
            for actual_address in rental_address_list:
                assert one_test_city in actual_address



