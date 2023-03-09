from selenium.webdriver.common.by import By
from pages.login_page import BasePage
from pages.checkout_step_1_page import CheckoutStep1Page

CHECKOUT_LOCATOR = (By. ID, 'checkout')


class StdUserCartPage(BasePage):
    def __init__(self, driver, url='/cart.html'):
        super().__init__(driver, url)

    def checkout(self):
        self.driver.find_element(*CHECKOUT_LOCATOR).click()
        return CheckoutStep1Page(self.driver, self.driver.current_url)
