from selenium.webdriver.common.by import By


class SetHomePageLocators:
    # 区域位置
    select_area_button = (By.CSS_SELECTOR, ".AreaInput-module__areaInput--3RHpI button")
    search_province_list = (By.CSS_SELECTOR, ".list-lvl1 .label")
    search_city_list = (By.CSS_SELECTOR, ".list-lvl2 .label")
    search_city_col = (By.CSS_SELECTOR, ".list-lvl2")
    search_index_list = (By.CSS_SELECTOR, ".wg51__location-cascader-menu .index-item")
    # 10 / 20 广告位，共6个
    ads_10_20_address = (By.CSS_SELECTOR, "[data-campaign^='house-rental-item'] .address")
    rental_list_address = (By.CSS_SELECTOR, ".wg51__rental-list-item .address")

