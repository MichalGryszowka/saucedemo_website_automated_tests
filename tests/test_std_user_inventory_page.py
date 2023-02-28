def test_std_user_inventory(get_user_data, get_login_page, get_std_user_inv_page):

    login_page = get_login_page

    std_user_inv_page = get_std_user_inv_page

    login_page.log_in_user(get_user_data["user_1"], get_user_data["pwd"])

    std_user_inv_page.add_backpack_to_cart()

    std_user_inv_page.add_tshirt_to_cart()

    std_user_inv_page.go_to_cart()

    # sprawdzenie czy przechodzimy na podstronę z koszykiem
    assert std_user_inv_page.get_url() == 'https://www.saucedemo.com/cart.html'




















