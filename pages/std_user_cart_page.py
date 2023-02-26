from selenium.webdriver.common.by import By
from pages.login_page import BasePage

CHECKOUT_LOCATOR = (By. ID, 'checkout')


class StdUserCartPage(BasePage):
    def __init__(self, driver, url='/cart.html'):
        super().__init__(driver, url)

    def checkout(self):
        self.driver.find_element(*CHECKOUT_LOCATOR).click()
