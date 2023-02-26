from selenium.webdriver.common.by import By
from pages.login_page import BasePage


FIRST_NAME_LOCATOR = (By.ID, 'first-name')
LAST_NAME_LOCATOR = (By.ID, 'last-name')
ZIP_CODE_LOCATOR = (By.ID, 'postal-code')
CONTINUE_LOCATOR = (By.ID, 'continue')


class CheckoutSep1Page(BasePage):
    def __init__(self, driver, url='/checkout-step-one.html'):
        super().__init__(driver, url)

    def get_input_frame(self, locator):
        return self.driver.find_element(*locator)

    def enter_full_name(self, name):
        self.get_input_frame(FIRST_NAME_LOCATOR).send_keys(name)

    def enter_last_name(self, last_name):
        self.get_input_frame(LAST_NAME_LOCATOR).send_keys(last_name)

    def enter_zip_code(self, zip_code):
        self.get_input_frame(ZIP_CODE_LOCATOR).send_keys(zip_code)

    def click_continue(self):
        self.get_input_frame(CONTINUE_LOCATOR).click()
