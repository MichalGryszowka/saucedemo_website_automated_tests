from time import sleep


def test_standard_user_login(get_login_page, get_user_data):

    login_page = get_login_page

    login_page.fill_in_user(get_user_data["user_1"])
    sleep(1)

    login_page.fill_in_pwd(get_user_data["pwd"])
    sleep(1)

    login_page.click_login_button()
    sleep(1)

    # Sprawdzenie czy przechodzimy na podstronę Inventory
    assert login_page.get_url() == 'https://www.saucedemo.com/inventory.html'


def test_failed_user_login(get_login_page, get_user_data):

    login_page = get_login_page

    login_page.fill_in_user(get_user_data["user_2"])
    sleep(1)

    login_page.fill_in_pwd(get_user_data["pwd"])
    sleep(1)

    login_page.click_login_button()
    sleep(1)

    # Sprawdzenie error message
    assert login_page.get_error_message() == 'Epic sadface: Sorry, this user has been locked out.'

    # Sprawdzenie czy zostajemy na tej samej stronie po próbie zalogowania na zablokowanego usera
    assert login_page.get_url() == 'https://www.saucedemo.com/'
    sleep(1)

    login_page.click_red_cross_button_error()
    sleep(1)

    # Sprawdzenie czy po kliknięciu krzyżyka obok błędu ramka z błędem zniknie
    assert login_page.find_error_frame() is None
    sleep(1)

# def test_problem_user_login(get_login_page):
#
#     login_page = get_login_page
#
#     login_page.fill_in_user(user_3)
#     sleep(1)
#
#     login_page.fill_in_pwd(pwd)
#     sleep(1)
#
#     login_page.click_login_button()
#     sleep(1)
#
#     # Sprawdzenie czy przechodzimy na podstronę Inventory
#     assert login_page.get_url() == 'https://www.saucedemo.com/inventory.html'

def test_delay_user_login(get_login_page, get_user_data):

    login_page = get_login_page

    login_page.fill_in_user(get_user_data["user_4"])
    # sleep(1)

    login_page.fill_in_pwd(get_user_data["pwd"])
    # sleep(1)

    login_page.click_login_button()
    # sleep(1)

    login_page.wait_for_delay_user_to_log_on()


























