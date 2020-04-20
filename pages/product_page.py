from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_promo_page(self):
        self.should_be_promo_url()
        self.should_be_add_to_basket_button()

    def should_be_promo_url(self):
        assert "?promo=newYear" in self.browser.current_url, "Incorrect url"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not present"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        expected_text = self.solve_quiz_and_get_code()

        assert "Поздравляем, вы справились!" in expected_text, "Incorrect alert"

    def should_be_correct_product(self):
        added_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert added_product.text == product_name.text, "Incorrect product name"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE)
        assert total_price.text == product_price.text, "Incorrect total price"
