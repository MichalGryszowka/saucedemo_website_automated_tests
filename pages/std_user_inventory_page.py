from selenium.webdriver.common.by import By
from pages.login_page import BasePage

BACKPACK_ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-sauce-labs-backpack')
TSHIRT_ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')


class StdUserInvPage(BasePage):
    def __init__(self, driver, url='/inventory.html'):
        super().__init__(driver, url)

    def add_product_to_cart(self, locator: tuple[By, str]):
        self.driver.find_element(*locator).click()
        self.driver.find_elements(*locator)

    def add_backpack_to_cart(self):
        self.add_product_to_cart(BACKPACK_ADD_TO_CART_LOCATOR)

    def add_tshirt_to_cart(self):
        self.add_product_to_cart(TSHIRT_ADD_TO_CART_LOCATOR)

    def go_to_cart(self):
        self.driver.find_element(By. CLASS_NAME, 'shopping_cart_link').click()
        return StdUserCartPage(self.driver)






