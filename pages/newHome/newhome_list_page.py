import time
from pages.newHome.new_home_base_page import NewhomeBasePage
from locators.newHome.locators_newhome_map import SetNewhomeMapLocators
from locators.newHome.locators_newhome_list import SetNewhomeListLocators
from utils.selenium_utils import SeleniumUtils


class NewhomeListPage(NewhomeBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 地图 - 点击地图上的点
    def click_house_point_on_map(self, listNumber):
        elements = self.driver.find_elements(*SetNewhomeMapLocators.house_on_map_points)
        self.driver.execute_script("arguments[0].click();", elements[listNumber])

    # 地图 - 点击地图上的点后，在弹窗里，点击 '查看'，进入详情页
    def click_newhome_modal_check_button(self):
        self.driver.find_element(*SetNewhomeMapLocators.newhome_modal_check_button).click()

    # 地图 - 点击地图上的点后，在弹窗里，返回 楼盘名
    def get_real_estate_name_on_modal(self):
        element = self.driver.find_element(*SetNewhomeMapLocators.real_estate_name_on_modal)
        return SeleniumUtils.get_text_by_element(element)

    # 列表 - 排序 -热门
    def click_sort_by_hot(self):
        self.wait_element(*SetNewhomeListLocators.sort_button).click()
        self.driver.find_element(*SetNewhomeListLocators.sort_by_hot).click()

    # 列表部分 - reload
    def wait_list_reload(self):
        time.sleep(0.5)
        self.wait_element(*SetNewhomeListLocators.sort_button)

    # 列表 - 返回页面上所有房源图片: list[element]
    def get_image_list(self):
        return self.driver.find_elements(*SetNewhomeListLocators.image_box)

    # 列表 - 返回页面上所有房源标签: list[element]
    def get_tag_list(self):
        return self.driver.find_elements(*SetNewhomeListLocators.tag_box)

    # 列表 - 返回页面上所有房源'热门推荐''经纪推荐': list[element]
    def get_recommendation_tag_list(self):
        return self.driver.find_elements(*SetNewhomeListLocators.recommendation)

    # 列表 - 返回页面上所有房源地址: list[element]
    def get_address_list(self):
        return self.driver.find_elements(*SetNewhomeListLocators.search_result_address_list)

    # 列表 - 返回页面上所有房源信息框: list[element]
    def get_real_estate_list(self):
        return self.driver.find_elements(*SetNewhomeListLocators.search_result_real_estate_list)

    # 列表 - 返回页面上所有房源的房型: list[element]
    def get_building_type_list(self):
        return self.driver.find_elements(*SetNewhomeListLocators.search_result_building_type_list)

    # 列表 - 返回页面上所有房源的入住时间: list[element]
    def get_checkin_time_list(self):
        return self.driver.find_elements(*SetNewhomeListLocators.search_result_checkin_time_list)

    # 列表 - 返回页面上所有房源的价格: list[element]
    def get_price_list(self):
        return self.driver.find_elements(*SetNewhomeListLocators.search_result_price_list)
