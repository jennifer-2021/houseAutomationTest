import time
from locators.newHome.locators_search_container import SetSearchHouseLocators
from pages.newHome.new_home_base_page import NewhomeBasePage


class SearchContainer(NewhomeBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 搜索框内 - 返回全部热门城市: list[element]
    def get_suggest_cities_elements(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_box_suggest_city_list)

    # 筛选 - 点击 房型
    def click_building_type_button(self):
        self.wait_element(*SetSearchHouseLocators.filter_building_type_button).click()

    # 筛选 - 下拉框 - 返回：list[element] - 用于 房型 & 入住时间
    def get_filter_dropdown_element_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.filter_drop_down_list)

    # 筛选 - 点击 入住时间
    def click_checkin_time_button(self):
        self.wait_element(*SetSearchHouseLocators.filter_check_in_time).click()

    # 筛选 - 点击 价格
    def click_price_button(self):
        self.wait_element(*SetSearchHouseLocators.filter_price_range_button).click()

    # 筛选 - 价格的下拉框 - 返回 所有最小价格： list[element]
    def get_min_price_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.filter_min_price_list)

    # 筛选 - 价格的下拉框 - 返回 所有最大价格： list[element]
    def get_max_price_list(self):
        return self.driver.find_elements(*SetSearchHouseLocators.filter_max_price_list)

    # 搜索框 - 输入楼盘名/mls# 全称后，点击下拉框内出现的第一个推荐
    def click_suggest(self):
        time.sleep(1)
        try:
            self.wait_element(*SetSearchHouseLocators.search_box_real_estate).click()
        except:
            print(".......No such suggested item.............")
