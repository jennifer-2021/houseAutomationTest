import time
from pages.search_container import SearchContainer
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestSearch:

    @allure.title("Login with valid data test")
    @allure.description("This is test of login with valid data")
    def test_search_without_autocomplete(self, config):
        searchKey = "toronto"
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        search_container.set_user_input(searchKey)
        time.sleep(3)
        filter_result = search_container.get_filter_box()
        assert searchKey in filter_result.lower()
