import pytest
from pages.rental.home_page import HomePage
from time import sleep


@pytest.fixture()
def rental_setup(setup, config):
    home_page = HomePage(setup)
    home_page.open_home_page(config)
    sleep(1)


