from selenium import webdriver
import pytest


class TestOne:

    def test_url(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)
        self.driver.get("http://duckduckgo.com/")
