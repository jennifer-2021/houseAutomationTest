from utils.selenium_utils import SeleniumUtils
from utils.read_json import JsonReader
from pages.newHome.newhome_list_page import NewhomeListPage
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestItemTags:
    testdata = JsonReader.get_tags_data()

    @allure.title("新房列表 - 房源图片上的 tag")
    @allure.description(" 验证：从列表上的房源，可以发现 all tags: 华人超市，Costco, 近大学，近地铁，GoTrain, Daycare ")
    @pytest.mark.parametrize("tagObject", testdata)
    def test_tags_on_image(self, config, tagObject):

        recommendations = tagObject["recommendation"]
        tags = tagObject["tags"]

        # 1 打开 新房首页
        list_page = NewhomeListPage(self.driver)
        list_page.open_home_page(config)
        # 2 等待 mapbox fully loaded
        list_page.wait_mapbox_loaded()
        recommendation_element_list = list_page.get_recommendation_tag_list()
        # 3 如果页面没有推荐房源，不报错
        recommendation_counter = 0
        if len(recommendation_element_list) == 0:
            print(".......... 没有任何房源推荐！....................")
        else:
            recommendation_counter = 0
            for element in recommendation_element_list:
                recommendation = SeleniumUtils.get_text_by_element(element)
                if recommendation in recommendations:
                    recommendation_counter += 1
        print("........列表页共有房源被推荐：" + str(recommendation_counter))

        # 4 如果页面没有任何tags，验证失败，立刻退出
        tag_element_list = list_page.get_tag_list()
        if len(tag_element_list) == 0:
            print(".............No any tags.....................")
            print(self.driver.current_url)
            assert False
        # 5 如果页面有所有的tag, 验证通过，否则失败
        for element in tag_element_list:
            tag_name = SeleniumUtils.get_text_by_element(element)
            if tag_name in tags:
                tags.remove(tag_name)
                if len(tags) == 0:
                    break
        print("......tags Not displayed on the list: " + str(tags))
        assert len(tags) == 0

