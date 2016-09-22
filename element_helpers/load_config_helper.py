from element_helpers.parse_csv_helper import ParseCSV

import configparser
import os


class LoadConfigHelper(object):


    __config = None


    # Конструктор для инициализации параметров
    def __init__(self, parse_csv: ParseCSV, test_path: str, config_name: str):
        self.parse_csv = parse_csv
        self.config_name = config_name
        self.test_path = test_path
        self.indexes_test_config = ("element_name", "value", "id", "name", "class", "cssSelector", "tag", "link",
                                    "partialLinkText", "xpath")
        self.__download_test_config(self.indexes_test_config)


    #Загружаем конфигурационный файл
    def __download_test_config(self, indexes_test_config):
        config_file = os.path.join(self.test_path, "config", self.config_name + ".csv")
        self.__config = self.parse_csv._parse(config_file, indexes_test_config)


    #Получаем конфигурационный файл
    def _get_config(self):
        return self.__config


    #читаем конфигурационный файл для testrail
    def _read_testrail_config_file(config_file: str):
        config = configparser.ConfigParser()
        config.read(config_file)
        return config