from model.base_test import BaseTest
from pages.login_page.login_page import MainPage

import pytest


@pytest.fixture(scope="module")
def main_page_obj(app):
    return MainPage(app)


class TestMainPage(BaseTest):


    def test_open_sign_form(self, main_page_obj:MainPage):
        main_page_obj.open_sign_form()


    def test_send_data_into_email_field(self, main_page_obj:MainPage):
        main_page_obj.send_data_into_email_field()


    def test_send_data_into_password_field(self, main_page_obj:MainPage):
        main_page_obj.send_data_into_password_field()


    def test_login_with_correct_data(self, main_page_obj: MainPage):
        main_page_obj.login_with_correct_data_and_logout()


    def test_login_with_incorrect_full_data(self, main_page_obj: MainPage):
        main_page_obj.login_with_incorrect_full_data()


    def test_check_error_message(self, main_page_obj: MainPage):
        main_page_obj.check_all_error_on_form()
