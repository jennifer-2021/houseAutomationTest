from selenium.webdriver.common.keys import Keys

from locators.mls.locators_mls_search_container import SetMlsSearchLocators
from pages.mls.mls_base_page import MlsBasePage
from utils.selenium_utils import SeleniumUtils
from utils.test_utils import TestUtils
from time import sleep


class SearchMlsContainer(MlsBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 搜索框内 - 返回全部热门城市: list[element]
    def get_suggest_cities_elements(self):
        return self.driver.find_elements(*SetMlsSearchLocators.search_box_suggested_city_list)

    # 搜索框内 - 返回全部热门城市: list[text]
    def get_suggest_cities(self):
        name_list = []
        element_list = self.get_suggest_cities_elements()
        for element in element_list:
            name_list.append(SeleniumUtils.get_text_by_element(element))
        return name_list

    # 筛选 - 点击 出售
    def click_sale_button(self):
        self.wait_element(*SetMlsSearchLocators.filter_sale).click()

    # 筛选 - 点击 房型
    def click_building_type_button(self):
        self.wait_element(*SetMlsSearchLocators.filter_building_type).click()

    #
    def click_building_type_confirm_button(self):
        self.wait_element(*SetMlsSearchLocators.filter_building_type_confirm_selection).click()

    # 筛选 - 点击 价格
    def click_price_button(self):
        self.wait_element(*SetMlsSearchLocators.filter_price).click()

    # 筛选 - 点击 卧室
    def click_bedroom_button(self):
        self.wait_element(*SetMlsSearchLocators.filter_bedroom).click()

    # 筛选 - 点击 更多
    def click_more_button(self):
        element = self.wait_element(*SetMlsSearchLocators.filter_more)
        SeleniumUtils.js_executor_click(self, element)

    # 筛选 - '出售'下拉框 - 返回：list[element]
    def get_sale_element_list(self):
        return self.driver.find_elements(*SetMlsSearchLocators.filter_sale_list)

    # 筛选 - '房型'下拉框 - 返回：list[element]
    def get_building_type_element_list(self):
        return self.driver.find_elements(*SetMlsSearchLocators.filter_building_type_list)

    # 筛选 - '价格'下拉框 - 设定最小，最大价格
    def set_price_min(self, min_price):
        elem = self.wait_element(*SetMlsSearchLocators.filter_price_min)
        elem.click()
        # elem.send_keys(Keys.NUMPAD8)
        elem.send_keys(min_price)

    def set_price_max(self, max_price):
        elem = self.wait_element(*SetMlsSearchLocators.filter_price_max)
        elem.click()
        elem.send_keys(max_price)

    # 筛选 - '卧室'下拉框 - 返回： list[element]
    def get_bedroom_element_list(self):
        return self.driver.find_elements(*SetMlsSearchLocators.filter_bedroom_list)

    # 筛选 - '更多'下拉框, 上市天数
    def get_days_on_market_text(self):
        element = self.wait_element(*SetMlsSearchLocators.filter_days_on_market)
        return SeleniumUtils.get_text_by_element(element)

    # 筛选 - '更多'下拉框, 室内面积 返回： list[element]
    def get_house_area(self):
        return self.driver.find_elements(*SetMlsSearchLocators.filter_more_area)

    # 筛选 - '更多'下拉框, 上市天数 - 返回： list[element]
    def get_days_on_market_element_list(self):
        return self.driver.find_elements(*SetMlsSearchLocators.filter_days_on_market_options)

    # 筛选 - '更多'下拉框, 车位 text
    def get_parking_space_text(self):
        element = self.wait_element(*SetMlsSearchLocators.filter_parking_space)
        return SeleniumUtils.get_text_by_element(element)

    # 筛选 - '更多'下拉框, 车位 - 返回： list[element]
    def get_parking_space_element_list(self):
        return self.driver.find_elements(*SetMlsSearchLocators.filter_parking_space_options)

    # 筛选 - '更多'下拉框, open house
    def get_open_house_text(self):
        element = self.wait_element(*SetMlsSearchLocators.filter_open_house)
        return SeleniumUtils.get_text_by_element(element)

    # 筛选 - '更多'下拉框, open house - click
    def click_open_house_toggle(self):
        self.wait_element(*SetMlsSearchLocators.filter_open_house_toggle).click()

    # 筛选 - '更多'下拉框, 价格变动
    def get_price_fluncuation_text(self):
        element = self.wait_element(*SetMlsSearchLocators.filter_price_fluncuation)
        return SeleniumUtils.get_text_by_element(element)

    # 筛选 - '更多'下拉框, click - 价格变动
    def click_price_fluncuation_toggle(self):
        self.wait_element(*SetMlsSearchLocators.filter_price_fluncuation_toggle).click()

    # 筛选 - '更多'下拉框, 无管理费
    def get_management_fee_text(self):
        element = self.wait_element(*SetMlsSearchLocators.filter_management_fee)
        return SeleniumUtils.get_text_by_element(element)

    # 筛选 - '更多'下拉框, click - 无管理费
    def click_management_fee_toggle(self):
        self.wait_element(*SetMlsSearchLocators.filter_management_fee_toggle).click()

    # 筛选 - '更多'下拉框, 管理费上限
    def get_management_fee_cap_text(self):
        element = self.wait_element(*SetMlsSearchLocators.filter_management_fee_cap)
        return SeleniumUtils.get_text_by_element(element)

    # 筛选 - '更多'下拉框, set value in 管理费上限
    def set_management_fee_cap(self, fee_cap):
        self.wait_element(*SetMlsSearchLocators.filter_management_fee_cap_input).send_keys(fee_cap)

    # 筛选 - '更多'下拉框, click - 搜索 button
    def click_more_search_button(self):
        self.wait_element(*SetMlsSearchLocators.filter_more_submit).click()

    # search box - drop down - select actived one
    def click_activated_suggest(self):
        sleep(1)
        self.wait_element(*SetMlsSearchLocators.search_activated_suggest).click()
        sleep(1)

    # 筛选条件 selected filter
    def get_selected_filter(self):
        element = self.wait_element(*SetMlsSearchLocators.filter_selected)
        return SeleniumUtils.get_text_by_element(element)

    # 选择 - "出售", "出租"，"已出售", "已出租"
    def select_transaction_type(self, transaction_type):
        self.click_sale_button()
        drop_down_element_list = self.get_sale_element_list()
        TestUtils.click_filter(drop_down_element_list, transaction_type)

    # 选择 - any building type
    def select_building_type(self, building_type):
        self.click_building_type_button()
        drop_down_element_list = self.get_building_type_element_list()
        TestUtils.click_filter(drop_down_element_list, building_type)
        self.click_building_type_confirm_button()
        sleep(1)

    # set price
    def set_price_range(self, min, max):
        self.click_price_button()
        self.set_price_min(min)
        self.click_price_button()
        self.click_price_button()
        self.set_price_max(max)
        self.click_price_button()
        sleep(1)

    # select bedroom
    def select_bedroom(self, bedroom):
        self.click_bedroom_button()
        element_list = self.get_bedroom_element_list()
        for element in element_list:
            text = SeleniumUtils.get_attribute_value(element, "value")
            if text == bedroom:
                element.click()
                break
        self.click_bedroom_button()
        sleep(1)

    # 筛选 - '更多'下拉框, 上市天数
    def select_days_on_market(self, days):
        self.click_more_button()
        element_list = self.get_days_on_market_element_list()
        TestUtils.click_filter(element_list, days)
        self.click_more_search_button()
        sleep(1)

    # 筛选 - '更多'下拉框, 室内面积
    def select_house_area(self, area):
        self.click_more_button()
        element_list = self.get_house_area()
        TestUtils.click_filter(element_list, area)
        self.click_more_search_button()
        sleep(1)

    # 今日上市 - default = 1
    @staticmethod
    def convert_days_to_int(days):
        test_day = 1
        if days == "3 天内":
            test_day = 3
        if days == "7 天内":
            test_day = 7
        if days == "14 天内":
            test_day = 14
        if days == "30 天内":
            test_day = 30
        return test_day

    # parking lots
    def select_parking_lot(self, parking):
        self.click_more_button()
        element_list = self.get_parking_space_element_list()
        for element in element_list:
            text = SeleniumUtils.get_text_by_element(element)
            if text == parking:
                SeleniumUtils.js_executor_click(self, element)
                #element.click()
                break
        self.click_more_search_button()
        sleep(1)
