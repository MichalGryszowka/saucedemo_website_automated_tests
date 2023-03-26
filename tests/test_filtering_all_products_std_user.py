def test_3_filtering_all_products_std_user(open_and_login_std_user):

    std_user_inv_page = open_and_login_std_user

    default_product_order = std_user_inv_page.get_list_of_products_names()

    default_price_order = std_user_inv_page.get_list_of_prices()

    # Checking if products are filtered by name A to Z by default
    assert std_user_inv_page.check_alphanumeric_order(default_product_order) is True

    std_user_inv_page.filter_name_z_to_a()

    z_a_product_order = std_user_inv_page.get_list_of_products_names()

    # Checking if filtering by name Z to A filters the products correctly
    assert z_a_product_order == list(reversed(default_product_order))

    std_user_inv_page.filter_price_l_to_h()

    l_to_h_prices_order = std_user_inv_page.get_list_of_prices()

    # Checking if filtering by price L to H filters the products correctly
    assert l_to_h_prices_order == sorted(default_price_order)

    std_user_inv_page.filter_price_h_to_l()

    h_to_l_prices_order = std_user_inv_page.get_list_of_prices()

    # Checking if filtering by price H to L filters the products correctly
    assert h_to_l_prices_order == sorted(default_price_order, reverse=True)

