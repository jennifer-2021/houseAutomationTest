import requests
from utils.selenium_utils import SeleniumUtils
from time import sleep


class TestUtils:

    @staticmethod
    def verify_links(link_url):
        response = requests.get(link_url)
        status_code = response.status_code
        if status_code != 200:
            print("........broken link: " + link_url + "status_code: " + status_code)
            return False
        return True

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
        price = ""
        if '-' in price_range:
            price_range = price_range.split(" - ")[0]

        price = price_range.replace('$', '')
        price = price.replace(',', '')
        return int(price)

    @staticmethod
    def get_to_price(price_range):
        to_price = ""
        if '-' in price_range:
            price_range = price_range.split(" - ")[1]
        to_price = price_range.replace('$', '')
        to_price = to_price.replace(',', '')
        return int(to_price)

    @staticmethod
    def get_bedroom(bedroom_str):
        if '+' in bedroom_str:
            bedroom_str = bedroom_str.split("+")[0]
        return int(bedroom_str)

    # param: element_list:
    # param: text:
    # logic：determine if 'text' in each string generated by element_list
    @staticmethod
    def is_text_in_string(element_list, text):
        error_counter = 0
        print("... test data: " + text)
        for element in element_list:
            actual_text = SeleniumUtils.get_text_by_element(element)
            if text not in actual_text:
                print("... test data: " + text + " not in this string: " + actual_text + ".....")
                error_counter += 1
        print("... error_counter: " + str(error_counter))
        return error_counter

    # param: element_list: 筛选项的 element list
    # param: text_to_click: 筛选项里的字符
    # logic: 点击筛选项里的字符
    @staticmethod
    def click_filter(element_list, text_to_click):
        for element in element_list:
            name = SeleniumUtils.get_text_by_element(element)
            if name == text_to_click:
                element.click()
                sleep(1)
                break

    # parse url to dictionary format
    @staticmethod
    def parse_url_get_dict(url):
        region = {}
        content = url.split("?")[1]
        contents = content.split("&")
        for c in contents:
            ary = c.split("=")
            key = ary[0]
            value = ary[1].replace("%2C%20", " ")
            value = value.replace("%20", " ")
            if key == "buildingType":
                value = value.replace("%2C", ",")
                value = value.replace("%2C", ",")
            if key != "region":
                region[key] = value

        return region

    @staticmethod
    def parse_url_get_region(url):
        region = {}
        content = url.split("?")[1]
        contents = content.split("&")
        for c in contents:
            ary = c.split("=")
            key = ary[0]
            value = ary[1].replace("%2C%20", " ")
            if key == "region":
                arry = value.split("%2C")
                value = []
                for x in arry:
                    value.append(x)
                    region[key] = value

        return region
