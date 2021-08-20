from selenium.webdriver.common.by import By


class SetSearchHouseLocators:
    search_box = (By.CSS_SELECTOR, ".filter-search-input input[type='search']")
    search_button = (By.CSS_SELECTOR, ".filter-search-input>div>button")
    search_box_suggest_menu = (By.CSS_SELECTOR, ".filter-search-input .suggest-menu")
    # search box - all cities on dropdown list
    search_box_suggest_cities = (By.CSS_SELECTOR, ".filter-search-input .mls-location-item h5")
    # all listed house address on the page
    search_result_address_list = (By.CSS_SELECTOR, ".list-wrap .address")
    # all listed house building type on the page
    search_result_building_type_list = (By.CSS_SELECTOR, ".list-wrap .building-type")
    # building type
    filter_building_type_button = (By.XPATH, "//span[text()='房型']")
    # 入住时间
    filter_check_in_time = (By.XPATH, "//span[text()='入住时间']")
    # price range
    filter_price_range = (By.CSS_SELECTOR, ".filter-dropdown-price-range")
    # get dropdown list values of 'building type' or 入住时间
    filter_menu_items = (By.CSS_SELECTOR, ".menu.show .item")
    # map_box 上的点
    map_box_points = (By.CSS_SELECTOR, ".marker-container.mapboxgl-marker")
    filter_box_city = (By.CSS_SELECTOR, ".filter-detail-box>span:nth-child(1)")

