from utils.selenium_utils import SeleniumUtils
from utils.read_json_rental import JsonReader
from pages.rental.home_page import HomePage
import allure
import pytest


@pytest.mark.usefixtures("rental_setup")
class TestSearchCity:
    testdata = JsonReader.get_city_data()

    @allure.title("租房 - 测试每个省，和省内的每个城市的显示数据完整")
    @allure.description("Select a province - 确认： 测试每个选项对应的项目是正确的")
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

    # 由于测试的数据比较大，所以时间较长 - 30分钟？
    @allure.title("租房 - 测试每个省，和省内的每个城市的搜索结果")
    @allure.description("选择一个省 - 每个城市选择一遍。 验证: 搜索结果页 - 所有页面上的房源，地址必须包含 所选择的城市")
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

    catalogdata = JsonReader.get_catalog_data()

    @allure.title("租房 - 区域位置, 测试地铁(TTC)，大学(安省)")
    @allure.description("确认：测试每个目录对应的选项是正确的")
    @pytest.mark.parametrize("catalogs", catalogdata)
    def test_catalog_options(self, catalogs):
        catalog = catalogs["catalog"]
        option = catalogs["option"]
        # 1 open rental home page
        # 2 click 区域位置, and iterate each province and its cities

        home_page = HomePage(self.driver)
        home_page.click_area_position()
        home_page.select_catalog(catalog)
        actual_option = home_page.get_all_provinces()
        print(actual_option)
        assert actual_option == option

    subwaydata = JsonReader.get_subway_data()

    @allure.title("租房 - 测试地铁(TTC) 对应的选项")
    @allure.description("确认： 选项对应的选项是正确的")
    @pytest.mark.parametrize("subwayObject", subwaydata)
    def test_subway_options(self, subwayObject):
        subway_lines = subwayObject["subwayLine"]
        subway_stations = subwayObject["subwayStation"]
        # 1 open rental home page
        # 2 click 区域位置, and iterate each province and its cities

        home_page = HomePage(self.driver)
        home_page.click_area_position()
        home_page.click_subway_catalog()
        home_page.select_province(subway_lines)
        actual_option = home_page.get_all_cities()
        print(actual_option)
        assert actual_option == subway_stations

    universitydata = JsonReader.get_university_data()

    @allure.title("租房 - 大学(安省) 对应的选项")
    @allure.description("确认： 选项对应的选项是正确的")
    @pytest.mark.parametrize("universityObject", universitydata)
    def test_university_options(self, universityObject):
        type = universityObject["type"]
        university = universityObject["option"]
        # 1 open rental home page
        # 2 click 区域位置, and iterate each province and its cities

        home_page = HomePage(self.driver)
        home_page.click_area_position()
        home_page.click_university_catalog()
        home_page.select_province(type)
        actual_option = home_page.get_all_cities()
        print(actual_option)
        assert actual_option == university

    @allure.title("租房 - 地图找房")
    @allure.description("确认： 新窗口打开 - https://house.51.ca/rental/map?注意：两个窗口的title 是一样的， URL不同")
    def test_search_by_map(self):

        # 1 open rental home page
        # 2 click 区域位置, and iterate each province and its cities

        home_page = HomePage(self.driver)
        home_page.click_area_position()
        home_page.click_search_by_map_catalog()
        home_page.dismiss_search_by_map()
        url = self.driver.current_url
        print(url)
        assert "rental?page" in url

        main_window = self.driver.current_window_handle
        home_page.click_area_position()
        home_page.click_search_by_map_catalog()
        home_page.submit_search_by_map()
        SeleniumUtils.switch_to_window(self, main_window)
        url = self.driver.current_url
        print(url)
        assert "rental/map?page" in url
