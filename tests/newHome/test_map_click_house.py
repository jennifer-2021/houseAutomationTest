

from utils.selenium_utils import SeleniumUtils
from utils.read_json_newhome import JsonReader
from pages.newHome.newhome_list_page import NewhomeListPage
from pages.newHome.real_estate_details_page import RealEstateDetailsPage
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestMapClickHouse:
    testdata = JsonReader.get_mapPoint_data()

    @allure.title("新房列表 - 房源图片上的 tag")
    @allure.description(" 验证：从地图上可以点击房源，进入详情页")
    @pytest.mark.parametrize("housePoint", testdata)
    def atest_open_details_from_map(self, config, housePoint):
        # 1 打开 新房首页
        list_page = NewhomeListPage(self.driver)
        list_page.open_home_page(config)
        # 2 等待 mapbox fully loaded
        list_page.wait_mapbox_loaded()
        # 3 点击地图上的一个点
        list_page.click_house_point_on_map(housePoint)
        # 4 弹出该房源的 弹窗后，拿到楼盘的名字
        real_estate_name_on_modal = list_page.get_real_estate_name_on_modal()
        main_window = self.driver.current_window_handle
        # 5 点击 '检查' 进入详情页
        list_page.click_newhome_modal_check_button()
        SeleniumUtils.switch_to_window(self, main_window)
        details_page = RealEstateDetailsPage(self.driver)
        # 6 验证详情页打开正确 - 楼盘名显示正确
        actual_name = details_page.get_real_estate_name()
        assert real_estate_name_on_modal == actual_name
