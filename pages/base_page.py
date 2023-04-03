from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'
        self.url = url
        self.get()

    def get(self):
        full_url = self.base_url + self.url
        if self.url not in self.driver.current_url:
            self.driver.get(full_url)

    def get_url(self):
        return self.driver.current_url

    def select_by(self, string: str, locator: tuple[By, str]):
        drop = Select(self.driver.find_element(*locator))
        drop.select_by_value(string)
