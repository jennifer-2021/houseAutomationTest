
from pages.base_page import BasePage
from locators.newHome.locators_newhome_map import SetNewhomeMapLocators
from locators.locators_search_common import SetSearchLocators
from selenium.common.exceptions import WebDriverException
from time import sleep


class MlsBasePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, config):
        home_page = config["base_page"] + "/mls"
        try:
           self.driver.get(home_page)
        except WebDriverException:
            print("page down")
        self.driver.add_cookie(config["cookie"])
        self.driver.refresh()

    def close_select_city_modal(self):
        try:
            self.wait_element(*SetSearchLocators.select_city_modal_close_button).click()
        except:
            print("........No Select City Modal Pops up.............")

    def wait_mapbox_loaded(self):
        sleep(2)
        self.wait_element(*SetNewhomeMapLocators.house_on_map_points)
        sleep(2)
