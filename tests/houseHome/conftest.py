import pytest
from pages.HouseHomePage.home_base_page import HomeBasePage
from time import sleep


@pytest.fixture()
def home_page_setup(setup, config):
    home_page = HomeBasePage(setup)
    home_page.open_home_page(config)
    sleep(1)