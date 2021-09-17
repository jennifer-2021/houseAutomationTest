from pages.base_page import BasePage


class HomeBasePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, config):
        home_page = config["base_page"]
        self.driver.get(home_page)
        self.driver.add_cookie(config["cookie"])
        self.driver.refresh()
