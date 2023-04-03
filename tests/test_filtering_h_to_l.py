def test_3_filtering_h_to_l(open_and_login_std_user):

    std_user_inv_page = open_and_login_std_user

    default_price_order = std_user_inv_page.get_list_of_prices()

    std_user_inv_page.filter_price_h_to_l()

    h_to_l_prices_order = std_user_inv_page.get_list_of_prices()

    # Checking if filtering by price H to L filters the products correctly
    assert h_to_l_prices_order == sorted(default_price_order, reverse=True)

