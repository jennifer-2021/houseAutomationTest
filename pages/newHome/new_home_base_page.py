from pages.base_page import BasePage
from locators.newHome.locators_newhome_map import SetNewhomeMapLocators
from time import sleep


class NewhomeBasePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, config):
        home_page = config["base_page"] + "/newhome"
        self.driver.get(home_page)

    def wait_mapbox_loaded(self):
        sleep(3)
        self.wait_element(*SetNewhomeMapLocators.house_on_map_points)
        sleep(3)
