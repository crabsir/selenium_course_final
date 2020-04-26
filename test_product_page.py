import pytest
import random
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.login_guest
class TestLoginFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.go_to_login_page()

        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.should_be_login_link()


@pytest.mark.product_page_promo
class TestProductPagePromo():
    def test_guest_can_add_product_to_basket_promo(self, browser):
        link_promo = link + "?promo=newYear2019"
        page = ProductPage(browser, link_promo)
        page.open()

        page.should_be_product_promo_page()

        page.add_to_basket_promo()

        page.should_be_correct_product()
        page.should_be_correct_price()

    @pytest.mark.parametrize('offer_num', ['0', '1', '2', '3', '4', '5', '6',
                                           pytest.param('7', marks=pytest.mark.xfail),
                                           '8', '9'])
    def test_guest_can_add_product_to_basket_param(self, browser, offer_num):
        link_promo = f"{link}?promo=offer{offer_num}"
        page = ProductPage(browser, link_promo)
        page.open()

        page.should_be_product_promo_page()

        page.add_to_basket_promo()

        page.should_be_correct_product()
        page.should_be_correct_price()


@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

        page = LoginPage(browser, browser.current_url)

        page.should_be_login_page()

        random_number = str(random.randint(0, 10000))
        email = f"user_{random_number}@mail{random_number}.com"
        password = f"random_password_{random_number}"
        page.register_new_user(email, password)

        page = MainPage(browser, browser.current_url)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.add_to_basket()

        page.should_be_correct_product()
        page.should_be_correct_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket()

    page.should_be_correct_product()
    page.should_be_correct_price()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()

    page.view_basket()

    page = BasketPage(browser, browser.current_url)
    page.should_be_basket_page()
    page.should_be_empty_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()


def test_guest_should_see_correct_product_in_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    product_name = page.add_to_basket().text

    page.should_be_correct_product()
    page.should_be_correct_price()

    page.view_basket()

    page = BasketPage(browser, browser.current_url)

    page.should_be_basket_page()
    page.should_not_be_empty_basket()
    page.should_be_correct_product_in_basket(product_name)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    page.should_disappear()
