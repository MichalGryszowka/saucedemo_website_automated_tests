def test_standard_user_login(get_login_page, get_user_data):

    login_page = get_login_page

    login_page.log_in_user(get_user_data["user_1"], get_user_data["pwd"])

    # Sprawdzenie czy przechodzimy na podstronę Inventory
    assert login_page.get_url() == 'https://www.saucedemo.com/inventory.html'


def test_failed_user_login(get_login_page, get_user_data):

    login_page = get_login_page

    login_page.log_in_user(get_user_data["user_2"], get_user_data["pwd"])

    # Sprawdzenie czy zostajemy na tej samej stronie po próbie zalogowania na zablokowanego usera
    assert login_page.get_url() == 'https://www.saucedemo.com/'

    # Sprawdzenie wartosci error message
    assert login_page.get_error_message() == 'Epic sadface: Sorry, this user has been locked out.'

    login_page.click_error_cross_button()

    # Sprawdzenie czy po kliknięciu krzyżyka obok błędu ramka z błędem zniknie
    assert login_page.wait_for_error_frame_to_disappear() is True


def test_problem_user_login(get_login_page, get_user_data):

    login_page = get_login_page

    login_page.log_in_user(get_user_data["user_3"], get_user_data["pwd"])

    # Sprawdzenie czy przechodzimy na podstronę Inventory
    assert login_page.get_url() == 'https://www.saucedemo.com/inventory.html'


def test_delay_user_login(get_login_page, get_user_data):

    login_page = get_login_page

    login_page.log_in_user(get_user_data["user_4"], get_user_data["pwd"])

    # Sprawdzenie czy przechodzimy na podstronę Inventory
    assert login_page.get_url() == 'https://www.saucedemo.com/inventory.html'

    # To jest źle. Funkcja nie powinna zwracać True bo strona ładuje się dłużej niż zadane 2 sec
    assert login_page.wait_for_delay_user_to_log_on() is True
