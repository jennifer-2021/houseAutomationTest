from utils.selenium_utils import SeleniumUtils
import re


class CheckSearchResults:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def check_city(element_list, suggestedCity):
        for element in element_list:
            text_on_result = SeleniumUtils.get_text_by_element(element)
            if suggestedCity not in text_on_result:
                print("..................error address in test: " + text_on_result)
                return False
        return True

    def check_building_type(self, element_list, buildingType):
        for result in element_list:
            building_info = SeleniumUtils.get_text_by_element(result)
            if buildingType not in building_info:
                print(".............Printing Error address..........................")
                parent_elem = SeleniumUtils.get_parent_element(self, result)
                error_city_elem = SeleniumUtils.get_next_sibling_element(self, parent_elem)
                error_city = SeleniumUtils.get_text_by_element(error_city_elem)
                print(building_info + "search for city: " + error_city)
                return False
        return True

    def checkin_time_on_list(self, result_element_list, checkinTime):
        if '+' in checkinTime:
            checkinTime = int(checkinTime[0:4])
            for result in result_element_list:
                actual_checkinTime = SeleniumUtils.get_text_by_element(result)
                if actual_checkinTime != "":
                    actual_checkinTime = re.findall(r'[0-9]+', actual_checkinTime)
                    actual_checkinTime = int(actual_checkinTime[0])
                    if actual_checkinTime < checkinTime:
                        self.print_err_address(result)
                        return False
        else:
            for result in result_element_list:
                actual_checkinTime = SeleniumUtils.get_text_by_element(result)
                if checkinTime not in actual_checkinTime:
                    print(".............Printing Error address..........................")
                    print("actual_checkinTime is:" + actual_checkinTime + "should be: " + checkinTime)
                    self.print_err_address(result)
                    return False

        return True

    def print_err_address(self, result):
        parent_elem = SeleniumUtils.get_parent_element(self, result)
        error_city_elem = SeleniumUtils.get_next_sibling_element(self, parent_elem)
        error_city = SeleniumUtils.get_text_by_element(error_city_elem)
        print("error city: " + error_city)

    @staticmethod
    def checkPriceOnResult(result_element_list, minPrice, max_price_int):
        for element in result_element_list:
            text = SeleniumUtils.get_text_by_element(element)
            actual_start_price = SeleniumUtils.get_start_price(text)
            if '-' in text:
                actual_to_price = SeleniumUtils.get_to_price(text)
                if actual_start_price > max_price_int:
                    return False
                if actual_to_price < minPrice:
                    return False
            else:
                if actual_start_price < minPrice:
                    return False
                if actual_start_price > max_price_int:
                    return False
        return True

    @staticmethod
    def click_filter(element_list, text_to_click):
        for element in element_list:
            name = SeleniumUtils.get_text_by_element(element)
            if name == text_to_click:
                element.click()
                break
