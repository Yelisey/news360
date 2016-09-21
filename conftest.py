from selenium import webdriver


import pytest
import os
import time


#переопределенные атрибуты py.test
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Type of browser: [\"name of browser\"]")
    parser.addoption("--base_url", action="store", default="news360.com", help="Base URL")


#тип браузера
@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


#базовый url
@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


#инициализация драйвера
@pytest.fixture(scope="session")
def driver(request, browser_type):
    if "firefox" == browser_type:
        driver = webdriver.Firefox()
    elif "chrome" == browser_type:
        driver = webdriver.Chrome()
    elif "ie" == browser_type:
        driver = webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(15)
    request.addfinalizer(driver.quit)
    return driver


#фикстура для определения директории, где хранятся тесты
@pytest.fixture(scope="module")
def test_path(request):
    return request.fspath.dirname