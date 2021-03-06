#coding: utf-8
from model.application import Application


class SignInPage(object):


    def __init__(self, app: Application):
        self.app = app


    def open_sign_in_form(self):
        self.app.get_navigation_helper.open_home_page()
        self.app.get_wait_helper.implicitly_wait(3)
        self.app.get_click_element_helper.click_element(self.app.get_config("Start reading button"))
        self.app.get_click_element_helper.click_element(self.app.get_config("Sign in with email link"))


    def logout(self):
        self.app.get_click_element_helper.click_element(self.app.get_config("Username"))
        self.app.get_click_element_helper.click_element(self.app.get_config("Logout"))
        self.app.get_wait_helper.implicitly_wait(3)


    def sign_in(self, email_locator = None, password_locator = None):
        self.open_sign_in_form()
        self.app.get_set_value_helper.set_value_field(self.app.get_config(email_locator))
        self.app.get_set_value_helper.set_value_field(self.app.get_config(password_locator))
        self.click_sign_in_button()
        self.app.get_wait_helper.implicitly_wait(3)


    def click_sign_in_button(self):
        self.app.get_click_element_helper.click_element(self.app.get_config("Sign in button"))


    def send_data_into_email_field(self):
        self.open_sign_in_form()
        self.app.get_set_value_helper.set_value_field(self.app.get_config("Correct data in email field"))


    def send_data_into_password_field(self):
        self.open_sign_in_form()
        self.app.get_set_value_helper.set_value_field(self.app.get_config("Correct data in password filed"))


    def clar_data(self, email_locator, password_locator):
        self.app.get_set_value_helper.clear_field(email_locator)
        self.app.get_set_value_helper.clear_field(password_locator)


    def login_with_correct_data_and_logout(self):
        self.sign_in("Correct data in email field", "Correct data in password filed")
        self.logout()


    def login_with_incorrect_full_data(self):
        self.sign_in("Incorrect data in email field", "Incorrect data in password filed")


    def check_all_error_on_form(self):
        # self.login("Incorrect email field", "Incorrect password filed")
        # self.app.get_text_element_helper.check_text_element(self.app.get_config("Error for all field"))

        self.open_sign_in_form()
        self.click_sign_in_button()
        self.app.get_text_element_helper.check_text_element(self.app.get_config("Error for empty email"))


        self.sign_in("Email field with broken mask", "Incorrect data in password filed")
        self.app.get_text_element_helper.check_text_element(self.app.get_config("Error for email"))


        self.sign_in("Email field with space", "Correct data in password filed")
        self.app.get_text_element_helper.check_text_element(self.app.get_config("Error for email"))