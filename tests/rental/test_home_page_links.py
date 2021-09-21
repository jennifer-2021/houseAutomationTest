from utils.selenium_utils import SeleniumUtils
from utils.read_json_rental import JsonReader
from pages.rental.home_page import HomePage
import allure
import pytest


@pytest.mark.usefixtures("rental_setup")
class TestHomePageLinks:
    testdata = JsonReader.get_publish_links_data()

    @allure.title("租房 - 免费发布")
    @allure.description("Select a province - 确认： 新窗口的URL正确")
    @pytest.mark.parametrize("linkObject", testdata)
    def atest_publish_links(self, linkObject):
        link = linkObject["link"]
        url = linkObject["url"]
        # 1 open rental home page

        home_page = HomePage(self.driver)
        main_window = self.driver.current_window_handle
        if link == "地图找房":
            home_page.click_search_by_map()
        if link == "租房管理-top":
            home_page.click_rental_management_primary()
        if link == "租房管理-middle":
            home_page.click_rental_management_secondary()
        if link == "免费发布-top":
            home_page.click_publish_rental_primary()
        if link == "免费发布-middle":
            home_page.click_publish_rental_secondary()
        SeleniumUtils.switch_to_window(self, main_window)
        actual_url = self.driver.current_url
        assert url in actual_url




