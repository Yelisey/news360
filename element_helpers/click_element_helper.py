# coding: utf-8
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException as error
from element_helpers.text_element_helper import TextElementHelper
from element_helpers.find_element_helper import FindElementHelper
from element_helpers.navigation_helper import NavigationHelper
from element_helpers.wait_helpers import WaitHelper



class ClickElementHelper(object):


    def __init__(self, driver: webdriver, find_element_helper: FindElementHelper,
                 navigation_helper: NavigationHelper, text_element_helper: TextElementHelper, wait_element_helper: WaitHelper):
        self.driver = driver
        assert isinstance(find_element_helper, FindElementHelper)
        self.find_element_helper = find_element_helper
        self.navigation_helper = navigation_helper
        self.text_element_helper = text_element_helper
        self.wait_element_helper = wait_element_helper


    # Нажатие на элемент страницы
    def click_element(self, element: dict):
        object_element = self.find_element_helper.search_element(element)
        self.find_element_helper._get_locator(element)
        try:
            self.__click(element, object_element, False)
        except error:
            assert False


    def __click(self, element: dict, object_element, check_text: bool):
        self.find_element_helper._get_locator(element)
        if check_text:
            self.text_element_helper.check_text_element(element)

        if object_element.is_displayed():
            object_element.click()

        else:
            objects = self.find_element_helper.search_elements(element)
            for object_element in objects:
                if object_element.is_displayed() and object_element.is_enabled():
                    self.wait_element_helper.implicitly_wait(10)
                    object_element.click()
                    break