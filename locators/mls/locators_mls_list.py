from selenium.webdriver.common.by import By


class SetMlsListLocators:
    image_box = (By.CSS_SELECTOR, ".img-box")
    recommendation = (By.CSS_SELECTOR, "")
    tag_box = (By.CSS_SELECTOR, "")
    sort_button = (By.CSS_SELECTOR, ".list-selection-mode [role='button']")
    sort_select_list = (By.CSS_SELECTOR, ".el51__dropdown .menu.show button")
    clear_filter_button = (By.CSS_SELECTOR, ".filter-detail-box .tag.clear")
    # search result - list page - return element list
    search_result_address_list = (By.CSS_SELECTOR, ".list-wrap .address")
    # search result - 楼盘 - return element list
    search_result_real_estate_list = (By.CSS_SELECTOR, "")
    # search result - list page - return element list
    search_result_building_type_list = (By.CSS_SELECTOR, "")
    # search result - list page - return element list (入住时间)
    search_result_checkin_time_list = (By.CSS_SELECTOR, "")
    # search result - list page - return element list (price)
    search_result_price_list = (By.CSS_SELECTOR, ".list-wrap .price")
    # map_box 上的点 - return element list - all points
    map_box_points = (By.CSS_SELECTOR, ".marker-container.mapboxgl-marker")
    # transaction type
    list_transaction_type = (By.CSS_SELECTOR, ".el51__transaction-type-tag span")
    # transaction type tag on image
    list_sold_transaction_type = (By.CSS_SELECTOR, "img[src*='icon_sold']")
    # transaction type tag on image
    list_leased_transaction_type = (By.CSS_SELECTOR, "img[src*='icon_leased']")
    # bedrooms on list
    search_result_bedroom_list = (By.CSS_SELECTOR, ".item-col.bed span")
    # days on market
    search_result_days_on_market_list = (By.CSS_SELECTOR, ".item-col.time")
    # parking
    search_result_parking_list = (By.CSS_SELECTOR, ".paking span")




