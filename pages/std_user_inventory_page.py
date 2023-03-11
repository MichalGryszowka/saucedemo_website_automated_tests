from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from pages.std_user_cart_page import StdUserCartPage
from technical.locators import StdUserInventoryPageLocators


class StdUserInvPage(BasePage):
    def __init__(self, driver, url='/inventory.html'):
        super().__init__(driver, url)

    def add_product_to_cart(self, locator: tuple[By, str]):
        self.driver.find_element(*locator).click()

    def add_backpack_to_cart(self):
        self.add_product_to_cart(StdUserInventoryPageLocators.BACKPACK_ADD_TO_CART_LOCATOR)

    def add_tshirt_to_cart(self):
        self.add_product_to_cart(StdUserInventoryPageLocators.TSHIRT_ADD_TO_CART_LOCATOR)

    def check_qty_in_shopping_cart(self):
        cart = self.driver.find_element(*StdUserInventoryPageLocators.SHOPPING_CART_BADGE_LOCATOR)
        return cart.get_attribute('innerText')

    def go_to_cart(self):
        self.driver.find_element(*StdUserInventoryPageLocators.SHOPPING_CART_LOCATOR).click()
        return StdUserCartPage(self.driver, self.driver.current_url)

    @staticmethod
    def check_alphanumeric_order(list_of_strings):
        for i in range(len(list_of_strings) - 1):
            if list_of_strings[i] > list_of_strings[i + 1]:
                return False
            return True

    def get_list_of_products(self):
        list_of_products = ''
        all_products = self.driver.find_elements(*StdUserInventoryPageLocators.INVENTORY_CONTAINER_LOCATOR)
        for product in all_products:
            list_of_products += product.text
        res = list_of_products.split()
        return res

    def get_list_of_products_names(self):
        my_list = self.get_list_of_products()
        final_list_of_products = []
        for i in range(0, len(my_list)-1):
            if my_list[i] == 'Labs' and my_list[i+1][0] != 'b':
                final_list_of_products.append(my_list[i+1])
        return final_list_of_products

    def get_list_of_prices(self):
        my_list = self.get_list_of_products()
        final_list_of_prices = []
        for i in range(0, len(my_list)-1):
            if '$' in my_list[i]:
                final_list_of_prices.append(float(my_list[i][1:]))
        return final_list_of_prices

    def filter_name_z_to_a(self):
        drop = Select(self.driver.find_element(*StdUserInventoryPageLocators.SORT_CONTAINER_LOCATOR))
        drop.select_by_value('za')

    def filter_price_l_to_h(self):
        drop = Select(self.driver.find_element(*StdUserInventoryPageLocators.SORT_CONTAINER_LOCATOR))
        drop.select_by_value('lohi')

    def filter_price_h_to_l(self):
        drop = Select(self.driver.find_element(*StdUserInventoryPageLocators.SORT_CONTAINER_LOCATOR))
        drop.select_by_value('hilo')



