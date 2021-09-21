from selenium.webdriver.common.by import By


class SetSearchLocators:
    # Apply for： newHome & mls
    search_box = (By.CSS_SELECTOR, ".filter-search-input input[type='search']")
    search_box_clear = (By.CSS_SELECTOR, ".el51__autocompelete button>i")
    # Apply for： newHome & mls
    search_button = (By.CSS_SELECTOR, ".filter-search-input>div>button")
    # Apply for： newHome & mls - search box - return one element - 'suggest menu'
    search_box_suggest_menu = (By.CSS_SELECTOR, ".filter-search-input .suggest-menu")
    # Apply for： newHome & mls --- 输入楼盘名/mls后，第一个 suggestion
    search_box_real_estate = (By.CSS_SELECTOR, ".filter-desk-container .suggest-item.actived")
    # Select City Modal
    select_city_modal_close_button = (By.CSS_SELECTOR, "button[class$='module__closeBtn--3VEOw']")
