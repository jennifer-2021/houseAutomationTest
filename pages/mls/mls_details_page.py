from utils.selenium_utils import SeleniumUtils
from pages.mls.mls_base_page import MlsBasePage
from locators.mls.locators_mls_details import SetMlsDetailsLocators
from time import sleep
from utils.test_utils import TestUtils


class MlsDetailsPage(MlsBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 详情页上的 MLS number
    def get_mls_number(self):
        element = self.wait_element(*SetMlsDetailsLocators.mls_name)
        return element.get_attribute('value')

    # click 附近成交 nav bar
    def click_nearby_deal_button(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.nearby_deal_button).click()
        sleep(0.5)

    # click 通勤计算 nav bar
    def click_commute_cal_button(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.commute_cal_button).click()
        sleep(0.5)

    # # 周边地图
    def click_surrounding_map_button(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.surrounding_map_button).click()
        sleep(0.5)

    # calculator
    def click_calculator(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.calculator_button).click()

    # 预估成交价 - have modal
    def click_estimated_price_button(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.estimated_trans_price).click()

    def get_estimated_price_modal_title(self):
        element = self.wait_element(*SetMlsDetailsLocators.estimated_trans_price_modal_title)
        return SeleniumUtils.get_text_by_element(element)

    # 咨询更多 - have modal
    def click_consult_more_button(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.consult_more).click()

    def get_consult_more_modal_content_text(self):
        element = self.wait_element(*SetMlsDetailsLocators.consult_more_modal_content)
        return SeleniumUtils.get_text_by_element(element)

    # 预约看房 not text  - Only check if the Form exist
    def is_book_appointment_box_exist(self):
        try:
            self.wait_element(*SetMlsDetailsLocators.book_appointment)
            return True
        except:
            return False

    # 查询该房源全部交易历史  - have modal
    def click_search_all_deal_history_button(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.search_all_deal_history).click()

    # 房屋详情解读 - have modal
    def click_interpret_housing_details(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.interpret_housing_details).click()

    # 查询房东交易条件 - have modal
    def click_check_landlord_trans_condition(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.check_landlord_trans_condition).click()

    # 咨询交易费用 - have modal
    def click_consult_trans_fee(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.consult_trans_fee).click()

    # 贷款计算器 - have modal
    def click_morgage_cal(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.morgage_cal).click()

    # calculator (in content) - have modal
    def click_in_form_calculator(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.calculator).click()

    # 咨询学区动态 - have modal
    def click_consult_school_district_news(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.consult_school_district_news).click()

    # 解读社区详情 - have modal
    def click_interpret_community_details(self):
        sleep(2)
        self.wait_element(*SetMlsDetailsLocators.interpret_community_details).click()

    # this modal_title css shared by all modals
    def get_modal_title(self):
        element = self.wait_element(*SetMlsDetailsLocators.modal_title)
        return SeleniumUtils.get_text_by_element(element)

    # get calculator modal text
    def get_calculator_modal_title(self):
        element = self.wait_element(*SetMlsDetailsLocators.modal_calculator_title)
        return SeleniumUtils.get_text_by_element(element)


