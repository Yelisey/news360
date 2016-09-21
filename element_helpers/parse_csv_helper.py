# coding: utf-8
import csv


class ParseCSV(object):


    # Парсим конфигурационный файл
    def _parse(self, file_csv, indexes: list):
        first = 0
        config_file = {}
        try:
            with open(file_csv, 'r', encoding='utf-8') as file:
                for row in csv.DictReader(file, delimiter=";", fieldnames=indexes):
                    if first == 0:
                        first += 1
                    else:
                        row = {k: v for k, v in row.items() if v}
                        config_file.update({row[indexes[0]]: row})
        except FileNotFoundError:
            assert False
        return config_file