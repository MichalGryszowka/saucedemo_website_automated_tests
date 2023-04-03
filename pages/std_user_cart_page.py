from pages.checkout_step_1_page import CheckoutStep1Page
from pages.login_page import BasePage
from technical.locators import StdUserCartPageLocators


class StdUserCartPage(BasePage):
    def __init__(self, driver, url='/cart.html'):
        super().__init__(driver, url)
        self.locators = StdUserCartPageLocators

    def checkout(self):
        self.driver.find_element(*self.locators.CHECKOUT_LOCATOR).click()
        return CheckoutStep1Page(self.driver, self.driver.current_url)
