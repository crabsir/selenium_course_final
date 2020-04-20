import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('offer_num', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}"
    page = ProductPage(browser, link)
    page.open()

    page.should_be_product_promo_page()

    page.add_to_basket()

    page.should_be_correct_product()
    page.should_be_correct_price()
