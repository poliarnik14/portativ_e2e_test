from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from time import sleep

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
        sleep(3)
        s('#right_filter > article > form > fieldset > div > div.filter-include > ul.filter-menu.class-aktivnoe_shumopodavlenie_anc_1368 > li > label > span > a').click()
        sleep(2)
        return self

    def first_shure_click(self, heads_name: str):
        s('/html/body/div[1]/div[4]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div[5]/a').click()
        ss('.product-sku').should(have.exact_texts(heads_name))
        return self

    def cart_test(self):
        s('/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/button').click()
        s('#modal_close').click()
        s('[href="javascript:void();"]').click()
        s('.more-btn').click()
        s('.less-btn').click().click()
        return self
    #
    def login(self, login_name: str, login_pass: str):
        s('.login-link').click()
        s('#login-email').click().type(login_name)
        s('#login-password').click().type(login_pass)
        s('.login-button').click()
        return self

    def personal_data_change (self, test_name: str, main_name: str):
        s('.header-customer-name').click()
        ss('.dashboard-link')[0].click()
        s('.edit-profile-link').click()
        s('#fullname').click().clear().type(test_name)
        s('[title="Зберегти зміни"]').click()
        s('#fullname').should(have.value(test_name))
        s('#fullname').click().clear().type(main_name)
        s('[title="Зберегти зміни"]').click()
        s('#fullname').should(have.value(main_name))


    def order_list (self):
        s('body > div.body-container > div.main-content.two-col-left.container > div.catalog-left-side > div > ul > li:nth-child(2) > a').click()
        #ss('.orders-history-list >').should(have.exact_texts('У вас ще немає замовлень.'))
        return self
    # Как сделать проверку что история заказов пустая? P.S. не смог выбрать селектор на историю заказов получше :(

    def second_item_click(self):
        ss('.cataloggrid-item-image-block')[1].click()
        return self

    def add_to_favorite (self):
        s('.catalogwishlist-add').click()
        s('[title="Обране"]').click()
        s('[title="Видалення"]').click()

    def comparing_test (self, search: str):
        s('.logo-image-link').click()
        s('[id="search-desktop"]').type(search).press_enter()
        s('.srch-res-text').click()
        sleep(2)
        s('.cataloggrid-item-image-block').click()
        sleep(2)
        s('.catalogcompare-add').click()
        ss('[itemprop = "itemListElement"]')[2].click()
        ss('.cataloggrid-item-image-block')[1].click()
        sleep(2)
        s('.catalogcompare-add').click()
        sleep(2)
        s('[title="Порівняння"]').click()

    def profile_exit (self):
        s('.header-customer-name').click()
        s('[href="https://portativ.ua/ua/customer/account/logout/"]').click()
        s('.logo-image-link').click()
        return self