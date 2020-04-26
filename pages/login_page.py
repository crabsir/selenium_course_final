from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_register_form()

        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS)
        pass_field.send_keys(password)
        pass_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS_CONFIRM)
        pass_confirm_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

        self.should_not_be_alert()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Incorrect url"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def should_be_registry_success_message(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_SUCCESS), "No success message for registry"

    def should_not_be_alert(self):
        assert self.is_not_element_present(*LoginPageLocators.REGISTER_FORM_ALERT), "Alert raised during registration"
