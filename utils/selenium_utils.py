class SeleniumUtils:

    @staticmethod
    def get_text(self, By, css):
        return self.driver.find_element(By, css).get_attribute("innerHTML")

    @staticmethod
    def get_text_by_element(element):
        return element.get_attribute("innerHTML")

    @staticmethod
    def get_next_sibling_element(self, anchor_elem):
        return self.driver.execute_script("return arguments[0].nextElementSibling;", anchor_elem)

    @staticmethod
    def get_parent_element(self, anchor_elem):
        return self.driver.execute_script("return arguments[0].parentNode;", anchor_elem)