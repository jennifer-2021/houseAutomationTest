from selenium.webdriver.common.by import By
from locators.locators_search_common import SetSearchLocators


class SetMlsSearchLocators(SetSearchLocators):
    search_box_suggested_city_list = (By.CSS_SELECTOR, ".suggest-item h5")
    filter_sale = (By.CSS_SELECTOR, ".menu-min-160.transaction-type")
    filter_building_type = (By.XPATH, "//span[text()='房型']")
    filter_building_type_confirm_selection = (By.CSS_SELECTOR, ".building-type-options button")
    filter_price = (By.CSS_SELECTOR, ".filter-dropdown-price-range .toggler")
    filter_bedroom = (By.CSS_SELECTOR, ".el51__multi-select.menu-min-160")
    filter_more = (By.CSS_SELECTOR, ".more-filter-dropdown .toggler")
    filter_sale_list = (By.CSS_SELECTOR, ".menu-min-160 .show .item")
    filter_building_type_list = (By.CSS_SELECTOR, ".building-type-options .label-txt")
    filter_building_type_list_submit = (By.CSS_SELECTOR, ".building-type-options button")
    filter_price_min = (By.CSS_SELECTOR, ".range-input .min")
    filter_price_max = (By.CSS_SELECTOR, ".range-input .max")
    filter_bedroom_list = (By.CSS_SELECTOR, ".el51__multi-select input")
    # 上市天数
    filter_days_on_market = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(1) .col-3")
    # 上市天数 - 6 options
    filter_days_on_market_options = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(1) .el51__btn")
    # 车位
    filter_parking_space = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(7) .col-3")
    filter_parking_space_options = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(7) .el51__btn")
    # 卫浴
    filter_washrooms = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(8) .col-3")
    filter_washrooms_options = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(8) .el51__btn")
    # open house
    filter_open_house = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(13) .col-3")
    filter_open_house_toggle = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(13) .switch-btn")
    # 价格变动
    filter_price_fluncuation = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(14) .col-3")
    filter_price_fluncuation_toggle = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(14) .switch-btn")
    # 无管理费
    filter_management_fee = (By.XPATH, "//label[text()='无管理费']")
    filter_management_fee_toggle = (By.CSS_SELECTOR, ".more-filters>.row:nth-child(15) .switch-btn")
    # 管理费上限
    filter_management_fee_cap = (By.XPATH, "//label[text()='管理费上限']")
    filter_management_fee_cap_input = (By.CSS_SELECTOR, "[name='maintenance-fee']")
    # 搜索 button
    filter_more_submit = (By.CSS_SELECTOR, ".more-filter-footer .el51__btn")
    # search box - activated suggestion
    search_activated_suggest = (By.CSS_SELECTOR, ".suggest-menu [data-index='0'] .overview")
    # selected filters displayed 筛选条件
    filter_selected = (By.CSS_SELECTOR, ".filter-detail-box .tag.opt:nth-child(2)")







