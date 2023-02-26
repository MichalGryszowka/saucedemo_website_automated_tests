from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import urllib3.exceptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.login_page import BasePage

BACKPACK_ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-sauce-labs-backpack')
TSHIRT_ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')


class StdUserInvPage(BasePage):
    def __init__(self, driver, url='/inventory.html'):
        super().__init__(driver, url)

    def add_product_to_cart(self, locator: tuple[By, str]):
        self.driver.find_element(*locator).click()

    def add_backpack_to_cart(self):
        self.add_product_to_cart(BACKPACK_ADD_TO_CART_LOCATOR)

    def add_tshirt_to_cart(self):
        self.add_product_to_cart(TSHIRT_ADD_TO_CART_LOCATOR)

    def go_to_cart(self):
        self.driver.find_element(By. CLASS_NAME, 'shopping_cart_link').click()

    def get_url(self):
        return self.driver.current_url




















    #
    # def add_to_cart(self, locator: tuple[By, str]) -> str | None:
    #     product = self.driver.find_element(*locator)
    #     return product.get_attribute("value")
    #

    #
    # def open_burger_dropdown(self):
    #     return self.driver.find_element(By.ID, 'react-burger-menu-btn').click()
    #
    # def close_burger_dropdown(self):
    #     return self.driver.find_element(By.ID, 'react-burger-cross-btn').click()
    #
    # def select_all_items(self):
    #     all_items = self.driver.find_element(By.ID, 'inventory_sidebar_link')
    #     all_items.click()
    #
    # def select_about(self):
    #     about = self.driver.find_element(By.ID, 'about_sidebar_link')
    #     about.click()
    #
    # def select_logout(self):
    #     logout = self.driver.find_element(By.ID, 'logout_sidebar_link')
    #     logout.click()
    #
    # def go_back(self):
    #     self.driver.back()
    #
    # def select_reset(self):
    #     reset = self.driver.find_element(By.ID, 'reset_sidebar_link')
    #     reset.click()
    #
    # def get_list_of_products(self):
    #     list_of_products = ''
    #     all_products = self.driver.find_elements(By. CLASS_NAME, "inventory_container")
    #     for product in all_products:
    #         list_of_products += product.text
    #     res = list_of_products.split()
    #     return res
    #
    # def get_list_of_products_names(self):
    #     my_list = self.get_list_of_products()
    #     final_list_of_products = []
    #     for i in range(0, len(my_list)-1):
    #         if my_list[i] == 'Labs' and my_list[i+1][0] != 'b':
    #             final_list_of_products.append(my_list[i+1])
    #     return final_list_of_products
    #
    # def get_list_of_prices(self):
    #     my_list = self.get_list_of_products()
    #     final_list_of_prices = []
    #     for i in range(0, len(my_list)-1):
    #         if '$' in my_list[i]:
    #             final_list_of_prices.append(float(my_list[i][1:]))
    #     return final_list_of_prices
    #
    # def filter_name_a_to_z(self):
    #     drop = Select(self.driver.find_element(By. CLASS_NAME, 'product_sort_container'))
    #     drop.select_by_value('az')
    #
    # def filter_name_z_to_a(self):
    #     drop = Select(self.driver.find_element(By. CLASS_NAME, 'product_sort_container'))
    #     drop.select_by_value('za')
    #
    # def filter_price_l_to_h(self):
    #     drop = Select(self.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    #     drop.select_by_value('lohi')
    #
    # def filter_price_h_to_l(self):
    #     drop = Select(self.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    #     drop.select_by_value('hilo')
    #
    # def get_filter_state(self):
    #     options = Options()
    #     options.add_experimental_option("detach", True)
    #     filters = self.driver.find_element(By.CLASS_NAME, "active_option")
    #     actual_value = filters.get_attribute('innerText')
    #     return actual_value
    #

    #
    # def check_qty_in_shopping_cart(self):
    #     cart = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    #     return cart.get_attribute('innerText')
    #
    # def click_remove_button_on_backpack(self):
    #     remove = self.driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    #     remove.click()
    #
    # def select_back_to_product_button(self):
    #     product = self.driver.find_element(By.ID, 'back-to-products')
    #     product.click()
    #
    # def select_t_shirt(self):
    #     product = self.driver.find_element(By.ID, 'item_1_title_link')
    #     product.click()






