from technical.shop_user_model import UserName
from technical.shop_user_model import Password
from pages.std_user_inventory_page import StdUserInvPage


def test_buy_2_products_std_user(get_login_page):

    login_page = get_login_page

    std_user_inv_page = login_page.log_in_user(UserName.user_1, Password.pwd)

    default_product_order = std_user_inv_page.get_list_of_products_names()

    default_price_order = std_user_inv_page.get_list_of_prices()

    # Checking if products are filtered by name A to Z by default
    assert StdUserInvPage.check_alphanumeric_order(default_product_order) is True

    std_user_inv_page.filter_name_z_to_a()

    z_a_product_order = std_user_inv_page.get_list_of_products_names()

    # Checking if filtering by name Z to A filters the products
    assert z_a_product_order == list(reversed(default_product_order))

    std_user_inv_page.filter_price_l_to_h()

    l_to_h_prices_order = std_user_inv_page.get_list_of_prices()

    # Checking if filtering by price L to H filters the products
    assert l_to_h_prices_order == sorted(default_price_order)

    std_user_inv_page.filter_price_h_to_l()

    h_to_l_prices_order = std_user_inv_page.get_list_of_prices()

    # Checking if filtering by price H to L filters the products
    assert h_to_l_prices_order == sorted(default_price_order, reverse=True)

    std_user_inv_page.add_backpack_to_cart()

    std_user_inv_page.add_tshirt_to_cart()

    std_user_cart_page = std_user_inv_page.go_to_cart()

    std_user_checkout_step_1_page = std_user_cart_page.checkout()

    std_user_checkout_step_1_page.enter_name(UserName.name)

    std_user_checkout_step_1_page.enter_last_name(UserName.last_name)

    std_user_checkout_step_1_page.enter_zip_code(UserName.zip_code)

    std_user_checkout_step_2_page = std_user_checkout_step_1_page.click_continue()

    complete_page = std_user_checkout_step_2_page.click_finish()

    complete_page.click_back_home()


