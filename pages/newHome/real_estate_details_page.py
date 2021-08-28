from pages.base_page import BasePage
from utils.selenium_utils import SeleniumUtils
from locators.newHome.locators_real_estate_details import SetDetailsPageLocators


class RealEstateDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_real_estate_name(self):
        element = self.wait_element_visible(*SetDetailsPageLocators.real_estate_name)
        return SeleniumUtils.get_text_by_element(element)

    def click_maphot_button(self):
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