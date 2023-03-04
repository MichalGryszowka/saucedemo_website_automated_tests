from technical.shop_user_model import UserName
from technical.shop_user_model import Password


def test_buy_2_products_std_user(get_login_page):

    login_page = get_login_page

    std_user_inv_page = login_page.log_in_user(UserName.user_1, Password.pwd)

    std_user_inv_page.add_backpack_to_cart()

    std_user_inv_page.add_tshirt_to_cart()

    # Checking if adding product increases badge counter
    assert std_user_inv_page.check_qty_in_shopping_cart() == '2'

    std_user_cart_page = std_user_inv_page.go_to_cart()

    std_user_checkout_step_1_page = std_user_cart_page.checkout()

    std_user_checkout_step_1_page.enter_name(UserName.name)

    std_user_checkout_step_1_page.enter_last_name(UserName.last_name)

    std_user_checkout_step_1_page.enter_zip_code(UserName.zip_code)

    std_user_checkout_step_2_page = std_user_checkout_step_1_page.click_continue()

    complete_page = std_user_checkout_step_2_page.click_finish()

    complete_page.click_back_home()

