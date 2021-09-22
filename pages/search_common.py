from pages.base_page import BasePage
import time
from locators.newHome.locators_search_container import SetSearchHouseLocators
from locators.locators_search_common import SetSearchLocators


class SearchCommon(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 搜索框 - 点击搜索框 - 打开下拉框，显示热门城市
    def click_in_search_box(self):
        self.wait_element(*SetSearchHouseLocators.search_box).click()
        self.wait_element(*SetSearchHouseLocators.search_box_suggest_menu)
        time.sleep(1)

    # clear text in # 搜索框
    def clear_search_box(self):
        self.wait_element(*SetSearchHouseLocators.search_box_clear).click()
        time.sleep(0.5)

    # 搜索框 - 输入 search key
    def set_search_box_input(self, searchKey):
        self.clear_search_box()
        element = self.wait_element(*SetSearchHouseLocators.search_box)
        element.send_keys(searchKey)
        time.sleep(1)

    def click_search_box_button(self):
        self.driver.find_element(*SetSearchHouseLocators.search_button).click()

    # 搜索框 - 让下拉框保持打开状态
    def keep_search_suggest_menu_open(self):
        elem = self.wait_element(*SetSearchHouseLocators.search_box_suggest_menu)
        self.driver.execute_script("arguments[0].setAttribute('style', " + "'display: block')", elem)

    # 刚打开页面出现的 弹窗 '搜索或选择您关注的城市'
    def close_modal(self):
        self.wait_element(*SetSearchLocators.select_city_modal_close_button).click()