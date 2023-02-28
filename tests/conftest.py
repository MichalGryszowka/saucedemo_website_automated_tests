import json
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.std_user_inventory_page import StdUserInvPage
from pages.std_user_cart_page import StdUserCartPage
from pages.checkout_step_1_page import CheckoutStep1Page
from pages.checkout_step_2_page import CheckoutStep2Page
from pages.complete_page import CompletePage


@fixture
def main():
    pass


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
    return CheckoutStep1Page(init_driver)


@fixture
def get_checkout_step_2_page(init_driver):
    return CheckoutStep2Page(init_driver)


@fixture
def get_complete_page(init_driver):
    return CompletePage(init_driver)


@fixture
def get_user_data():
    with open("../data/login_creds.json") as f:
        data = json.load(f)
        return data
