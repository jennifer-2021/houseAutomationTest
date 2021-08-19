from selenium.webdriver.common.by import By


class SetSearchHouseLocators:
    search_box = (By.CSS_SELECTOR, ".filter-search-input input[type='search']")
    search_button = (By.CSS_SELECTOR, ".filter-search-input>div>button")
    search_box_suggest_menu = (By.CSS_SELECTOR, ".filter-search-input .suggest-menu")
    search_box_suggest_cities = (By.CSS_SELECTOR, ".filter-search-input .mls-location-item h5")
    search_result_list = (By.CSS_SELECTOR, ".list-wrap .address")
    #
    filter_box_city = (By.CSS_SELECTOR, ".filter-detail-box>span:nth-child(1)")

