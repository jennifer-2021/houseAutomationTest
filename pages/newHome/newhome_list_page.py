import time

from pages.base_page import BasePage
from pages.newHome.locators_newhome_map import SetNewhomeMapLocators
from pages.newHome.locators_newhome_list import SetNewhomeListLocators
from utils.selenium_utils import SeleniumUtils


class NewhomeListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # click on 1st element
    def click_house_point_on_map(self, listNumber):
        elements = self.driver.find_elements(*SetNewhomeMapLocators.house_on_map_points)
        self.driver.execute_script("arguments[0].click();", elements[listNumber])

    def click_newhome_modal_check_button(self):
        self.driver.find_element(*SetNewhomeMapLocators.newhome_modal_check_button).click()

    def get_real_estate_name_on_modal(self):
        element = self.driver.find_element(*SetNewhomeMapLocators.real_estate_name_on_modal)
        return SeleniumUtils.get_text_by_element(element)

    def click_sort_by_hot(self):
        self.wait_element(*SetNewhomeListLocators.sort_button).click()
        self.driver.find_element(*SetNewhomeListLocators.sort_by_hot).click()

    def wait_list_reload(self):
        time.sleep(0.5)
        self.wait_element(*SetNewhomeListLocators.sort_button)