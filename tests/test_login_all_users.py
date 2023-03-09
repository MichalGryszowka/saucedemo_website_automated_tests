from technical.shop_user_model import UserName
from technical.shop_user_model import Password


def test_standard_user_login(get_login_page):

    login_page = get_login_page

    login_page.log_in_user(UserName.user_1, Password.pwd)

    # Checking if after logging we go to Inventory page
    assert login_page.get_url() == 'https://www.saucedemo.com/inventory.html'


def test_failed_user_login(get_login_page):

    login_page = get_login_page

    login_page.log_in_user(UserName.user_2, Password.pwd)

    # Checking if after logging on the failed user we stay on the same page
    assert login_page.get_url() == 'https://www.saucedemo.com/'

    # Checking error message text
    assert login_page.get_error_message() == 'Epic sadface: Sorry, this user has been locked out.'

    login_page.click_error_cross_button()

    # Checking if after closing error frame the error message disappears
    assert login_page.wait_for_error_frame_to_disappear() is True


def test_problem_user_login(get_login_page):

    login_page = get_login_page

    login_page.log_in_user(UserName.user_3, Password.pwd)

    # Checking if after logging we go to Inventory page
    assert login_page.get_url() == 'https://www.saucedemo.com/inventory.html'


def test_delay_user_login(get_login_page):

    login_page = get_login_page

    login_page.log_in_user(UserName.user_4, Password.pwd)

    # Checking if login frame container disappears. This acts incorrectly
    assert login_page.wait_for_delay_user_to_log_on() is True

    # Checking if after logging we go to Inventory page
    assert login_page.get_url() == 'https://www.saucedemo.com/inventory.html'


