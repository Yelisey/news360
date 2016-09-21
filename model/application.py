from selenium import webdriver
from element_helpers.click_element_helper import ClickElementHelper
from element_helpers.load_config_helper import LoadConfigHelper
from element_helpers.navigation_helper import NavigationHelper
from element_helpers.parse_csv_helper import ParseCSV
from element_helpers.find_element_helper import FindElementHelper
from element_helpers.set_value_helper import SetValueHelper
from element_helpers.text_element_helper import TextElementHelper
from element_helpers.wait_helpers import WaitHelper

import logging


class Application(object):


    # Конструктор для инициализации параметров
    def __init__(self, driver: webdriver, base_url: str, test_path: str, test_config: str):
        self.driver = driver
        self.base_url = base_url
        self.test_path = test_path
        self.config_name = test_config


    @property
    def get_navigation_helper(self) -> NavigationHelper:
        return NavigationHelper(self.driver, self.base_url, self.get_find_element_helper)


    @property
    def get_find_element_helper(self) -> FindElementHelper:
        return FindElementHelper(self.driver)


    @property
    def get_click_element_helper(self) -> ClickElementHelper:
        return ClickElementHelper(self.driver, self.get_find_element_helper, self.get_navigation_helper,
                                  self.get_text_element_helper, self.get_wait_helper)


    @property
    def get_set_value_helper(self) -> SetValueHelper:
        return SetValueHelper(self.driver, self.get_find_element_helper)


    @property
    def get_text_element_helper(self) -> TextElementHelper:
        return TextElementHelper(self.driver, self.get_find_element_helper)


    @property
    def get_parse_csv(self) -> ParseCSV:
        return ParseCSV()


    @property
    def get_wait_helper(self) -> WaitHelper:
        return WaitHelper(self.driver)


    @property
    def get_load_config(self) -> LoadConfigHelper:
        return LoadConfigHelper(self.get_parse_csv, self.test_path, self.config_name)


    def get_config(self, element_name: str):
        config_file = self.get_load_config._get_config()
        try:
            element_from_config = None
            if element_name is not None:
                element_from_config = config_file[element_name]
            else:
                print("Вы не указали имя элемента")
            return element_from_config
        except KeyError:
            assert False