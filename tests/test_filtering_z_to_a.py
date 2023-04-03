def test_filtering_z_to_a(open_and_login_std_user):

    std_user_inv_page = open_and_login_std_user

    default_product_order = std_user_inv_page.get_list_of_products_names()

    std_user_inv_page.filter_name_z_to_a()

    z_a_product_order = std_user_inv_page.get_list_of_products_names()

    # Checking if filtering by name Z to A filters the products correctly
    assert z_a_product_order == list(reversed(default_product_order))
