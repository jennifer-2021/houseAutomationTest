from pages.mls.search_mls_container import SearchMlsContainer
from utils.read_json_mls import JsonReader
from pages.mls.mls_list_page import MlsListPage
from utils.test_utils import TestUtils
import allure
import pytest


@pytest.mark.usefixtures("mls_setup")
class TestFilterMore:
    testdata = JsonReader.get_days_on_market_data()

    @allure.title("二手房 - 筛选 - 上市天数")
    @allure.description("选择每个上市天数 验证: all returned houses meet selected option")
    @pytest.mark.parametrize("days", testdata)
    def test_days_on_market(self, days):
        # 1 open mls home page
        # 2 select 'days on market'
        search_mls_container = SearchMlsContainer(self.driver)
        search_mls_container.select_days_on_market(days)

        test_day = SearchMlsContainer.convert_days_to_int(days)

        # 3 verify
        today = TestUtils.get_today()
        error_counter = 0
        list_page = MlsListPage(self.driver)
        # get actual: list [datetime]
        days_on_market_list = list_page.get_days_on_market_list()
        for actual_day in days_on_market_list:
            diff = today - actual_day
            diff_days = TestUtils.get_datetime_diff(diff)
            if diff_days > test_day:
                error_counter += 1

        assert error_counter == 0

    parkingdata = JsonReader.get_parking_lot()

    @allure.title("二手房 - 筛选 - 车位")
    @allure.description("选择每个车位 验证: all returned houses meet selected option")
    @pytest.mark.parametrize("parking", parkingdata)
    def test_parking_lots(self, parking):
        # 1 open mls home page
        # 2 select 'days on market'
        search_mls_container = SearchMlsContainer(self.driver)
        search_mls_container.select_parking_lot(parking)

        # 3 verify
        error_counter = 0
        list_page = MlsListPage(self.driver)
        parking_list = list_page.get_parking_space_list()

        for actual_parking in parking_list:
            if actual_parking not in parking:
                error_counter += 1
        assert error_counter == 0

