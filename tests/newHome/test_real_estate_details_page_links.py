import time
from pages.newHome.newhome_list_page import NewhomeListPage
from utils.read_json import JsonReader
from utils.selenium_utils import SeleniumUtils
from pages.newHome.search_container import SearchContainer
from pages.newHome.real_estate_details_page import RealEstateDetailsPage
from pages.agents.contact_agent import ContactAgent
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestItemTags:

    @allure.title("楼盘列表页 - 点击房源图片进入详情页")
    @allure.description(" 验证：详情页-楼盘名 和 列表页上的楼盘名相符 ")
    def test_click_link_to_details_page(self, config):

        # 1 打开 新房首页
        search_container = SearchContainer(self.driver)
        search_container.open_home_page(config)
        # 2 等待 mapbox fully loaded
        search_container.wait_mapbox_loaded()
        windows = [self.driver.current_window_handle]
        # 3 从页面点击一个房源，进入详情页
        list_page = NewhomeListPage(self.driver)
        real_estate_element_list = list_page.get_real_estate_list()
        real_estate_name_on_list = SeleniumUtils.get_text_by_element(real_estate_element_list[1])
        real_estate_element_list[1].click()
        SeleniumUtils.switch_to_window(self, windows)
        real_estate_details = RealEstateDetailsPage(self.driver)
        real_estate_name_on_details = real_estate_details.get_real_estate_name()
        print(".......name on list: " + real_estate_name_on_list)
        print(".......name on details page: " + real_estate_name_on_details)
        assert real_estate_name_on_list == real_estate_name_on_details

    testdata = JsonReader.get_details_page_buttons_data()

    @allure.title("楼盘详情页 - 页面上的链接")
    @allure.description(" 验证：所有的链接都能打开正确的窗口 ")
    @pytest.mark.parametrize("real_estate_url", testdata)
    def test_buttons_on_details_page(self, config, real_estate_url):

        # 1 打开 新房-楼盘详情页
        real_estate_details_page = RealEstateDetailsPage(self.driver)
        real_estate_details_page.open_page(config, real_estate_url)
        main_window = self.driver.current_window_handle
        real_estate_details_page.click_maphot_button()
        SeleniumUtils.switch_to_window(self, main_window)
        error_counter = 0
        time.sleep(2)
        current_url = self.driver.current_url
        print(current_url)
        print("....testing - open the map: " + current_url)
        if "google.com/maps" not in current_url:
            print("...Error....楼盘详情页 - 地图链接 异常")
            error_counter += 1
        self.driver.close()
        # 2 test: 贷款预批申请 modal displayed
        self.driver.switch_to_window(main_window)
        contact_agent = ContactAgent(self.driver)
        try:
            real_estate_details_page.click_loan_pre_approve_button()
            title = contact_agent.get_loan_pre_approve_modal_title()
            print("....testing - open the modal: 贷款预批申请 title....." + title)
            contact_agent.close_loan_pre_approve_modal()
        except:
            print("........test 异常: 贷款预批申请 modal title")
            error_counter += 1
        # 6 免费领取户型图&价格
        try:
            real_estate_details_page.click_free_info_button()
            title = contact_agent.get_free_info_modal_title()
            print("....testing - open the modal:: 免费领取户型图&价格 title....." + title)
            contact_agent.close_free_info_modal()
        except:
            print("........test 异常: 免费领取户型图&价格 modal title")
            error_counter += 1
        # 7 付款周期
        try:
            real_estate_details_page.click_payment_cycle_button()
            title = contact_agent.get_payment_cycle_modal_title()
            print("....testing - open the modal:: 付款周期 title....." + title)
            contact_agent.close_payment_cycle_modal()
        except:
            print("........test 异常: 付款周期 modal title")
            error_counter += 1
        # 8 免费报名
        try:
            real_estate_details_page.click_house_tour_button()
            title = contact_agent.get_house_tour_modal_title()
            print("....testing - open the modal:: 免费报名 title....." + title)
            contact_agent.close_house_tour_modal()
        except:
            print("........test 异常: 免费报名 modal title")
            error_counter += 1
        # 9 优惠政策
        try:
            real_estate_details_page.click_discount_policy_button()
            title = contact_agent.get_discount_policy_modal_title()
            print("....testing - open the modal: 优惠政策 title....." + title)
            contact_agent.close_discount_policy_modal()
        except:
            print("........test 异常: 优惠政策 modal title")
            error_counter += 1
        # 10 立即咨询
        try:
            real_estate_details_page.click_consult_button()
            title = contact_agent.get_consult_modal_title()
            print("....testing - open the modal: 立即咨询 title....." + title)
            contact_agent.close_consult_modal()
        except:
            print("........test 异常: 立即咨询 modal title")
            error_counter += 1

        assert error_counter == 0
