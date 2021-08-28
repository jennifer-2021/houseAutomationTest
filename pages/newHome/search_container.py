import time
from locators.newHome.locators_search_container import SetSearchHouseLocators
from pages.base_page import BasePage


class SearchContainer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 搜索框 - 点击搜索框 - 打开下拉框，显示热门城市
    def click_in_search_box(self):
        self.wait_mapbox_loaded()
        self.wait_element(*SetSearchHouseLocators.search_box).click()
        self.wait_element(*SetSearchHouseLocators.search_box_suggest_menu)

    # 搜索框 - 输入楼盘名全称后，点击下拉框内出现的第一个推荐
    def click_real_estate_suggest(self):
        time.sleep(1)
        try:
            self.wait_element(*SetSearchHouseLocators.search_box_real_estate).click()
        except:
            print(".......No such suggested Real Estate.............")

    # 搜索框内 - 返回全部热门城市: list[element]
    def get_suggest_cities_elements(self):
        return self.driver.find_elements(*SetSearchHouseLocators.search_box_suggest_city_list)

    def set_search_box_input(self, searchKey):
        element = self.wait_element(*SetSearchHouseLocators.search_box)
        element.send_keys(searchKey)

    def click_search_box_button(self):
        self.driver.find_element(*SetSearchHouseLocators.search_button).click()

    # 搜索框 - 让下拉框保持打开状态
    def keep_search_suggest_menu_open(self):
        elem = self.wait_element(*SetSearchHouseLocators.search_box_suggest_menu)
        self.driver.execute_script("arguments[0].setAttribute('style', " + "'display: block')", elem)
        return self

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
