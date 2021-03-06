from selenium.webdriver.common.by import By


class SetNewhomeListLocators:
    image_box = (By.CSS_SELECTOR, ".img-box")
    recommendation = (By.CSS_SELECTOR, ".tags-wrap>.special-tag-box")
    tag_box = (By.CSS_SELECTOR, ".tags-wrap>[class='tag-box']")
    sort_button = (By.CSS_SELECTOR, ".list-top-box [role='button']")
    sort_by_hot = (By.CSS_SELECTOR, ".list-top-box [data-value='hot']")
    clear_filter_button = (By.CSS_SELECTOR, ".filter-detail-box .tag.clear")
    # search result - list page - return element list
    search_result_address_list = (By.CSS_SELECTOR, ".list-wrap .address")
    # search result - 楼盘 - return element list
    search_result_real_estate_list = (By.CSS_SELECTOR, ".list-wrap .info-box .name")
    # search result - list page - return element list
    search_result_building_type_list = (By.CSS_SELECTOR, ".list-wrap .building-type")
    # search result - list page - return element list (入住时间)
    search_result_checkin_time_list = (By.CSS_SELECTOR, ".list-wrap .construction-status")
    # search result - list page - return element list (price)
    search_result_price_list = (By.CSS_SELECTOR, ".list-wrap .price")
    # map_box 上的点 - return element list - all points
    map_box_points = (By.CSS_SELECTOR, ".marker-container.mapboxgl-marker")
