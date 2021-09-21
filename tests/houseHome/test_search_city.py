from utils.selenium_utils import SeleniumUtils
from utils.read_json_house_home import JsonReader
from pages.HouseHomePage.home_select_city import HouseHomePage
import allure
import pytest


@pytest.mark.usefixtures("home_page_setup")
class TestSearchCity:
    provincedata = JsonReader.get_home_province_data()

    @allure.title("房屋首页 - 测试每个省，确认下拉菜单显示数据完整")
    @allure.description(" 打开选择城市的下拉菜单，验证： 下拉菜单显示数据是正确的")
    @pytest.mark.parametrize("province", provincedata)
    def done_test_province(self, province):
        # 1 get test data
        expected_province_list = province["provinces"]

        # 2 get actual province_list
        home_page = HouseHomePage(self.driver)
        actual_province_list = home_page.get_province_en_list()
        print(actual_province_list)
        assert actual_province_list == expected_province_list

    citydata = JsonReader.get_home_city_data()

    @allure.title("房屋首页 - 测试每个省，和省内的每个城市的显示数据完整")
    @allure.description("选择每个省 - 验证： 测试每个省对应的城市是正确的")
    @pytest.mark.parametrize("cityObject", citydata)
    def done_test_cities_in_province(self, cityObject):
        # 1 get test data
        province_to_test = cityObject["province"]
        expected_city_list = cityObject["city"]

        # 2 get actual province_list
        home_page = HouseHomePage(self.driver)
        home_page.click_select_city_button()
        home_page.select_province(province_to_test)

        actual_city_list = home_page.get_city_en_list()
        print(actual_city_list)
        assert actual_city_list == expected_city_list

