from technical.shop_user_model import ShopUser


def test_buy_goods_normal_user(get_user_data, get_login_page):
    user = ShopUser("Jan", "Kowalski", "31-666")

    login_page = get_login_page
    inventory_page = login_page.log_in_user(get_user_data["user_1"], get_user_data["pwd"])

    inventory_page.add_backpack_to_cart()
    inventory_page.add_tshirt_to_cart()

    cart_page = inventory_page.go_to_cart()
    x = 0

    std_user_cart_page.checkout()

    checkout_step1_page.enter_full_name(user.surname)

    checkout_step1_page.enter_last_name(user.surname)

    checkout_step1_page.enter_zip_code(user.zip_code)

    checkout_step1_page.click_continue()

    checkout_step2_page.click_finish()

    complete_page.click_back_home()

    complete_page.get_url()

    # sprawdzenie czy przechodzimy na wlasciwa podstronę
    # assert checkout_step2_page.get_url() == 'https://www.saucedemo.com/inventory.html'
