import pytest
from utils.driver_factory import DriverFactory
from pages.newHome.search_container import SearchContainer


@pytest.mark.usefixtures("setup")
class TestBase:
    def __init__(self):
        self.search_container = SearchContainer(self.driver)

    def start_test(self, config):

        self.search_container.open_home_page(config)

