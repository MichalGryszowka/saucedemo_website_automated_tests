from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.std_user_cart_page import StdUserCartPage
from technical.locators import HeaderStdUserInvPageLocators
from technical.locators import StdUserInvPageLocators


class HeaderStdUserInvPage(BasePage):
    def __init__(self, driver, url='/inventory.html'):
        super().__init__(driver, url)
        self.locators = HeaderStdUserInvPageLocators()

    def go_to_cart(self):
        self.driver.find_element(*self.locators.SHOPPING_CART_LOCATOR).click()
        return StdUserCartPage(self.driver, self.driver.current_url)


class StdUserInvPage(BasePage):
    def __init__(self, driver, url='/inventory.html'):
        super().__init__(driver, url)
        self.locators_h = HeaderStdUserInvPageLocators()
        self.locators_p = StdUserInvPageLocators()
        self.header = HeaderStdUserInvPage(driver)

    def check_qty_in_shopping_cart(self):
        cart = self.driver.find_element(*self.locators_h.SHOPPING_CART_BADGE_LOCATOR)
        return cart.get_attribute('innerText')

    def get_list_of_products(self):
        list_of_products = ''
        all_products = self.driver.find_elements(*self.locators_h.INVENTORY_CONTAINER_LOCATOR)
        for product in all_products:
            list_of_products += product.text
        res = list_of_products.split()
        return res

    def get_list_of_products_names(self):
        my_list = self.get_list_of_products()
        final_list_of_products = []
        for i in range(len(my_list) - 1):
            if my_list[i] == 'Labs' and my_list[i + 1][0] != 'b':
                final_list_of_products.append(my_list[i + 1])
        return final_list_of_products

    def get_list_of_prices(self):
        my_list = self.get_list_of_products()
        final_list_of_prices = []
        for i in range(0, len(my_list) - 1):
            if '$' in my_list[i]:
                final_list_of_prices.append(float(my_list[i][1:]))
        return final_list_of_prices

    def filter_name_z_to_a(self):
        self.select_by('za', self.locators_h.SORT_CONTAINER_LOCATOR)

    def filter_price_l_to_h(self):
        self.select_by('lohi', self.locators_h.SORT_CONTAINER_LOCATOR)

    def filter_price_h_to_l(self):
        self.select_by('hilo', self.locators_h.SORT_CONTAINER_LOCATOR)

    @staticmethod
    def check_alphanumeric_order(list_of_strings):
        for i in range(len(list_of_strings) - 1):
            if list_of_strings[i] > list_of_strings[i + 1]:
                return False
            return True

    def add_product_to_cart(self, locator: tuple[By, str]):
        self.driver.find_element(*locator).click()

    def add_backpack_to_cart(self):
        self.add_product_to_cart(self.locators_p.BACKPACK_ADD_TO_CART_LOCATOR)

    def add_tshirt_to_cart(self):
        self.add_product_to_cart(self.locators_p.TSHIRT_ADD_TO_CART_LOCATOR)



