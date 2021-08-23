from selenium.webdriver.common.by import By


class SetSearchHouseLocators:
    search_box = (By.CSS_SELECTOR, ".filter-search-input input[type='search']")
    search_button = (By.CSS_SELECTOR, ".filter-search-input>div>button")
    # search box - return one element - 'suggest menu'
    search_box_suggest_menu = (By.CSS_SELECTOR, ".filter-search-input .suggest-menu")
    # search box - drop down list - return the city element list
    search_box_suggest_city_list = (By.CSS_SELECTOR, ".filter-search-input .mls-location-item h5")
    # search result - list page - return element list
    search_result_address_list = (By.CSS_SELECTOR, ".list-wrap .address")
    # search result - list page - return element list
    search_result_building_type_list = (By.CSS_SELECTOR, ".list-wrap .building-type")
    # search result - list page - return element list (入住时间)
    search_result_checkin_time_list = (By.CSS_SELECTOR, ".list-wrap .construction-status")
    # search result - list page - return element list (price)
    search_result_price_list = (By.CSS_SELECTOR, ".list-wrap .price")
    # filter button - element '房型'
    filter_building_type_button = (By.CSS_SELECTOR, ".filter-dropdown-select")  # (By.XPATH, "//span[text()='房型']")
    # filter button - element '入住时间'
    filter_check_in_time = (By.XPATH, "//span[text()='入住时间']")
    # filter button - element 'price'
    filter_price_range_button = (By.CSS_SELECTOR, ".filter-dropdown-price-range")
    # filter - price - drop down - min price list
    filter_min_price_list = (By.CSS_SELECTOR, ".price-suggest .item[data-name='min']")
    # filter - price - drop down - max price list
    filter_max_price_list = (By.CSS_SELECTOR, ".price-suggest .item[data-name='max']")
    # filter - drop down - element list for both 'building type' & 入住时间
    filter_drop_down_list = (By.CSS_SELECTOR, ".menu.show .item")

    # map_box 上的点 - return element list - all points
    map_box_points = (By.CSS_SELECTOR, ".marker-container.mapboxgl-marker")
    # TODO: this is a dynamic element
    filter_box_city = (By.CSS_SELECTOR, ".filter-detail-box>span:nth-child(1)")
