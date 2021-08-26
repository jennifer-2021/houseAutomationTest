from selenium.webdriver.common.by import By


class SetNewhomeListLocators:
    image_box = (By.CSS_SELECTOR, ".img-box")
    recommendation = (By.CSS_SELECTOR, ".tags-wrap>.special-tag-box")
    tag_box = (By.CSS_SELECTOR, ".tags-wrap>[class='tag-box']")
    sort_button = (By.CSS_SELECTOR, ".list-top-box [role='button']")
    sort_by_hot = (By.CSS_SELECTOR, ".list-top-box [data-value='hot']")
    clear_filter_button = (By.CSS_SELECTOR, ".filter-detail-box .tag.clear")
