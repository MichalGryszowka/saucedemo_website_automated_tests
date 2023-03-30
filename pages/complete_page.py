from pages.login_page import BasePage
from technical.locators import CompletePageLocators


class CompletePage(BasePage):
    def __init__(self, driver, url='/checkout-complete.html'):
        super().__init__(driver, url)
        self.locators = CompletePageLocators()

    def click_back_home(self):
        self.driver.find_element(*self.locators.FIRST_NAME_LOCATOR).click()
