from selenium.webdriver.common.by import By


# 楼盘详情页
class SetDetailsPageLocators:
    real_estate_name = (By.CSS_SELECTOR, ".d-main-title h2")
    # real_estate_name = (By.XPATH, "//div[@class='d-main-title']//h2")
    swiper_button_next = (By.CSS_SELECTOR, ".swiper-button-next")
    get_free_real_estate_info = (By.CSS_SELECTOR, ".book-btn-item>button")
    maphot_button = (By.CSS_SELECTOR, ".maphot")
    loan_pre_approve_button = (By.CSS_SELECTOR, "[data-role='loan']")
    payment_cycle_subscribe_now = (By.CSS_SELECTOR, "[data-role='pay-schedule']")
    discount_policy_subscribe_now = (By.CSS_SELECTOR, "[data-role='promotion']")
    house_tour_sign_up = (By.CSS_SELECTOR, "[data-role='event-signup']")
    consult_now = (By.CSS_SELECTOR, "[data-role='contact-support']")
    photo_wall = (By.CSS_SELECTOR, ".newhouse-photo-wall .swiper-slide img")
    navbar_list = (By.CSS_SELECTOR, ".navbar-scroll li>a")
    newhome_high_light = (By.CSS_SELECTOR, ".newhome-highlights")
    promotion_anchor = (By.CSS_SELECTOR, "#anchor-promotion+div h2")
    floor_plan = (By.CSS_SELECTOR, ".floor-plan-section h2")
    related_events = (By.CSS_SELECTOR, ".related-events-blocks>header>h2")





