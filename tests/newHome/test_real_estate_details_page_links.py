import time
from pages.newHome.newhome_list_page import NewhomeListPage
from utils.read_json_newhome import JsonReader
from utils.selenium_utils import SeleniumUtils
from pages.newHome.search_container import SearchContainer
from pages.newHome.real_estate_details_page import RealEstateDetailsPage
from pages.agents.contact_agent import ContactAgent
import allure
import pytest


def open_free_info_modal(details_page, agent_page, errors):
    try:
        print(".......免费领取户型图&价格 - try to click the button")
        details_page.click_loan_pre_approve_button()
        title = agent_page.get_loan_pre_approve_modal_title()
        print("....testing - open the modal: 贷款预批申请 title....." + title)
        agent_page.close_loan_pre_approve_modal()
    except:
        print("........test 异常: 贷款预批申请 modal title")
        errors += 1


def open_payment_cycle_modal(details_page, agent_page, errors):
    try:
        details_page.click_payment_cycle_button()
        print(".......付款周期 - clicked the button")
        title = agent_page.get_payment_cycle_modal_title()
        print("....testing - open the modal:: 付款周期 title....." + title)
        agent_page.close_payment_cycle_modal()
    except:
        print("........test 异常: 付款周期 modal title")
        errors += 1


def open_house_tour_modal(details_page, agent_page, errors):
    try:
        details_page.click_house_tour_button()
        print(".......免费报名- clicked the button")
        title = agent_page.get_house_tour_modal_title()
        print("....testing - open the modal:: 免费报名 title....." + title)
        agent_page.close_house_tour_modal()
    except:
        print("........test 异常: 免费报名 modal title")
        errors += 1


def open_discount_policy(details_page, agent_page, errors):
    try:
        details_page.click_discount_policy_button()
        title = agent_page.get_discount_policy_modal_title()
        print("....testing - open the modal: 优惠政策 title....." + title)
        agent_page.close_discount_policy_modal()
    except:
        print("........test 异常: 优惠政策 modal title")
        errors += 1


def open_loan_pre_approve(details_page, agent_page, errors):
    try:
        details_page.click_loan_pre_approve_button()
        title = agent_page.get_loan_pre_approve_modal_title()
        print("....testing - open the modal: 贷款预批申请 title....." + title)
        agent_page.close_loan_pre_approve_modal()
    except:
        print("........test 异常: 贷款预批申请 modal title")
        errors += 1


def open_consult_modal(details_page, agent_page, errors):
    try:
        details_page.click_consult_button()
        print(".......立即咨询- clicked the button")
        title = agent_page.get_consult_modal_title()
        print("....testing - open the modal: 立即咨询 title....." + title)
        agent_page.close_consult_modal()
    except:
        print("........test 异常: 立即咨询 modal title")
        errors += 1


@pytest.mark.usefixtures("setup")
class TestItemTags:

    @allure.title("楼盘列表页 - 点击房源图片进入详情页")
    @allure.description(" 验证：详情页-楼盘名 和 列表页上的楼盘名相符 ")
    def atest_click_link_to_details_page(self, config):
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
            error_counter += 1
            print("...Error....楼盘详情页 - 地图链接 异常")

        self.driver.close()
        # 2 test: 贷款预批申请 modal displayed
        self.driver.switch_to_window(main_window)
        contact_agent = ContactAgent(self.driver)
        open_consult_modal(real_estate_details_page, contact_agent, error_counter)

        # 6 免费领取户型图&价格
        open_free_info_modal(real_estate_details_page, contact_agent, error_counter)

        # 7 付款周期
        print(".......付款周期 - try to click the button")
        open_payment_cycle_modal(real_estate_details_page, contact_agent, error_counter)

        # 8 免费报名
        print(".......免费报名 - try to click the button")
        open_house_tour_modal(real_estate_details_page, contact_agent, error_counter)
        # 9 优惠政策
        print(".......优惠政策 - try to click the button")
        open_discount_policy(real_estate_details_page, contact_agent, error_counter)

        # 10 立即咨询
        print(".......立即咨询 - try to click the button")
        open_consult_modal(real_estate_details_page, contact_agent, error_counter)

        assert error_counter == 0
