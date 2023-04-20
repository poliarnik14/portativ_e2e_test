from portativ_e2e_test.portativ_testing.Model import port

def test_portativ():
    port.open()
    # Search and pick
    port.search('наушники')
    port.headphones_btn_click()
    port.first_item_click()
    port.headphones_category_click()
    port.shure_filters_choose()
    port.first_shure_click('Код товару: 24267')
    # Cart
    port.add_to_cart_click()
    port.cart_close_click()
    port.cart_open_click()
    port.cart_quantity_change()
    # Login
    port.login_link_click()
    port.login_data_input('oleksii.nizhynskyi@gmail.com', 'qwertyqwerty')
    port.login_btn_click()
    # Profile info editing
    port.customer_name_click()
    port.customer_data_click()
    port.custiomer_edit_profile_click()
    port.personal_data_change('second name')
    port.personal_data_change('test test')
    port.customer_order_list_click()
    # Add to favorite
    port.search('KOSS')
    port.headphones_btn_click()
    port.second_item_click()
    port.add_to_favorite_and_del()
    # Comparing
    port.go_back()
    port.add_to_compare_click()
    port.main_page_click()
    port.compare_shure_choose()
    port.add_to_compare_click()
    port.compare_click()
    port.compare_clear()
    port.profile_exit()
def test_negative():
    port.login_link_click()
    port.login_data_input('oleksii.nizhynskyi', 'qwertyqwerty')
    port.negative_login()
    port.login_data_input('oleksii.nizhynskyi@gmail.com', '12345')
    port.login_btn_click()
    port.negative_pass()