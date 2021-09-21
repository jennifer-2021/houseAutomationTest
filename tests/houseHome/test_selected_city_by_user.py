from utils.read_json_house_home import JsonReader
from pages.HouseHomePage.home_select_city import HouseHomePage
import allure
import pytest


@pytest.mark.usefixtures("home_page_setup")
class TestSelectedCity:
    catalogdata = JsonReader.get_catalog_data()

    @allure.title("房屋首页 - 测试每个省，确认下拉菜单显示数据完整")
    @allure.description(" 打开选择城市的下拉菜单，验证： 下拉菜单显示数据是正确的")
    @pytest.mark.parametrize("catalogObject", catalogdata)
    def atest_selected_cities(self, catalogObject):
        province = catalogObject["province"]
        city = catalogObject["city"]

        # 1 select a city
        home_page = HouseHomePage(self.driver)
        home_page.click_select_city_button()
        home_page.select_province(province)
        home_page.select_city(city)
