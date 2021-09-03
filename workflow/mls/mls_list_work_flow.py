import time
from utils.selenium_utils import SeleniumUtils
import re


class MlsListPage:

    def __init__(self, driver):
        self.driver = driver

