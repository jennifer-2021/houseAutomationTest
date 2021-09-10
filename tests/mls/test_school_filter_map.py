from utils.read_json_mls import JsonReader
from pages.mls.mls_list_map_section import MlsListMap
import allure
import pytest


@pytest.mark.usefixtures("mls_setup")
class TestMapSchoolFilter:
    testdata = JsonReader.get_school_grade_map()

    @allure.title("二手房 Map filter - 学区筛选")
    @allure.description("地图上 点击学区筛选；验证: 年级")
    @pytest.mark.parametrize("grade", testdata)
    def test_school_filter_on_map(self, grade):
        # 1 open mls home page
        # 2 click each transaction status

        mls_map = MlsListMap(self.driver)
        mls_map.select_school_grade(grade)

        # 3 verify

        elementary_list = mls_map.get_grade_elementary_element_list()
        middle_school_list = mls_map.get_grade_middle_element_list()
        high_school_list = mls_map.get_high_school_element_list()
        if grade == "中小学":
            assert len(elementary_list) > 0 and len(middle_school_list) > 0 and len(high_school_list) == 0
        if grade == "高中":
            assert len(elementary_list) == 0 and len(middle_school_list) == 0 and len(high_school_list) > 0

    testdata = JsonReader.get_school_rank_map()

    @allure.title("二手房 Map filter - 综合评分")
    @allure.description("地图上 点击综合评分；验证: 综合评分 on result list")
    @pytest.mark.parametrize("rankObject", testdata)
    def test_rank_filter_on_map(self, rankObject):
        score = rankObject["label"]
        expected_rank = rankObject["expected"]
        # 1 open mls home page
        # 2 click each transaction status

        mls_map = MlsListMap(self.driver)
        mls_map.select_school_score(score)

        # 3 verify
        actual_rank_list = mls_map.get_score_result_list()
        print(actual_rank_list)
        for rank in actual_rank_list:
            assert float(rank) > expected_rank or float(rank) == expected_rank
