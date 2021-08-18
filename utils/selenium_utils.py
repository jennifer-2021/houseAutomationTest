class SeleniumUtils:
    def __init__(self, driver):
        self.driver = driver

    def get_text(self, By, css):
        return self.driver.find_element(By, css).get_attribute("innerHTML")
