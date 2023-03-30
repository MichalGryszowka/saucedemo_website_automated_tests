def test_filtering_default(open_and_login_std_user):

    std_user_inv_page = open_and_login_std_user

    default_product_order = std_user_inv_page.get_list_of_products_names()

    # Checking if products are filtered by name A to Z by default
    assert std_user_inv_page.check_alphanumeric_order(default_product_order) is True

