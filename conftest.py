import json
import time

import pytest
from utils.driver_factory import DriverFactory

CONFIG_PATH = "config.json"
DEFAULT_WEBSITE = "https://house.51.ca/"


@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope='session')
def website_setup():
    return config['base_page'] if 'base_page' in config else DEFAULT_WEBSITE


@pytest.fixture()
def setup(request, config):
    time.sleep(2)
    driver = DriverFactory.get_driver(config["browser"], config["headless_mode"])
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    driver.maximize_window()

    yield driver
    driver.quit()
