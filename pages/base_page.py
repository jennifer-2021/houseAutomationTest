import pytest
import time
from pages.newHome.locators_search_container import SetSearchHouseLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXPLICIT_WAIT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self, config):
        home_page = config["base_page"] + "/newhome"
        self.driver.get(home_page)

    def wait_element(self, By, css):
        wait = WebDriverWait(self.driver, EXPLICIT_WAIT)
        element = wait.until(EC.element_to_be_clickable((By, css)))
        return element

    def wait_mapbox_loaded(self):
        time.sleep(3)
        self.wait_element(*SetSearchHouseLocators.map_box_points)
        time.sleep(3)