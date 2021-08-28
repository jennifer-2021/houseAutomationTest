import time

from utils.read_json import JsonReader
from utils.selenium_utils import SeleniumUtils
from utils.test_utils import TestUtils
from pages.newHome.real_estate_details_page import RealEstateDetailsPage
from pages.agents.contact_agent import ContactAgent
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestImagesAndLinks:
    testdata = JsonReader.get_details_page_buttons_data()

    @allure.title("楼盘详情页 - 图墙的图片和链接")
    @allure.description(" 验证：页面图墙的图片显示正常，图片的链接没有 broken ")
    @pytest.mark.parametrize("real_estate_url", testdata)
    def test_photo_wall_links_and_images(self, config, real_estate_url):
        # 1 打开 新房-楼盘详情页
        real_estate_details_page = RealEstateDetailsPage(self.driver)
        real_estate_details_page.open_page(config, real_estate_url)
        img_element_list = real_estate_details_page.get_photo_wall_img_elements()
        print("......total images on photo wall: " + str(len(img_element_list)))
        error_counter = 0
        for element in img_element_list:
            src = SeleniumUtils.get_src_from_img(element)
            if not TestUtils.verify_links(src):
                error_counter += 1
            if not SeleniumUtils.is_img_display(self, element):
                error_counter += 1
        assert error_counter == 0


