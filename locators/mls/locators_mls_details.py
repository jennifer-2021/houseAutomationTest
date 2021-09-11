from selenium.webdriver.common.by import By


class SetMlsDetailsLocators:
    mls_name = (By.CSS_SELECTOR, ".listing-box-column input")
    # 最近成交记录
    transaction_record_nav = (By.CSS_SELECTOR, ".navbar-scroll [data-role='history-btn']")
    search_transaction_record_text = (By.CSS_SELECTOR, ".history-out-container [data-type='ask_history'] span")
    search_transaction_record_button = (By.CSS_SELECTOR, ".history-out-container [data-type='ask_history']")
    # 查询该房源全部交易历史 modal window
    transaction_record_form_title = (By.CSS_SELECTOR, ".contact-agent-box [data-role='header-text']")
    contact_agent_form_name_input = (By.CSS_SELECTOR, "#ask-surrounding-modal-form [name='name']")
    contact_agent_form_phone_input = (By.CSS_SELECTOR, "#ask-surrounding-modal-form [name='phone']")
    contact_agent_form_submit = (By.CSS_SELECTOR, "#ask-surrounding-modal-form [type='submit']")
    # 附近成交
    nearby_deal_button = (By.CSS_SELECTOR, ".container.anchor-nav-sticky [href*='map-search']")
    # 通勤计算
    commute_cal_button = (By.CSS_SELECTOR, ".anchor-nav-sticky [data-role='commute-btn'")
    # 周边地图
    surrounding_map_button = (By.CSS_SELECTOR, ".anchor-nav-sticky [data-role='map-point-btn']")
    # calculator (on top nav bar) - have modal
    calculator_button = (By.CSS_SELECTOR, ".anchor-nav-sticky [data-role*='morgage-calculator']")
    modal_calculator_title = (By.CSS_SELECTOR, "h2.App-module_modalTitle__X4yW")
    # 预估成交价 - have modal
    estimated_trans_price = (By.CSS_SELECTOR, "[data-type='ask_price_evaluation']")
    estimated_trans_price_modal_title = (By.CSS_SELECTOR, ".modal-content .icon-dollar+span")
    # 咨询更多 - have modal
    consult_more = (By.CSS_SELECTOR, ".book-btn-box [data-target='#contactQuestionsModal']")
    consult_more_modal_content = (By.CSS_SELECTOR, "#contactQuestionsModalLabel")
    # 电话咨询 - NO TEST
    phone_consult = (By.CSS_SELECTOR, "#phone-box")
    # 预约看房 not text  - Only check if the Form exist
    book_appointment = (By.CSS_SELECTOR, ".d-lg-block .contact-agent-box h3")
    # 查询该房源全部交易历史  - have modal
    search_all_deal_history = (By.CSS_SELECTOR, ".tit-box+.history-contents .book-btn-item button")

    # 房屋详情解读 - have modal
    interpret_housing_details = (By.CSS_SELECTOR, ".detail-mainkey .book-btn-box button")

    # 查询房东交易条件 - have modal
    check_landlord_trans_condition = (By.CSS_SELECTOR, ".condition-ask-block button")
    # 咨询交易费用 - have modal
    consult_trans_fee = (By.CSS_SELECTOR, ".d-aid-block .book-btn-box button")
    # 贷款计算器 - have modal
    morgage_cal = (By.CSS_SELECTOR, ".d-aid-block [data-tab='mortgage-estimate']")
    # 计算器 (in content) - have modal
    calculator = (By.CSS_SELECTOR, ".d-aid-block .cash-need-tool button")

    # 咨询学区动态 - have modal
    consult_school_district_news = (By.CSS_SELECTOR, ".icon-xuequfang")
    # 解读社区详情 - have modal
    interpret_community_details = (By.CSS_SELECTOR, ".community-tit button")
    # this modal_title css shared by all modals
    modal_title = (By.CSS_SELECTOR, ".el51__small-popup-modal-container [data-role='header-text']")





