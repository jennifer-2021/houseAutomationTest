import allure
import pytest
from utils.read_json_house_home import JsonReader
from pages.HouseHomePage.home_select_city import HouseHomePage

search_key = "Markham"


@pytest.mark.usefixtures("home_page_setup")
class TestSearchBox:
    searchdata = JsonReader.get_catalog_data()

    @allure.title("房屋首页 - 测试hot navigation链接跳转正确")
    @allure.description(" 点击hot navigation，验证： 链接跳转正确")
    # @pytest.mark.parametrize("catalog", searchdata)
    def test_search_box(self):
        # 1 close the modal window
        house_home_page = HouseHomePage(self.driver)
        house_home_page.set_search_input(search_key)
        url = self.driver.current_url
        print(url)
