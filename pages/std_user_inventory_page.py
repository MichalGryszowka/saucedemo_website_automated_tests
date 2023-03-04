from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.std_user_cart_page import StdUserCartPage

BACKPACK_ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-sauce-labs-backpack')
TSHIRT_ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
SHOPPING_CART_LOCATOR = (By. CLASS_NAME, 'shopping_cart_link')
SHOPPING_CART_BADGE_LOCATOR = (By. CLASS_NAME, 'shopping_cart_badge')


class StdUserInvPage(BasePage):
    def __init__(self, driver, url='/inventory.html'):
        super().__init__(driver, url)

    def add_product_to_cart(self, locator: tuple[By, str]):
        self.driver.find_element(*locator).click()

    def add_backpack_to_cart(self):
        self.add_product_to_cart(BACKPACK_ADD_TO_CART_LOCATOR)

    def add_tshirt_to_cart(self):
        self.add_product_to_cart(TSHIRT_ADD_TO_CART_LOCATOR)

    def check_qty_in_shopping_cart(self):
        cart = self.driver.find_element(*SHOPPING_CART_BADGE_LOCATOR)
        return cart.get_attribute('innerText')

    def go_to_cart(self):
        self.driver.find_element(*SHOPPING_CART_LOCATOR).click()
        return StdUserCartPage(self.driver, self.driver.current_url)






