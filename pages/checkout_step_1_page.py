from pages.checkout_step_2_page import CheckoutStep2Page
from pages.login_page import BasePage
from technical.locators import CheckoutStep1PageLocators


class CheckoutStep1Page(BasePage):
    def __init__(self, driver, url='/checkout-step-one.html'):
        super().__init__(driver, url)
        self.locators = CheckoutStep1PageLocators()

    def get_input_frame(self, locator):
        return self.driver.find_element(*locator)

    def enter_name(self, name):
        self.get_input_frame(self.locators.FIRST_NAME_LOCATOR).send_keys(name)

    def enter_last_name(self, last_name):
        self.get_input_frame(self.locators.LAST_NAME_LOCATOR).send_keys(last_name)

    def enter_zip_code(self, zip_code):
        self.get_input_frame(self.locators.ZIP_CODE_LOCATOR).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*self.locators.CONTINUE_LOCATOR).click()
        return CheckoutStep2Page(self.driver, self.driver.current_url)

