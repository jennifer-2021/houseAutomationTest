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
    def get_previous_sibling_element(self, anchor_elem):
        return self.driver.execute_script("return arguments[0].previousElementSibling;", anchor_elem) #preceding-sibling

    @staticmethod
    def get_parent_element(self, anchor_elem):
        return self.driver.execute_script("return arguments[0].parentNode;", anchor_elem)

    @staticmethod
    def get_children_elements(self, anchor_elem):
        return self.driver.execute_script("return arguments[0].children;", anchor_elem)

    @staticmethod
    def get_first_child_element(self, anchor_elem):
        return self.driver.execute_script("return arguments[0].firstElementChild;", anchor_elem)

    @staticmethod
    def js_executor_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @staticmethod
    def switch_to_window(self, main_window):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)

    # return drop down list texts as a list
    @staticmethod
    def get_text_list(elementList):
        text_list = []
        for element in elementList:
            text_list.append(SeleniumUtils.get_text_by_element(element))

        return text_list

    # convert a price-range string to int(price) i.e ($2,000 - $3,000) to 2000
    @staticmethod
    def get_price_int(price_range):
        if '-' in price_range:
            price_range = price_range.split(" - ")[0]

        price = price_range.replace('$', '')
        price = price.replace(',', '')
        return int(price)

    @staticmethod
    def get_to_price(price_range):
        if '-' in price_range:
            price_range = price_range.split(" - ")[1]
            to_price = price_range.replace('$', '')
            to_price = to_price.replace(',', '')
        return int(to_price)
