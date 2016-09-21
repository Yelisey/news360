from selenium import webdriver
from element_helpers.find_element_helper import FindElementHelper

import logging
import re


class TextElementHelper(object):


    # Конструктор для инициализации параметров
    def __init__(self, driver: webdriver, find_element_helper: FindElementHelper):
        self.driver = driver
        self.find_element_helper = find_element_helper


    def check_text_element(self, element: dict):
        text_element_on_page = self.get_text_element(element)
        self.find_element_helper._check_value(element)
        text_element = element["value"]
        print ("Сравнение с текстом элемента на странице")
        if text_element == text_element_on_page:
            print("Сравнение прошло успешно")
        else:
            print ("Fail")
            assert False


    def get_text_element(self, element: dict):
        object_element = self.find_element_helper.search_element(element)
        self.find_element_helper._get_locator(element)
        try:
            text_element_on_page = object_element.text
        except Exception:
            assert False
        return text_element_on_page