from pages.login_page import BasePage
from technical.locators import CompletePageLocators


class CompletePage(BasePage):
    def __init__(self, driver, url='/checkout-complete.html'):
        super().__init__(driver, url)

    def click_back_home(self):
        self.driver.find_element(*CompletePageLocators.FIRST_NAME_LOCATOR).click()
