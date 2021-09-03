from selenium.webdriver.common.by import By
from locators.locators_search_common import SetSearchLocators


class SetSearchHouseLocators(SetSearchLocators):
    # search box - drop down list - return the city element list
    search_box_suggest_city_list = (By.CSS_SELECTOR, ".filter-search-input .mls-location-item h5")
    # filter button - element '房型'
    filter_building_type_button = (By.CSS_SELECTOR, ".filter-dropdown-select")
    # filter button - element '入住时间'
    filter_check_in_time = (By.XPATH, "//span[text()='入住时间']")
    # filter - price - drop down - min price list
    filter_min_price_list = (By.CSS_SELECTOR, ".price-suggest .item[data-name='min']")
    # filter - price - drop down - max price list
    filter_max_price_list = (By.CSS_SELECTOR, ".price-suggest .item[data-name='max']")
    # filter - drop down - element list for both 'building type' & 入住时间
    filter_drop_down_list = (By.CSS_SELECTOR, ".menu.show .item")
    # filter button - 'price'
    filter_price_range_button = (By.CSS_SELECTOR, ".filter-dropdown-price-range")

    # TODO: this is a dynamic element
    filter_box_city = (By.CSS_SELECTOR, ".filter-detail-box>span:nth-child(1)")
