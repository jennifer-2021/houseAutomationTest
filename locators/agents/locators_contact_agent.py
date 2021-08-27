from selenium.webdriver.common.by import By


class SetContactAgentLocators:
    loan_pre_approve_modal_title = (By.CSS_SELECTOR, "#exampleModalLabel")
    loan_pre_approve_modal_close = (By.CSS_SELECTOR, "#applyofferclose")
    free_info_modal_title = (By.XPATH, "//h5[text()='免费领取户型图&价格']")
    payment_cycle_modal_title = (By.XPATH, "//h5[text()='订阅付款周期']")
    discount_policy_modal_title = (By.XPATH, "//h5[text()='订阅优惠政策']")
    house_tour_modal_title = (By.XPATH, "//h5[text()='报名相关活动']")
    consult_now_modal_title = (By.XPATH, "//h5[text()='立即咨询小助手']")