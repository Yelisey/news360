from model.base_test import BaseTest
from pages.sign_up_page.sign_up_page import SignUpPage

import pytest


@pytest.fixture(scope="module")
def sign_up_page_obj(app):
    return SignUpPage(app)


class TestSignUpPage(BaseTest):


    def test_open_sign_up_form(self, sign_up_page_obj:SignUpPage):
        sign_up_page_obj.open_sign_up_form()


    def test_sign_up_with_correct_data(self, sign_up_page_obj: SignUpPage):
        sign_up_page_obj.sign_up_with_correct_data_and_logout()


    def test_send_data_into_email_field(self, sign_up_page_obj:SignUpPage):
        sign_up_page_obj.send_data_into_email_field()


    def test_send_data_into_password_field(self, sign_up_page_obj:SignUpPage):
        sign_up_page_obj.send_data_into_password_field()


    def test_send_data_into_confirm_password_field(self, sign_up_page_obj:SignUpPage):
        sign_up_page_obj.send_data_into_confirm_password_field()


    def test_sign_up_with_incorrect_full_data(self, sign_up_page_obj: SignUpPage):
        sign_up_page_obj.login_with_incorrect_full_data()


    def test_check_error_message(self, sign_up_page_obj: SignUpPage):
        sign_up_page_obj.check_all_error_on_form()

