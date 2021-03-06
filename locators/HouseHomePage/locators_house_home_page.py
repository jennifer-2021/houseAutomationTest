from selenium.webdriver.common.by import By


class SetHouseHomePageLocators:
    # Nav bar:
    select_city_open_button = (By.CSS_SELECTOR, "#header-city-selector-root>div>button")
    search_box = (By.CSS_SELECTOR, "[class*='__searchInput'] input")
    province_list = (By.CSS_SELECTOR, "[class*='provinceWrap'] div:nth-child(1)")
    city_list = (By.CSS_SELECTOR, ".CitySelector-module__cityWrap--gcLfY [class*='city--3EVAd']>div")

    # modal
    select_area_modal = (By.CSS_SELECTOR, "//h5[text()='搜索或选择您关注的城市']")

    # hot navigation - catalogs on the top of the page
    hot_nav_list = (By.CSS_SELECTOR, ".hot-nav-list-item .title")

    # search: 找二手房 # 找新房 # 找租房 # 查成交
    search_button_list = (By.CSS_SELECTOR, ".container-md .channel-item")

    # '推荐好房' 部分
    recommendation_list = (By.CSS_SELECTOR, ".feed-list-header .nav-box a")
    # search box
    search_box_input = (By.CSS_SELECTOR, ".search-input")
    search_box_button = (By.CSS_SELECTOR, ".search-btn")

