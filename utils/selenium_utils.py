class SeleniumUtils:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_text(self, By, css):
        return self.driver.find_element(By, css).get_attribute("innerHTML")

    @staticmethod
    def get_text_by_element(self, element):
        return element.get_attribute("innerHTML")