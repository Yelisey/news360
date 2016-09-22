# coding: utf-8
from selenium import webdriver


class WaitHelper(object):


    # Конструктор для инициализации параметров
    def __init__(self, driver: webdriver):
        self.driver = driver


    # Неявное ожидание
    def implicitly_wait(self, timeout):
        self.driver.implicitly_wait(timeout)