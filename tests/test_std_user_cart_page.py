def test_std_user_cart_page(get_user_data, get_login_page, get_std_user_inv_page, get_std_user_cart_page):

    login_page = get_login_page

    std_user_inv_page = get_std_user_inv_page

    std_user_cart_page = get_std_user_cart_page

    login_page.log_in_user(get_user_data["user_1"], get_user_data["pwd"])

    std_user_inv_page.add_backpack_to_cart()

    std_user_inv_page.add_tshirt_to_cart()

    std_user_inv_page.go_to_cart()

    std_user_cart_page.checkout()