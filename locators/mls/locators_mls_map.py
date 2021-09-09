from selenium.webdriver.common.by import By


# 列表页上的地图部分
class SetMlsMapLocators:
    house_on_map_points_single = (By.CSS_SELECTOR, ".map51__single-marker")
    house_on_map_points_multi = (By.XPATH, "*//button[text()='2']")
    # transaction status buttons on map
    transaction_checkbox_list = (By.CSS_SELECTOR, ".filter-mobile-field .el51__btn")
    days_on_market = (By.CSS_SELECTOR, ".more-filters>div:nth-child(1) .el51__btn")
    deal_date = (By.CSS_SELECTOR, ".more-filters>div:nth-child(2) .el51__btn")

