from selenium import webdriver
from selenium.webdriver.support.select import Select
from element_helpers.find_element_helper import FindElementHelper

import logging


class SetValueHelper(object):


    # Конструктор для инициализации параметров
    def __init__(self, driver: webdriver, find_element_helper: FindElementHelper):
        self.driver = driver
        self.find_element_helper = find_element_helper


    # Записывает значение в поле на странице
    def set_value_field(self, element: dict):
        self.find_element_helper._check_value(element)
        value = element["value"]
        self.find_element_helper._get_locator(element)
        object_element = self.find_element_helper.search_element(element)
        if not object_element.is_displayed():
            objects_element = self.find_element_helper.search_elements(element)
            for obj in objects_element:
                if obj.is_displayed():
                    object_element = obj
        try:
            object_element.send_keys(value)
        except Exception:
            assert False


    # Закрытый метод очистки поля
    def __clear(self, object_element):
        try:
            object_element.clear()
        except Exception:
            assert False


    # Метод очищения поля
    def clear_field(self, element: dict):
        self.__clear(element)