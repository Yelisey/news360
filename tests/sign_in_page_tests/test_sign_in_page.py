from model.base_test import BaseTest
from pages.sign_in_page.sign_in_page import SignInPage

import pytest


@pytest.fixture(scope="module")
def sign_in_page_obj(app):
    return SignInPage(app)


class TestSignInPage(BaseTest):


    def test_open_sign_in_form(self, sign_in_page_obj:SignInPage):
        sign_in_page_obj.open_sign_in_form()


    def test_send_data_into_email_field(self, sign_in_page_obj:SignInPage):
        sign_in_page_obj.send_data_into_email_field()


    def test_send_data_into_password_field(self, sign_in_page_obj:SignInPage):
        sign_in_page_obj.send_data_into_password_field()


    def test_sign_in_with_correct_data(self, sign_in_page_obj: SignInPage):
        sign_in_page_obj.login_with_correct_data_and_logout()


    def test_sign_in_with_incorrect_full_data(self, sign_in_page_obj: SignInPage):
        sign_in_page_obj.login_with_incorrect_full_data()


    def test_check_error_message(self, sign_in_page_obj: SignInPage):
        sign_in_page_obj.check_all_error_on_form()