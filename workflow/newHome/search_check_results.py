import time
from utils.selenium_utils import SeleniumUtils
import re


class CheckSearchResults:

    def __init__(self, driver):
        self.driver = driver

    # param: element_list: 列表页上房源-城市的 element list;
    # param: suggestedCity: 测试的推荐的热门城市
    # logic：点击一个热门城市后，列表上所有返回的房源地址， 必须包含 suggestedCity
    @staticmethod
    def check_city(element_list, suggestedCity):
        unexpected_result = 0
        for element in element_list:
            text_on_result = SeleniumUtils.get_text_by_element(element)
            if suggestedCity not in text_on_result:
                print("..................error address in test: " + text_on_result)
                unexpected_result += 1
        return unexpected_result

    # param: element_list: 列表页上房源-房型的 element list;
    # param: buildingType: 测试的房型
    # logic：选中一个房型后，列表上所有返回的房源的房型， 必须包含 buildingType
    # error handle: 打印出城市地址和房型
    def check_building_type(self, element_list, buildingType):
        unexpected_result = 0
        for result in element_list:
            building_info = SeleniumUtils.get_text_by_element(result)
            if buildingType not in building_info:
                print(".............Printing Error address..........................")
                parent_elem = SeleniumUtils.get_parent_element(self, result)
                error_city_elem = SeleniumUtils.get_next_sibling_element(self, parent_elem)
                error_city = SeleniumUtils.get_text_by_element(error_city_elem)
                print(building_info + "search for city: " + error_city)
                unexpected_result += 1
        return unexpected_result

    # param: result_element_list: 列表页上房源-入住时间的 element list;
    # param: checkinTime: 测试的入住时间
    # logic：选中一个入住时间后，列表上所有返回的房源的入住时间， 必须包含 checkinTime
    # error handle: 打印出城市地址和入住时间
    def checkin_time_on_list(self, result_element_list, checkinTime):
        unexpected_result = 0
        if '+' in checkinTime:
            checkinTime = int(checkinTime[0:4])
            for result in result_element_list:
                actual_checkinTime = SeleniumUtils.get_text_by_element(result)
                if actual_checkinTime != "":
                    actual_checkinTime = re.findall(r'[0-9]+', actual_checkinTime)
                    actual_checkinTime = int(actual_checkinTime[0])
                    if actual_checkinTime < checkinTime:
                        self.time_print_err_address(result)
                        unexpected_result += 1
        else:
            for result in result_element_list:
                actual_checkinTime = SeleniumUtils.get_text_by_element(result)
                if checkinTime not in actual_checkinTime:
                    print(".............Printing Error address..........................")
                    print("actual_checkinTime is:" + actual_checkinTime + "should be: " + checkinTime)
                    self.time_print_err_address(result)
                    unexpected_result += 1

        return unexpected_result

    # usage：是 checkin_time_on_list（）打印错误信息
    # param: result: 出错的 element
    # logic: 根据 出错的element，打印出该房源的地址
    def time_print_err_address(self, result):
        parent_elem = SeleniumUtils.get_parent_element(self, result)
        error_city_elem = SeleniumUtils.get_next_sibling_element(self, parent_elem)
        error_city = SeleniumUtils.get_text_by_element(error_city_elem)
        print("error city: " + error_city)

    # param: result_element_list: 列表页上房源-价格的 element list;
    # param: minPrice: 测试的最小价格 in Integer
    # param: max_price_int: 测试的最大价格 in Integer
    # logic：选中一个价格范围后，列表上所有返回的房源的价格， 必须在要求的价格范围内
    # error handle: 打印出城市地址和房源上显示的真实价格 - 调用：price_print_err_address（）
    def check_price(self, result_element_list, minPrice, max_price_int):
        unexpected_result = 0
        for element in result_element_list:
            text = SeleniumUtils.get_text_by_element(element)
            actual_start_price = SeleniumUtils.get_price_int(text)
            if '-' in text:
                actual_to_price = SeleniumUtils.get_to_price(text)
                if actual_start_price > max_price_int or actual_to_price < minPrice:
                    self.price_print_err_address(element, text)
                    unexpected_result += 1
            else:
                if actual_start_price < minPrice or actual_start_price > max_price_int:
                    self.price_print_err_address(element, text)
                    unexpected_result += 1
        return unexpected_result

    # usage：是帮助 check_price（）打印错误信息
    # param: anchor_element: 出错的 element
    # param: text: 出错房源的价格信息
    # logic: 根据 出错的element，打印出该房源的地址
    def price_print_err_address(self, anchor_element, text):
        print("......error：...actual price: " + text)
        error_city_elem = SeleniumUtils.get_previous_sibling_element(self, anchor_element)
        error_city = SeleniumUtils.get_text_by_element(error_city_elem)
        print("error city: " + error_city)

    # param: element_list: 筛选项的 element list
    # param: text_to_click: 筛选项里的字符
    # logic: 点击筛选项里的字符
    @staticmethod
    def click_filter(element_list, text_to_click):
        for element in element_list:
            name = SeleniumUtils.get_text_by_element(element)
            if name == text_to_click:
                element.click()
                time.sleep(1)
                break
