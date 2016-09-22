#coding: utf-8
from model.application import Application


class SignUpPage(object):


    def __init__(self, app: Application):
        self.app = app


    def open_sign_up_form(self):
        self.app.get_navigation_helper.open_home_page()
        self.app.get_wait_helper.implicitly_wait(3)
        self.app.get_click_element_helper.click_element(self.app.get_config("Start reading button on site"))
        self.app.get_click_element_helper.click_element(self.app.get_config("Sign in with email link"))
        self.app.get_click_element_helper.click_element(self.app.get_config("Sign up button"))


    def logout(self):
        self.app.get_click_element_helper.click_element(self.app.get_config("Start reading button"))
        self.app.get_click_element_helper.click_element(self.app.get_config("Username"))
        self.app.get_click_element_helper.click_element(self.app.get_config("Logout"))
        self.app.get_wait_helper.implicitly_wait(3)


    def sign_up(self, email_locator = None, password_locator = None, confirm_password_locator = None):
        self.open_sign_up_form()
        self.app.get_set_value_helper.set_value_field(self.app.get_config(email_locator))
        self.app.get_set_value_helper.set_value_field(self.app.get_config(password_locator))
        self.app.get_set_value_helper.set_value_field(self.app.get_config(confirm_password_locator))
        self.click_sign_up_button()
        self.app.get_wait_helper.implicitly_wait(3)


    def click_sign_up_button(self):
        self.app.get_click_element_helper.click_element(self.app.get_config("Sign up button on sing_up form"))


    def sign_up_with_correct_data_and_logout(self):
        self.sign_up("Correct data in email field", "Correct data in password field", "Correct data in confirm password field")
        self.logout()


    def login_with_incorrect_full_data(self):
        self.sign_up("Incorrect email field", "Incorrect password field", "Correct data in confirm password field")


    def send_data_into_email_field(self):
        self.open_sign_up_form()
        self.app.get_set_value_helper.set_value_field(self.app.get_config("Correct data in email field"))


    def send_data_into_password_field(self):
        self.open_sign_up_form()
        self.app.get_set_value_helper.set_value_field(self.app.get_config("Correct data in password field"))


    def send_data_into_confirm_password_field(self):
        self.open_sign_up_form()
        self.app.get_set_value_helper.set_value_field(self.app.get_config("Correct data in confirm password field"))


    def check_all_error_on_form(self):
        self.open_sign_up_form()
        self.click_sign_up_button()
        self.app.get_find_element_helper.find_and_check_count_of_elements(self.app.get_config("Error for empty data"), 3)
        self.app.get_text_element_helper.check_text_element(self.app.get_config("Error for empty data"))

        self.sign_up("Email field with broken mask", "Correct data in password field", "Correct data in confirm password field")
        self.app.get_text_element_helper.check_text_element(self.app.get_config("Error for email"))