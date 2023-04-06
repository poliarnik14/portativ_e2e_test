from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

class Portativ:
    def __init__(self):
        self.base_url = 'https://portativ.ua/ua/'

    def open(self):
        browser.open('https://portativ.ua/ua/')
        browser.driver.maximize_window()
        return self

    def search(self, port: str):
        s('[id="search-desktop"]').type(port).press_enter()
        return self

    def headphones_btn(self):
        s('.srch-res-text').click()
        return self

    def first_item_click(self):
        s('.cataloggrid-item-image-block').click()
        return self

    def headphones_cat(self):
        ss('[itemprop = "itemListElement"]')[2].click()
        return self

    def shure_choose(self):
        s('.show-all').click()
        s('[href="https://portativ.ua/ua/category_841832.html?brand=169841"]').click()
        #ss('.hide').element_by(have.exact_text('Shure')).click()
        #s('//label[contains(.,"Є")]/input').click()
        return self


