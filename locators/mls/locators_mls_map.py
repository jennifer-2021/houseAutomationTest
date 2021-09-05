from selenium.webdriver.common.by import By


# 列表页上的地图部分
class SetMlsMapLocators:
    house_on_map_points_single = (By.CSS_SELECTOR, ".map51__single-marker")
    house_on_map_points_multi = (By.XPATH, "*//button[text()='2']")