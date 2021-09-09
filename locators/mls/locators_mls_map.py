from selenium.webdriver.common.by import By


# 列表页上的地图部分
class SetMlsMapLocators:
    house_on_map_points_single = (By.CSS_SELECTOR, ".map51__single-marker")
    house_on_map_points_multi = (By.XPATH, "*//button[text()='2']")
    # transaction status buttons on map
    transaction_checkbox_list = (By.CSS_SELECTOR, ".filter-mobile-field .el51__btn")
    #
    days_on_market_button = (By.XPATH, "//span[text()='上市天数']")
    sold_days_on_market_button = (By.XPATH, "//span[@class='label']/span[text()='2年内']")
    days_on_market_list = (By.CSS_SELECTOR, ".el51__dropdown.show .item")



