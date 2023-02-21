import json
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.standard_user_inventory_page import StdUserInvPage
from selenium.webdriver.chrome.options import Options


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
def get_user_data():
    with open(r'C:\Users\HP\PycharmProjects\Saucedemo\data\login_creds.json') as f:
        data = json.load(f)
        return data
