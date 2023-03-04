from selenium.webdriver.common.by import By
from pages.complete_page import CompletePage
from pages.login_page import BasePage

FINISH_LOCATOR = (By.ID, 'finish')


class CheckoutStep2Page(BasePage):
    def __init__(self, driver, url='/checkout-step-two.html'):
        super().__init__(driver, url)

    def click_finish(self):
        self.driver.find_element(*FINISH_LOCATOR).click()
        return CompletePage(self.driver, self.driver.current_url)

