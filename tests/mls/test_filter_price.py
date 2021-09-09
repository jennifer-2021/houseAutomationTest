from pages.mls.search_mls_container import SearchMlsContainer
from utils.read_json_mls import JsonReader
from pages.mls.mls_list_page import MlsListPage
import allure
import pytest


@pytest.mark.usefixtures("mls_setup")
class TestBuildingType:
    testdata = JsonReader.get_price_data()

    @allure.title("二手房 - 筛选 - price")
    @allure.description("input a price range. 验证: all returned houses price")
    @pytest.mark.parametrize("testObject", testdata)
    def test_mls_price(self, config, testObject):
        min_price = testObject["from"]
        max_price = testObject["to"]

        # 1 open mls home page
        # 2 set price range
        search_mls_container = SearchMlsContainer(self.driver)
        search_mls_container.set_price_range(min_price, max_price)

        # 3 verify
        error_counter = 0
        list_page = MlsListPage(self.driver)
        price_list = list_page.get_price_list()
        for price in price_list:
            if price < min_price or price > max_price:
                print("......price not in the range, actual===" + str(price))
                error_counter += 1

        assert error_counter == 0
