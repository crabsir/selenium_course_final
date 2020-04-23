from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_title()

    def should_be_basket_title(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TITLE), "Basket title is not present"

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Incorrect url"

    def should_be_correct_product_in_basket(self, product_name):
        assert product_name in self.find_elements_text(*BasketPageLocators.PRODUCT_TITLE), \
            "Not found expected product in basket"

    def should_be_empty_basket(self):
        self.should_be_empty_basket_title()
        self.should_not_be_product_in_basket()

    def should_be_empty_basket_title(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "No empty basket text"

    def should_be_proceed_to_checkout_button(self):
        assert self.is_element_present(*BasketPageLocators.CHECKOUT_BUTTON), "Checkout button is not present"

    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_TITLE), "Basket is empty"

    def should_not_be_empty_basket(self):
        self.should_not_be_empty_basket_title()
        self.should_be_product_in_basket()

    def should_not_be_empty_basket_title(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Empty basket text is displayed"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_TITLE), "Found a product in the basket"
