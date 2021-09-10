
from utils.read_json_mls import JsonReader
from pages.mls.mls_list_map_section import MlsListMap
import allure
import pytest


@pytest.mark.usefixtures("mls_setup")
class TestMapTransaction:
    testdata = JsonReader.get_transaction_on_map()

    @allure.title("二手房 Map - 城市：默认为空白选项；测试：出售,出租,已出售,已出租")
    @allure.description("点击出售,出租,已出售,已出租；验证: 必须对应 上市天数 或 今日成交")
    @pytest.mark.parametrize("transObject", testdata)
    def test_transaction_type(self, config, transObject):
        transaction = transObject["transaction"]
        expected_options = transObject["options"]

        # 1 open mls home page
        # 2 click each transaction status

        mls_map = MlsListMap(self.driver)
        if transaction != "出售":
            mls_map.select_transaction_type(transaction)

        # 3 verify

        days_on_market_list = mls_map.get_days_on_market_option_list(transaction)
        assert days_on_market_list == expected_options
