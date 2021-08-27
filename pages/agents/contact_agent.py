from pages.base_page import BasePage
from locators.agents.locators_contact_agent import SetContactAgentLocators
from utils.selenium_utils import SeleniumUtils


class ContactAgent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_loan_pre_approve_modal_title(self):
        element = self.wait_element(*SetContactAgentLocators.loan_pre_approve_modal_title)
        return SeleniumUtils.get_text_by_element(element)

    def close_loan_pre_approve_modal(self):
        self.driver.find_element(*SetContactAgentLocators.loan_pre_approve_modal_close).click()

    def get_free_info_modal_title(self):
        element = self.wait_element(*SetContactAgentLocators.free_info_modal_title)
        return SeleniumUtils.get_text_by_element(element)

    def close_free_info_modal(self):
        element = self.wait_element(*SetContactAgentLocators.free_info_modal_title)
        SeleniumUtils.get_next_sibling_element(self, element).click()

    def get_payment_cycle_modal_title(self):
        element = self.wait_element(*SetContactAgentLocators.payment_cycle_modal_title)
        return SeleniumUtils.get_text_by_element(element)

    def close_payment_cycle_modal(self):
        element = self.wait_element(*SetContactAgentLocators.payment_cycle_modal_title)
        SeleniumUtils.get_next_sibling_element(self, element).click()

    def get_discount_policy_modal_title(self):
        element = self.wait_element(*SetContactAgentLocators.discount_policy_modal_title)
        return SeleniumUtils.get_text_by_element(element)

    def close_discount_policy_modal(self):
        element = self.wait_element(*SetContactAgentLocators.discount_policy_modal_title)
        SeleniumUtils.get_next_sibling_element(self, element).click()

    def get_house_tour_modal_title(self):
        element = self.wait_element(*SetContactAgentLocators.house_tour_modal_title)
        return SeleniumUtils.get_text_by_element(element)

    def close_house_tour_modal(self):
        element = self.wait_element(*SetContactAgentLocators.house_tour_modal_title)
        SeleniumUtils.get_next_sibling_element(self, element).click()

    def get_consult_modal_title(self):
        element = self.wait_element(*SetContactAgentLocators.consult_now_modal_title)
        return SeleniumUtils.get_text_by_element(element)

    def close_consult_modal(self):
        element = self.wait_element(*SetContactAgentLocators.consult_now_modal_title)
        SeleniumUtils.get_next_sibling_element(self, element).click()