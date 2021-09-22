import json
import time

from pages.newHome.new_home_base_page import NewhomeBasePage
from utils.selenium_utils import SeleniumUtils
from locators.newHome.locators_real_estate_details import SetDetailsPageLocators


class RealEstateDetailsPage(NewhomeBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_real_estate_name(self):
        element = self.wait_element_visible(*SetDetailsPageLocators.real_estate_name)
        return SeleniumUtils.get_text_by_element(element)

    def click_maphot_button(self):
        time.sleep(2)
        self.wait_element(*SetDetailsPageLocators.maphot_button).click()

    def click_loan_pre_approve_button(self):
        self.wait_element(*SetDetailsPageLocators.loan_pre_approve_button).click()

    def click_payment_cycle_button(self):
        self.wait_element(*SetDetailsPageLocators.payment_cycle_subscribe_now).click()

    def click_discount_policy_button(self):
        self.wait_element(*SetDetailsPageLocators.discount_policy_subscribe_now).click()

    def click_consult_button(self):
        self.wait_element(*SetDetailsPageLocators.consult_now).click()

    def click_free_info_button(self):
        # element = self.wait_element(*SetDetailsPageLocators.get_free_real_estate_info)
        # SeleniumUtils.js_executor_click(self, element)
        self.wait_element(*SetDetailsPageLocators.get_free_real_estate_info).click()

    def click_house_tour_button(self):
        self.wait_element(*SetDetailsPageLocators.house_tour_sign_up).click()

    def get_photo_wall_img_elements(self):
        return self.driver.find_elements(*SetDetailsPageLocators.photo_wall)

    def get_navbar_elements(self):
        return self.driver.find_elements(*SetDetailsPageLocators.navbar_list)

    def get_name_position_on_screen(self):
        element = self.driver.find_element(*SetDetailsPageLocators.real_estate_name)
        position = element.location
        return json.dumps(position)

    def get_high_light_position_on_screen(self):
        element = self.driver.find_element(*SetDetailsPageLocators.newhome_high_light)
        position = element.location
        return json.dumps(position)

    def get_promotion_position_on_screen(self):
        element = self.driver.find_element(*SetDetailsPageLocators.promotion_anchor)
        position = element.location
        return json.dumps(position)

    def get_floor_plan_position_on_screen(self):
        element = self.driver.find_element(*SetDetailsPageLocators.floor_plan)
        position = element.location
        return json.dumps(position)

    def get_events_position_on_screen(self):
        element = self.driver.find_element(*SetDetailsPageLocators.related_events)
        position = element.location
        return json.dumps(position)

    def click_navbars(self):
        click_counter = 0
        element_list = self.get_navbar_elements()
        for element in element_list:
            text = SeleniumUtils.get_text_by_element(element)
            element.click()
            click_counter += 1
            if text == "主要信息":
                print(text + "..." + self.get_name_position_on_screen())
            elif text == "项目亮点":
                print(text + "..." + self.get_high_light_position_on_screen())
            elif text == "优惠政策":
                print(text + "..." + self.get_promotion_position_on_screen())
            elif text == "户型&amp;价格":
                print(text + "..." + self.get_floor_plan_position_on_screen())
            elif text == "相关活动":
                print(text + "..." + self.get_events_position_on_screen())
        if click_counter < 3:
            print("....楼盘详情页的navbar是否显示正常")
