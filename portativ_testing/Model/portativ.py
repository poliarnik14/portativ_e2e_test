from selene import have
from selene.support.conditions import be
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

    def main_page_click (self):
        s('.logo-image-link').click()

    def search(self, port: str):
        s('[id="search-desktop"]').type(port).press_enter()
        return self

    def headphones_btn_click(self):
        s('.srch-res-text').click()
        return self

    def first_item_click(self):
        s('.cataloggrid-item-image-block').click()
        return self

    def second_item_click(self):
        ss('.cataloggrid-item-image-block')[1].click()
        return self

    def headphones_category_click(self):
        ss('[itemprop = "itemListElement"]')[2].click()
        return self

    def shure_filters_choose(self):
        s('.show-all').click()
        s('[href="https://portativ.ua/ua/category_841832.html?brand=169841"]').click()
        sleep(3)
        s('#right_filter > article > form > fieldset > div > div.filter-include > '
          'ul.filter-menu.class-aktivnoe_shumopodavlenie_anc_1368 > li > label > span > a').click()
        sleep(2)
        return self

    def first_shure_click(self, heads_name: str):
        s('/html/body/div[1]/div[4]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div[5]/a').click()
        ss('.product-sku').should(have.exact_texts(heads_name))
        return self

    def add_to_cart_click(self):
        s('/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/button').click()
        return self

    def cart_close_click(self):
        s('#modal_close').click()
        return self

    def cart_open_click(self):
        s('[href="javascript:void();"]').click()
        return self

    def cart_quantity_change(self):
        s('.more-btn').click()
        s('.less-btn').click().click()
        return self

    def login_link_click(self):
        s('.login-link').click()
        return self

    def login_data_input(self, login_name: str, login_pass: str):
        s('#login-email').click().clear().type(login_name)
        s('#login-password').click().clear().type(login_pass)
        return self

    def negative_login(self):
        s('#login-email').should(have.css_class('error'))
        return self

    def negative_pass(self):
        s('//*[@id="login-modal-form"]/ul/li[1]/div[2]').should(be.visible)
        return self

    def login_btn_click(self):
        s('.login-button').click()
        return self

    def customer_name_click(self):
        s('.header-customer-name').click()
        return self

    def customer_data_click(self):
        ss('.dashboard-link')[0].click()
        return self

    def custiomer_edit_profile_click(self):
        s('.edit-profile-link').click()
        return self

    def personal_data_change (self, test_name: str):
        s('#fullname').click().clear().type(test_name)
        s('[title="Зберегти зміни"]').click()
        s('#fullname').should(have.value(test_name))

    def customer_order_list_click (self):
        s('body > div.body-container > div.main-content.two-col-left.container > '
          'div.catalog-left-side > div > ul > li:nth-child(2) > a').click()
        s('.empty-text').should(be.visible)
        return self

    def add_to_favorite_and_del (self):
        s('.catalogwishlist-add').click()
        s('[title="Обране"]').click()
        s('[title="Видалення"]').click()
        return self

    def go_back (self):
        browser.driver.back()
        return self

    def add_to_compare_click(self):
        s('.catalogcompare-add').click()
        return self

    def compare_click(self):
        s('.catalogcompare-add').click()

    def compare_shure_choose(self):
        s('[href="https://portativ.ua/ua/product_28335.html"]').click()
        return self

    def compare_clear(self):
        s('.w-close').click().click()

    def profile_exit (self):
        self.customer_name_click()
        s('[href="https://portativ.ua/ua/customer/account/logout/"]').click()
        return self

