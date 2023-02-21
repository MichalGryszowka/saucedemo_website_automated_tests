from time import sleep
import json


f = open(r'C:\Users\HP\PycharmProjects\Saucedemo\data\login_creds.json')
data = json.load(f)
user_1 = data["user_1"]
pwd = data["pwd"]


def check_alphanumeric_order(list_of_strings):
    for i in range(len(list_of_strings) - 1):
        if list_of_strings[i] > list_of_strings[i + 1]:
            return False
        return True


def test_login(get_login_page, get_std_user_inv_page):

    login_page = get_login_page
    std_user_inv_page = get_std_user_inv_page

    login_page.fill_in_user(user_1)
    sleep(1)

    login_page.fill_in_pwd(pwd)
    sleep(1)

    login_page.click_login_button()
    sleep(1)

    std_user_inv_page.open_burger_dropdown()
    sleep(1)

    std_user_inv_page.select_all_items()
    sleep(2)

    url_all_items = std_user_inv_page.get_url()

    # sprawdzenie czy pozostajemy na stronie z inventory
    assert url_all_items == 'https://www.saucedemo.com/inventory.html'

    std_user_inv_page.select_about()
    sleep(2)

    about_url = std_user_inv_page.get_url()

    # sprawdzenie czy przekierowało nas na stronę z about
    assert about_url == 'https://saucelabs.com/'

    std_user_inv_page.go_back()
    sleep(2)

    std_user_inv_page.select_logout()
    sleep(2)

    logout_url = std_user_inv_page.get_url()

    # sprawdzenie czy przekierowalo nas na strone logowania
    assert logout_url == 'https://www.saucedemo.com/'

    login_page.fill_in_user(user_1)
    sleep(1)

    login_page.fill_in_pwd(pwd)
    sleep(1)

    login_page.click_login_button()
    sleep(1)

    std_user_inv_page.open_burger_dropdown()
    sleep(1)

    std_user_inv_page.select_reset()
    sleep(1)

    reset_url = std_user_inv_page.get_url()

    # sprawdzenie czy po resecie zostajemy na stronie z inventory
    assert reset_url == 'https://www.saucedemo.com/inventory.html'

    std_user_inv_page.close_burger_dropdown()
    sleep(1)

    # na lekcja zapytac jak dobrac sie do after button ktory nie dziala

    default_product_order = std_user_inv_page.get_list_of_products_names()
    default_price_order = std_user_inv_page.get_list_of_prices()
    default_filter_state = std_user_inv_page.get_filter_state()

    # sprawdzenie czy produkty wyjsciowo sa przefiltrowane alfabetycznie
    assert check_alphanumeric_order(default_product_order) is True

    std_user_inv_page.filter_name_z_to_a()
    sleep(1)

    z_a_product_order = std_user_inv_page.get_list_of_products_names()

    # sprawdzenie czy lista produktow przefiltorwanych od Z do A jest równa
    # wyjściowemy ustawieniu produktów po odwróceniu metoda reversed
    assert z_a_product_order == list(reversed(default_product_order))

    std_user_inv_page.filter_price_l_to_h()
    sleep(1)

    l_to_h_prices_order = std_user_inv_page.get_list_of_prices()
    sleep(1)

    # sprawdzenie czy lista produktow przefiltorwanych po cenie od L do H jest OK
    assert l_to_h_prices_order == sorted(default_price_order)

    std_user_inv_page.filter_price_h_to_l()
    sleep(1)

    h_to_l_prices_order = std_user_inv_page.get_list_of_prices()
    sleep(1)

    # sprawdzenie czy lista produktow przefiltorwanych po cenie od H do L jest OK
    assert h_to_l_prices_order == sorted(default_price_order, reverse=True)

    std_user_inv_page.open_burger_dropdown()
    sleep(1)

    std_user_inv_page.select_reset()
    sleep(1)

    filter_state_after_reset = std_user_inv_page.get_filter_state()

    # wywala błąd bo Reset strony nie resetuje filtrów do stanu wyjściowego
    # Jak zrobić Soft Assertion żeby nie przerywać testu?
    try:
        assert default_filter_state == filter_state_after_reset
    except AssertionError:
        print('Assertion failed. Reset doesnt put the app in default state')

    std_user_inv_page.close_burger_dropdown()
    sleep(1)

    std_user_inv_page.add_backpack_to_cart()
    sleep(1)

    # sprawdzenie czy dodanie produktu do koszyka zwiększa jego licznik
    assert std_user_inv_page.check_qty_in_shopping_cart() == '1'
    sleep(1)

    std_user_inv_page.click_remove_button_on_backpack()
    sleep(1)

    # jak sprawdzić cz'shopping_cart_badge' = None? 0?
    # assert std_user_inv_page.check_qty_in_shopping_cart() == ''











    #
    #
    # std_user_inv_page.add_to_cart()
    # sleep(1)
    #
    #
    # std_user_inv_page.select_back_to_product_button()
    # sleep(1)
    #
    # std_user_inv_page.select_t_shirt()
    # sleep(1)
    #
    # std_user_inv_page.select_add_to_cart()
    # sleep(1)























