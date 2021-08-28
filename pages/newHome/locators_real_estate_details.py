from selenium.webdriver.common.by import By


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




