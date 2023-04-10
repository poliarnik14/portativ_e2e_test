from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from time import sleep
from portativ_e2e_test.portativ_testing.Model import port

def test_portativ():
    port.open()
    port.search('наушники')
    port.headphones_btn()
    port.first_item_click()
    port.headphones_cat()
    port.shure_choose()
    port.first_shure_click('Код товару: 28335')
    port.cart_test()
    port.login('oleksii.nizhynskyi@gmail.com', 'qwertyqwerty')
    port.personal_data_change('second name', 'test test')
    port.order_list()
    port.search('KOSS')
    port.second_item_click()
    port.add_to_favorite()
    # port.comparing_test('Audio-Technica')

    port.profile_exit()
    sleep(3)