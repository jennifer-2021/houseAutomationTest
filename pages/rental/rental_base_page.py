from pages.base_page import BasePage
from locators.newHome.locators_newhome_map import SetNewhomeMapLocators
from time import sleep
from selenium.common.exceptions import WebDriverException


class RentalBasePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, config):
        home_page = config["base_page"] + "/rental"
        try:
            self.driver.get(home_page)
        except WebDriverException:
            print("page down")
        self.driver.add_cookie(config["cookie"])
        self.driver.refresh()

    def wait_mapbox_loaded(self):
        sleep(2)
        self.wait_element(*SetNewhomeMapLocators.house_on_map_points)
        sleep(2)
