from selenium.webdriver.common.by import By
from pages.login_page import BasePage

FIRST_NAME_LOCATOR = (By.ID, 'back-to-products')


class CompletePage(BasePage):
    def __init__(self, driver, url='/checkout-complete.html'):
        super().__init__(driver, url)

    def click_back_home(self):
        self.driver.find_element(*FIRST_NAME_LOCATOR).click()
