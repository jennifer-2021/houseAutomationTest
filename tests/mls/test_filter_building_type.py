from pages.search_common import SearchCommon
from pages.mls.search_mls_container import SearchMlsContainer
from pages.mls.mls_list_page import MlsListPage
from workflow.mls.mls_list_work_flow import MlsListWorkflow
from utils.read_json_mls import JsonReader
from utils.test_utils import TestUtils
import allure
import pytest


@pytest.mark.usefixtures("mls_setup")
class TestBuildingType:
    testdata = JsonReader.get_building_type_data()

    @allure.title("二手房 - 筛选 - 房型")
    @allure.description("选择单个，或是 多个房型，根据返回的页面url,验证: 房型id")
    @pytest.mark.parametrize("testObject", testdata)
    def test_mls_building_type(self, config, testObject):
        buildingType = testObject["bt"]
        expected = testObject["expected"]

        # 1 open mls home page
        # 2 click each building type
        search_mls_container = SearchMlsContainer(self.driver)
        search_mls_container.select_building_type(buildingType)

        # 3 verify
        actual_selected = search_mls_container.get_selected_filter()
        assert buildingType in actual_selected
        url = self.driver.current_url
        actual = TestUtils.parse_url_get_dict(url)
        print(actual)

        assert actual == expected
