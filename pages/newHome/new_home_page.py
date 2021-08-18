from pages.base_page import BasePage


class NewhomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_all_house_types(self):
        self.wait_element()
