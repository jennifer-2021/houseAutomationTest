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

    # return drop down list texts as a list
    @staticmethod
    def get_dropdown_list(elementList):
        text_list = []
        for element in elementList:
            text_list.append(SeleniumUtils.get_text_by_element(element))

        return text_list
