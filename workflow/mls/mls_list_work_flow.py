import time
from utils.selenium_utils import SeleniumUtils
import re


class MlsListWorkflow:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def verify_transaction_status(element_list, transaction_type_in_test):
        error_counter = 0
        for element in element_list:
            text = SeleniumUtils.get_text_by_element(element)
            if text == "有条件售出":
                text = "出售"
            if text == "有条件租出":
                text = "出租"
            if text != transaction_type_in_test:
                error_counter += 0
        return error_counter
