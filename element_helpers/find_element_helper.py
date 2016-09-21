# coding: utf-8
from selenium.common.exceptions import NoSuchElementException as error
from selenium import webdriver

import logging


class FindElementHelper(object):


    # Конструктор для инициализации параметров
    def __init__(self, driver: webdriver):
        self.driver = driver


    # Проверка локатора в конфиге
    def __check_locator(self, locator):
        try:
            if locator["type"] and locator["value"]:
                print ("Ok")
        except KeyError:
            assert False


    # Проверка наличия value у элемента
    def _check_value(self, element: dict):
        try:
            if element["value"]:
                print ("Ok")
        except KeyError:
            assert False


    # Получение типа локатора и его значения из элемента в конфиге
    def _get_locator(self, element: dict):
        locator = {}
        if element.get("id"):
            locator = {"type": "id", "value": element["id"]}
        elif element.get("name"):
            locator = {"type": "name", "value": element["name"]}
        elif element.get("class"):
            locator = {"type": "class", "value": element["class"]}
        elif element.get("cssSelector"):
            locator = {"type": "cssSelector", "value": element["cssSelector"]}
        elif element.get("tag"):
            locator = {"type": "tag", "value": element["tag"]}
        elif element.get("link"):
            locator = {"type": "link", "value": element["link"]}
        elif element.get("partialLinkText"):
            locator = {"type": "partialLinkText", "value": element["partialLinkText"]}
        elif element.get("xpath"):
            locator = {"type": "xpath", "value": element["xpath"]}
        self.__check_locator(locator)
        return locator


    # Поиск элемента на странице
    def __find_element(self, element: dict):
        object_element = None
        locator = self._get_locator(element)
        try:
            if locator["type"] == "id":
                object_element = self.driver.find_element_by_id(locator["value"])
            elif locator["type"] == "name":
                object_element = self.driver.find_element_by_name(locator["value"])
            elif locator["type"] == "class":
                object_element = self.driver.find_element_by_class_name(locator["value"])
            elif locator["type"] == "cssSelector":
                object_element = self.driver.find_element_by_css_selector(locator["value"])
            elif locator["type"] == "tag":
                object_element = self.driver.find_element_by_tag_name(locator["value"])
            elif locator["type"] == "link":
                object_element = self.driver.find_element_by_link_text(locator["value"])
            elif locator["type"] == "partialLinkText":
                object_element = self.driver.find_element_by_partial_link_text(locator["value"])
            elif locator["type"] == "xpath":
                object_element = self.driver.find_element_by_xpath(locator["value"])
        except error:
            assert False
        return object_element


    # Поиск элементов на странице
    def __find_elements(self, element: dict):
        object_element = None
        locator = self._get_locator(element)
        try:
            if locator["type"] == "id":
                object_element = self.driver.find_elements_by_id(locator["value"])
            elif locator["type"] == "name":
                object_element = self.driver.find_elements_by_name(locator["value"])
            elif locator["type"] == "class":
                object_element = self.driver.find_elements_by_class_name(locator["value"])
            elif locator["type"] == "cssSelector":
                object_element = self.driver.find_elements_by_css_selector(locator["value"])
            elif locator["type"] == "tag":
                object_element = self.driver.find_elements_by_tag_name(locator["value"])
            elif locator["type"] == "link":
                object_element = self.driver.find_elements_by_link_text(locator["value"])
            elif locator["type"] == "partialLinkText":
                object_element = self.driver.find_elements_by_partial_link_text(locator["value"])
            elif locator["type"] == "xpath":
                object_element = self.driver.find_elements_by_xpath(locator["value"])
        except error:
            assert False
        return object_element


    # Получение объекта элемента на странице
    def search_element(self, element: dict) -> webdriver:
        return self.__find_element(element)


    # Получение объектов элемента на странице
    def search_elements(self, element: dict) -> webdriver:
        return self.__find_elements(element)