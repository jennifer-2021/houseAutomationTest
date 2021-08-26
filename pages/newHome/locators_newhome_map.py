from selenium.webdriver.common.by import By


class SetNewhomeMapLocators:
    house_on_map_points = (By.CSS_SELECTOR, ".map51__single-marker")
    newhome_modal_check_button = (By.CSS_SELECTOR, ".newhome-modal .el51__btn--primary")
    real_estate_name_on_modal = (By.CSS_SELECTOR, ".newhome-modal .name")