from selenium.webdriver.common.by import By


class SetHomePageLocators:
    # index:
    catalog_index_list = (By.CSS_SELECTOR, ".wg51__location-cascader-menu .index-item span")

    # 区域位置
    select_area_button = (By.CSS_SELECTOR, ".AreaInput-module__areaInput--3RHpI button")
    search_province_list = (By.CSS_SELECTOR, ".list-lvl1 .label")
    search_city_list = (By.CSS_SELECTOR, ".list-lvl2 .label")
    search_city_col = (By.CSS_SELECTOR, ".list-lvl2")
    search_index_list = (By.CSS_SELECTOR, ".wg51__location-cascader-menu .index-item")
    search_subway_catalog = (By.XPATH, "//span[text()='地铁(TTC)']")
    search_university_catalog = (By.XPATH, "//span[text()='大学(安省)']")
    search_by_map_catalog = (By.XPATH, "//ul[@class='index']//span[text()='地图找房']")
    map_search_submit = (By.CSS_SELECTOR, ".modal-content .btn-primary")
    map_search_dismiss = (By.CSS_SELECTOR, ".modal-content .btn-outline-info")
    building_type_filters = (By.CSS_SELECTOR, "[class*='BuildingTypesInput'] .label-wrap")
    # 10 / 20 广告位，共6个
    ads_10_20_address = (By.CSS_SELECTOR, "[data-campaign^='house-rental-item'] .address")
    rental_list_address = (By.CSS_SELECTOR, ".wg51__rental-list-item .address")
    rental_list_building_type = (By.CSS_SELECTOR, ".wg51__rental-list-item .title")


