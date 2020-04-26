from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    VIEW_BASKET = (By.XPATH, '//a[@class="btn btn-default" and contains(@href, "basket")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_TITLE = (By.XPATH, '//div[@class="page-header action"]/h1[contains(text(), "Basket")]')
    CHECKOUT_BUTTON = (By.XPATH, '//a[contains(@href, "checkout")]')
    EMPTY_BASKET = (By.XPATH, '//div[@id="content_inner"]/p[contains(text(), "Your basket is empty")]')
    PRODUCT_IMG = (By.XPATH, '//a[contains(@href, "catalogue")]/img[@class="thumbnail"]')
    PRODUCT_TITLE = (By.XPATH, '//div[@class="col-sm-4"]//a[contains(@href, "catalogue")]')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    REGISTER_FORM_ALERT = (By.CSS_SELECTOR, '.alert-danger')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASS_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_SUCCESS = (By.XPATH, '//div[contains(text(), "Thanks for registering")]')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ADDED_PRODUCT = (By.CSS_SELECTOR, '#messages>.alert-success:nth-child(1) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-success')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    VIEW_BASKET = (By.XPATH, '//a[@class="btn btn-default" and contains(@href, "basket")]')
