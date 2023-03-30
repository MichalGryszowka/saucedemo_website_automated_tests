def test_filtering_l_to_h(open_and_login_std_user):

    std_user_inv_page = open_and_login_std_user

    default_price_order = std_user_inv_page.get_list_of_prices()

    std_user_inv_page.filter_price_l_to_h()

    l_to_h_prices_order = std_user_inv_page.get_list_of_prices()

    # Checking if filtering by price L to H filters the products correctly
    assert l_to_h_prices_order == sorted(default_price_order)

