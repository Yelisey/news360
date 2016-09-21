import pytest
from model.application import Application


class BaseTest(object):


    __test_config = "config"
    log = None


    # Задание имени конфигу
    def set_config_name(self, name_config):
        self.__test_config = name_config


    # Получение имени конфига
    def get_config_name(self):
        return self.__test_config


    # Инициализация конфигурации тестовой
    @pytest.fixture(scope="module")
    def app(self, driver, base_url: str, test_path):
        config_name = self.get_config_name()
        return Application(driver, base_url, test_path, config_name)