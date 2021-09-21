
from utils.test_utils import TestUtils
from pages.newHome.newhome_list_page import NewhomeListPage
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestListSort:

    @allure.title("新房列表 - 排序")
    @allure.description(" 验证：默认排序 和 热门排序 不应该相同")
    def atest_tags_on_image(self, config):
        # 1 打开 新房首页
        list_page = NewhomeListPage(self.driver)
        list_page.open_home_page(config)
        # 2 等待 mapbox fully loaded
        list_page.wait_mapbox_loaded()
        # 3 保存默认排序的list - 用楼盘名排序
        sort_default = list_page.get_real_estate_list()
        sort_default_name = TestUtils.get_text_list(sort_default)
        # 4 保存热门排序的list
        list_page = NewhomeListPage(self.driver)
        list_page.click_sort_by_hot()
        list_page.wait_list_reload()
        sort_hot = list_page.get_real_estate_list()
        sort_hot_name = TestUtils.get_text_list(sort_hot)
        print("......默认排序: " + str(sort_default_name))
        print("......热门排序: " + str(sort_hot_name))
        # 5 验证两个排序不同
        if sort_default == sort_hot:
            print("..Error..... 默认排序 和 热门排序 相同")
        assert sort_default != sort_hot
