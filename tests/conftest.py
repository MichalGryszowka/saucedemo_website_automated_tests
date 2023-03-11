from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from technical.shop_user_model import Password
from technical.shop_user_model import UserName


@fixture
def init_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()


@fixture
def get_login_page(init_driver):
    return LoginPage(init_driver)


@fixture
def open_and_login_std_user(get_login_page):
    std_user_inv_page = get_login_page.log_in_user(UserName.user_1, Password.pwd)
    return std_user_inv_page


