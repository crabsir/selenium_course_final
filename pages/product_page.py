from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT)

    def add_to_basket_promo(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        expected_text = self.solve_quiz_and_get_code()

        assert expected_text is not None, "Incorrect alert"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not present"

    def should_be_correct_product(self):
        added_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert added_product.text == product_name.text, "Incorrect product name"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE)
        assert total_price.text == product_price.text, "Incorrect total price"

    def should_be_product_promo_page(self):
        self.should_be_promo_url()
        self.should_be_add_to_basket_button()

    def should_be_promo_url(self):
        assert "?promo=" in self.browser.current_url, "Incorrect url"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear but didn't"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
