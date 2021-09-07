from utils.selenium_utils import SeleniumUtils
from pages.mls.mls_base_page import MlsBasePage
from locators.mls.locators_mls_list import SetMlsListLocators
from locators.mls.locators_mls_map import SetMlsMapLocators
from utils.test_utils import TestUtils


class MlsListPage(MlsBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # list - get address element list
    def get_address_element_list(self):
        return self.driver.find_elements(*SetMlsListLocators.search_result_address_list)

    # 地图 - 点击地图上的点
    def click_house_single_point_on_map(self, listNumber):
        elements = self.driver.find_elements(*SetMlsMapLocators.house_on_map_points_single)
        self.driver.execute_script("arguments[0].click();", elements[listNumber])

    # get 列表上 所有房源 的 交易类型描述 - list[element]
    def get_transaction_element_list(self):
        return self.driver.find_elements(*SetMlsListLocators.list_transaction_type)

    # get 列表上 所有房源 图片上的 已售出 标签 - list[element]
    def get_transaction_sold_element_list(self):
        return self.driver.find_elements(*SetMlsListLocators.list_sold_transaction_type)

    # get 列表上 所有房源 图片上的 已租出 标签 - list[element]
    def get_transaction_leased_element_list(self):
        return self.driver.find_elements(*SetMlsListLocators.list_leased_transaction_type)

