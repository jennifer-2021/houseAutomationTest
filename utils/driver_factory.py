from selenium import webdriver

PATH = 'driver/chromedriver'


class DriverFactory:
    @staticmethod
    def get_driver(browser, headless_mode=False):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless_mode is True:
                options.add_argument("--headless")
            driver = webdriver.Chrome(PATH, options=options)
            driver.maximize_window()
            return driver

        elif browser == "phantomJS":
            driver = webdriver.PhantomJS()
            driver.set_window_size(1120, 550)
            return driver

        raise Exception("Provide valid driver name")
