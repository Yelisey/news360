# news360
Автотесты для проекта news360.com

1. /element_helpers/ - вспомогательные классы для исполнения тех или иных действий на WEB-странице: поиск элемента, клик по элементу
2. /model/ - общая точка входа во фреймворк (Application)
3. conftest.py - файл с параметрами для запуска автотестов на py.test


Запускаем тесты с помощью команды (находясь при этом в корне репозитория):

py.test

Либо

py.test --browser firefox (chrome/ie) - соответственно указываем тем самым, что запускаем на определенном браузере, но надо понимать, что для 
chrome мы должны точно указывать где лежит chromedriver (иначе будет конфликт при запуске webdriver хрома)

Лучше всего для запуска тестов использовать любую  IDE (поддерживающую python) - PyCharm к примеру
