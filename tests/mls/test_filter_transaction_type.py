from pages.search_common import SearchCommon
from pages.mls.search_mls_container import SearchMlsContainer
from pages.mls.mls_list_page import MlsListPage
from workflow.mls.mls_list_work_flow import MlsListWorkflow
from utils.read_json_mls import JsonReader
from utils.test_utils import TestUtils
import allure
import pytest


@pytest.mark.usefixtures("mls_setup")
class TestFilter:
    testdata = JsonReader.get_mls_suggested_cities_data()

    @allure.title("二手房 - 搜索框热门城市")
    @allure.description("验证: 点击每个热门城市，根据返回的页面url,确认城市名称，location_id")
    @pytest.mark.parametrize("cityObject", testdata)
    def test_suggested_cities(self, config, cityObject):
        # 1 open mls home page
        city = cityObject["city"]
        expected = cityObject["url"]
        search_mls_container = SearchMlsContainer(self.driver)
        # 2 click on search box to open the drop down list
        search_common = SearchCommon(self.driver)
        search_common.click_in_search_box()
        # 3 get and click the actual cities in search drop down list
        suggest_city_element_list = search_mls_container.get_suggest_cities_elements()
        TestUtils.click_filter(self, suggest_city_element_list, city)
        # 4 verify url
        search_mls_container.wait_mapbox_loaded()
        url = self.driver.current_url
        actual_result = TestUtils.parse_url_get_dict(url)
        print(actual_result)
        print(expected)
        assert expected == actual_result

    transactiondata = JsonReader.get_transaction_status_data()

    @allure.title("二手房 - 城市：默认为空白选项；测试：出售,出租 ")
    @allure.description("验证: 点击出售,出租，返回的所有房源的租售状态 必须符合筛选条件")
    @pytest.mark.parametrize("transaction", transactiondata)
    def atest_transaction_type(self, config, transaction):
        # 1 open mls home page
        search_mls_container = SearchMlsContainer(self.driver)
        # 2 click each transaction status

        if transaction != "出售":
            search_mls_container.select_transaction_type(transaction)

        # 3 verify
        mls_list_page = MlsListPage(self.driver)
        transaction_element_list = mls_list_page.get_transaction_element_list()
        is_all_transaction_in_place = MlsListWorkflow.verify_transaction_status(transaction_element_list, transaction)
        assert is_all_transaction_in_place == 0

    transactiondata2 = JsonReader.get_transaction2_status_data()

    @allure.title("二手房 - 城市：默认为空白选项；测试：已出售, 已出租 ")
    @allure.description("点击已出售, 已出租，验证: 返回的所有房源的 1 内容标签 2 图片上的标签")
    @pytest.mark.parametrize("transaction", transactiondata2)
    def atest_transaction_type_2(self, config, transaction):
        # 1 open mls home page
        search_mls_container = SearchMlsContainer(self.driver)

        # 2 click each transaction status
        search_mls_container.select_transaction_type(transaction)

        # 3 verify
        mls_list_page = MlsListPage(self.driver)
        transaction_element_list = mls_list_page.get_transaction_element_list()
        error_counter = MlsListWorkflow.verify_transaction_status(transaction_element_list, transaction)

        if transaction == '已出售':
            transaction_icon_element_list = mls_list_page.get_transaction_sold_element_list()
        else:
            transaction_icon_element_list = mls_list_page.get_transaction_leased_element_list()

        if len(transaction_element_list) != len(transaction_icon_element_list):
            error_counter += 1

        assert error_counter == 0
