from selenium.webdriver.common.by import By


class SetNewhomeListLocators:
    image_box = (By.CSS_SELECTOR, ".img-box")
    recommendation = (By.CSS_SELECTOR, ".tags-wrap>.special-tag-box")
    tag_box = (By.CSS_SELECTOR, ".tags-wrap>[class='tag-box']")
