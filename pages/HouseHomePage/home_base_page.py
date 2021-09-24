import time

from pages.base_page import BasePage
from locators.locators_search_common import SetSearchLocators
from selenium.common.exceptions import WebDriverException


class HomeBasePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, config):
        home_page = config["base_page"]
        try:
            self.driver.get(home_page)
        except WebDriverException:
            print(".....打不开主页.......")
        self.driver.add_cookie(config["cookie"])
        self.driver.refresh()

    def guest_open_home_page(self, config):
        home_page = config["base_page"]
        try:
            self.driver.get(home_page)
        except WebDriverException:
            print(".....打不开主页.......")

    def close_select_city_modal(self):
        try:
            self.wait_element(*SetSearchLocators.select_city_modal_close_button).click()
            time.sleep(1)
        except:
            print(".......尝试点击 选择城市弹窗，但是弹窗并不存在，测试没有中断，继续下一步.............")
