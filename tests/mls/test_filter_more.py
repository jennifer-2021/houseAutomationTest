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
    def test_days_on_market(self, config, days):
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

    @allure.title("二手房 - 筛选 - 上市天数 / 3 天内")
    @allure.description("选择每个上市天数 验证: all returned houses meet selected option")
    @pytest.mark.parametrize("days", testdata)
    def stest_days_market(self, config, days):
        # 1 open mls home page
        # 2 select 'days on market'
        search_mls_container = SearchMlsContainer(self.driver)
        search_mls_container.select_days_on_market(days)

        # 3 verify
        today = TestUtils.get_today()
        yesterday = TestUtils.get_yesterday()
        error_counter = 0
        list_page = MlsListPage(self.driver)
        days_on_market_list = list_page.get_days_on_market_list()
        print(str(days_on_market_list))
        for days in days_on_market_list:
            if days != today and days != yesterday:
                error_counter += 1

        assert error_counter == 0
    testdata = JsonReader.get_area()

    @allure.title("二手房 - 筛选 - 室内面积")
    @allure.description("选择每个室内面积 验证: all returned houses meet selected option")
    @pytest.mark.parametrize("area", testdata)
    def stest_area(self, config, area):

        # 1 open mls home page
        # 2 select 'days on market'
        search_mls_container = SearchMlsContainer(self.driver)
        search_mls_container.select_house_area(area)

        # 3 verify
        error_counter = 0
        list_page = MlsListPage(self.driver)

    @allure.title("二手房 - 筛选 - 上市天数")
    @allure.description("选择每个上市天数 验证: all returned houses meet selected option")
    @pytest.mark.parametrize("days", testdata)
    def stest__market(self, config, days):
        # 1 open mls home page
        # 2 select 'days on market'
        search_mls_container = SearchMlsContainer(self.driver)
        search_mls_container.select_days_on_market(days)
