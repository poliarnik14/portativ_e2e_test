from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from time import sleep
from portativ_testing.Model import port

def test_portativ():
    port.open()
    port.search('навушники')
    port.headphones_btn()
    port.first_item_click()
    port.headphones_cat()
    port.shure_choose()


    sleep(3)