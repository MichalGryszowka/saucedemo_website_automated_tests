from technical.shop_user_model import UserName


def test_buy_2_products_std_user(open_and_login_std_user):

    std_user_inv_page = open_and_login_std_user

    std_user_inv_page.add_backpack_to_cart()

    std_user_inv_page.add_tshirt_to_cart()

    std_user_cart_page = std_user_inv_page.header.go_to_cart()

    std_user_checkout_step_1_page = std_user_cart_page.checkout()

    std_user_checkout_step_1_page.enter_name(UserName.name)

    std_user_checkout_step_1_page.enter_last_name(UserName.last_name)

    std_user_checkout_step_1_page.enter_zip_code(UserName.zip_code)

    std_user_checkout_step_2_page = std_user_checkout_step_1_page.click_continue()

    complete_page = std_user_checkout_step_2_page.click_finish()

    complete_page.click_back_home()


