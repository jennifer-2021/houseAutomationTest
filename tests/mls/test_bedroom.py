

from pages.mls.search_mls_container import SearchMlsContainer
from utils.read_json_mls import JsonReader
from pages.mls.mls_list_page import MlsListPage
import allure
import pytest


@pytest.mark.usefixtures("mls_setup")
class TestBedroom:
    testdata = JsonReader.get_bedroom_data()

    @allure.title("二手房 - 筛选 - bedroom")
    @allure.description("input a price range. 验证: all returned houses price")
    @pytest.mark.parametrize("bedroom", testdata)
    def atest_mls_bedroom(self, bedroom):

        # 1 open mls home page
        # 2 set price range
        search_mls_container = SearchMlsContainer(self.driver)
        search_mls_container.select_bedroom(bedroom)

        # 3 verify
        expected_bedroom = int(bedroom)

        error_counter = 0
        list_page = MlsListPage(self.driver)
        bedroom_list = list_page.get_bedroom_list()
        i = 0
        for actual_bedroom in bedroom_list:
            i += 1
            if actual_bedroom < expected_bedroom:
                print("......bedroom is incorrect, actual===" + str(actual_bedroom))
                print("......error on list position: " + str(i))
                error_counter += 1

        assert error_counter == 0
