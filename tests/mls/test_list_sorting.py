
from utils.read_json_mls import JsonReader
from pages.mls.mls_list_page import MlsListPage
import allure
import pytest


@pytest.mark.usefixtures("mls_setup")
class TestListSort:
    parkingdata = JsonReader.get_sorting()

    @allure.title("mls 列表 - 排序")
    @allure.description(" 验证：默认排序 和 更新时间 不应该相同")
    @pytest.mark.parametrize("sort", parkingdata)
    def test_list_sort(self, sort):
        # 1 打开 新房首页
        # 2 select 'sorting'
        list_page = MlsListPage(self.driver)
        # 3 get the list in default sorting
        default_sort_list = list_page.get_price_list()
        # 4 select a sort
        list_page.click_sorting_button()
        list_page.select_a_sort(sort)

        # 3 verify
        new_sort_list = list_page.get_price_list()
        print(new_sort_list)
        if sort == "更新时间":
            assert default_sort_list != new_sort_list

        if sort == "价格从高到低":
            sorted_list = sorted(new_sort_list, reverse=True)
            assert sorted_list == new_sort_list

        if sort == "价格从低到高":
            sorted_list = sorted(new_sort_list)
            assert sorted_list == new_sort_list

