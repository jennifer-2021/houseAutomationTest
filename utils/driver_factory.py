from selenium import webdriver

PATH = 'driver/chromedriver'


class DriverFactory:
    @staticmethod
    def get_driver(headless_mode=False):
        options = webdriver.ChromeOptions()
        if headless_mode is True:
            options.add_argument("--headless")
        driver = webdriver.Chrome(PATH, options=options)
        driver.maximize_window()

        return driver
        raise Exception("Provide valid driver name")
