import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self, config):
        home_page = config["base_page"] + "/newhome"
        self.driver.get(home_page)

    def wait_element(self, By, css):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By, css)))
        return element
