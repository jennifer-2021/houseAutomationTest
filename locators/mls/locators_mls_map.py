from selenium.webdriver.common.by import By


# 列表页上的地图部分
class SetMlsMapLocators:
    # map - house point list
    house_on_map_points_single = (By.CSS_SELECTOR, ".map51__single-marker.type-1")
    house_on_map_multi_points = (By.XPATH, "//button[text()='2']")
    # transaction status buttons on map
    transaction_checkbox_list = (By.CSS_SELECTOR, ".filter-mobile-field .el51__btn")
    #
    days_on_market_button = (By.CSS_SELECTOR, ".more-filter-selections>.el51__btn.toggler")
    sold_days_on_market_button = (By.XPATH, "//span[@class='label']/span[text()='2年内']")
    days_on_market_list = (By.CSS_SELECTOR, ".el51__dropdown.show .item")
    # school filter
    school_filter_toggle = (By.CSS_SELECTOR, ".SchoolCtrl_schoolSwitch__H_0Lt .switch-btn")
    # school filter - grade
    school_filter_grade_list = (By.CSS_SELECTOR, ".FilterMenu_gradeIcon__1jrQy+span")
    # school filter - general score
    school_filter_score_list = (By.XPATH, "//span[text()='综合评分']/following-sibling::div//input[@type='checkbox']")
    school_filter_submit = (By.CSS_SELECTOR, ".FilterMenu_searchFooter__3Kdu_ button")
    # school search result
    school_elementary_label = (By.XPATH, "//div[text()='小学']")
    school_middle_school_label = (By.XPATH, "//div[text()='初中']")
    school_high_school_label = (By.XPATH, "//div[text()='高中']")
    school_filter_score_label = (By.CSS_SELECTOR, ".SchoolItem_rankContent__1p-t5.undefined b")
    # modal on map
    modal_go_to_details_button = (By.CSS_SELECTOR, "a[href*='house-mls-map']")
    modal_multi_house_1st = (By.CSS_SELECTOR, ".multi-container a:nth-child(1)")






