# coding: utf-8
from selenium import webdriver
from element_helpers.find_element_helper import FindElementHelper


class NavigationHelper(object):


    # Конструктор для инициализации параметров
    def __init__(self, driver: webdriver, base_url: str, find_element_helper: FindElementHelper):
        self.driver = driver
        self.base_url = base_url
        self.find_element_helper = find_element_helper


    # Получение протокола
    def _get_protocol(self, protocol):
        if protocol:
            protocol = "https://"
        else:
            protocol = "http://"
        return protocol


    # Открытие домашней страницы
    def open_home_page(self, https=False):
        self.__open(self.base_url, https)


    # Вспомогательный метод открытия страницы
    def __open(self, url: str, https=False):
        self.driver.get(self._get_protocol(https) + url)