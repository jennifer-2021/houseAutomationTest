from pages.mls.mls_details_page import MlsDetailsPage
from pages.mls.mls_list_page import MlsListPage
from utils.selenium_utils import SeleniumUtils
from utils.read_json_mls import JsonReader
import allure
import pytest

nearby_deal_url = "ca/map-search/"
commute_calculation_url = "https://www.google.com/maps/dir"
surrounding_map_url = "https://www.google.com/maps"


@pytest.mark.usefixtures("mls_setup")
class TestHouseDetailsPage:

    @allure.title("二手房 details page: 附近成交")
    @allure.description("click 附近成交, should redirect to 附近成交 page. Verify: 附近成交URL")
    def atest_nearby_deal_windows(self):
        self.go_to_details_page()
        # click 附近成交
        details_page = MlsDetailsPage(self.driver)
        details_page.click_nearby_deal_button()
        url = self.driver.current_url
        assert nearby_deal_url in url

    @allure.title("二手房 details page: 通勤计算")
    @allure.description("click 通勤计算, should redirect to google/map")
    def atest_commute_cal_windows(self):
        self.go_to_details_page()
        main_window = self.driver.current_window_handle
        # click 通勤计算
        details_page = MlsDetailsPage(self.driver)
        details_page.click_commute_cal_button()
        SeleniumUtils.switch_to_window(self, main_window)
        url = self.driver.current_url
        assert commute_calculation_url in url

    @allure.title("二手房 details page: 周边地图")
    @allure.description("click 周边地图, should redirect to google/map")
    def atest_surrounding_map(self):
        self.go_to_details_page()
        main_window = self.driver.current_window_handle
        # click 通勤计算
        details_page = MlsDetailsPage(self.driver)
        details_page.click_surrounding_map_button()
        SeleniumUtils.switch_to_window(self, main_window)
        url = self.driver.current_url
        assert surrounding_map_url in url

    testdata = JsonReader.get_modal_link()

    @allure.title("二手房 details page: 11个 modal, 测试每个 modal 可以弹出")
    @allure.description("点击 每个modal, 验证：modal 的 title 显示正确")
    @pytest.mark.parametrize("modal", testdata)
    def atest_modal_windows(self, modal):
        self.go_to_details_page()
        details_page = MlsDetailsPage(self.driver)
        if modal == "贷款计算器":
            details_page.click_morgage_cal()
            actual = details_page.get_calculator_modal_title()
            print(modal + "..." + actual)
            assert actual in modal
            return
        if modal == "计算器":
            details_page.click_calculator()
            actual = details_page.get_calculator_modal_title()
            print(modal + "..." + actual)
            assert modal in actual
            return
        if modal == "预估成交价":
            details_page.click_estimated_price_button()
        if modal == "咨询更多":
            details_page.click_consult_more_button()
            actual = details_page.get_consult_more_modal_content_text()
            print(modal + "..." + actual)
            assert modal in actual
            return
        if modal == "预约看房":
            actual = details_page.is_book_appointment_box_exist()
            print(modal + "..." + str(actual))
            assert actual
            return
        if modal == "查询该房源全部交易历史":
            details_page.click_search_all_deal_history_button()
        if modal == "房屋详情解读":
            details_page.click_interpret_housing_details()
        if modal == "查询房东交易条件":
            details_page.click_check_landlord_trans_condition()
        if modal == "咨询交易费用":
            details_page.click_consult_trans_fee()
        if modal == "解读社区详情":
            details_page.click_interpret_community_details()
        if modal == "咨询学区动态":
            details_page.click_consult_school_district_news()
        actual = details_page.get_modal_title()
        print(modal + "..." + actual)
        assert modal in actual

    def go_to_details_page(self):
        main_window = self.driver.current_window_handle
        list_page = MlsListPage(self.driver)

        # 3 go to details button
        list_page.click_1st_house()
        SeleniumUtils.switch_to_window(self, main_window)
