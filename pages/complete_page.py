from selenium.webdriver.common.by import By
from pages.login_page import BasePage


class CompletePage(BasePage):
    def __init__(self, driver, url='/checkout-complete.html'):
        super().__init__(driver, url)

    def click_back_home(self):
        self.driver.find_element(By.ID, 'back-to-products').click()

    def get_url(self):
        return self.driver.current_url
