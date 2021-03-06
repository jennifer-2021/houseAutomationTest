import time

from pages.mls.search_mls_container import SearchMlsContainer
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
    def test_mls_building_type(self, testObject):
        buildingType = testObject["bt"]
        expected = testObject["expected"]

        # 1 open mls home page
        # 2 click each building type
        search_mls_container = SearchMlsContainer(self.driver)
        search_mls_container.select_building_type(buildingType)

        # 3 verify
        actual_selected = search_mls_container.get_selected_filter()
        assert buildingType in actual_selected
        time.sleep(1)
        url = self.driver.current_url
        print(url)
        actual = TestUtils.parse_url_get_dict(url)
        print(actual)

        assert TestUtils.compare_two_dict(expected, actual)
