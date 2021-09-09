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
        return self.driver.execute_script("return arguments[0].previousElementSibling;",
                                          anchor_elem)  # preceding-sibling

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

    # img_element - 选到 <img ...> 的node级别
    @staticmethod
    def is_img_display(self, img_element):
        return self.driver.execute_script(
            "return (typeof arguments[0].naturalWidth !=\"undefined\" && arguments[0].naturalWidth > 0);", img_element);

    @staticmethod
    def js_executor_send_keys(self, key, element):
        script = "arguments[0].value=" + key + ";"
        self.driver.execute_script(script, element)

    @staticmethod
    def get_src_from_img(img_element):
        return img_element.get_attribute("src")

    @staticmethod
    def get_attribute_value(element, attribute):
        return element.get_attribute(attribute)

    @staticmethod
    def switch_to_window(self, main_window):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)

