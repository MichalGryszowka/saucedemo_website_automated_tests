import json
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.std_user_inventory_page import StdUserInvPage
from pages.std_user_cart_page import StdUserCartPage
from pages.checkout_step_1_page import CheckoutSep1Page


@fixture
def init_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()


@fixture
def get_login_page(init_driver):
    return LoginPage(init_driver)


@fixture
def get_std_user_inv_page(init_driver):
    return StdUserInvPage(init_driver)


@fixture
def get_std_user_cart_page(init_driver):
    return StdUserCartPage(init_driver)


@fixture
def get_checkout_step_1_page(init_driver):
    return CheckoutSep1Page(init_driver)


@fixture
def get_user_data():
    with open(r'C:\Users\HP\PycharmProjects\Saucedemo\data\login_creds.json') as f:
        data = json.load(f)
        return data
