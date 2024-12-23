### Hexlet tests and linter status:
[![Actions Status](https://github.com/RatiborM/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/RatiborM/python-project-50/actions)


DESCRIPTION:
Вычислитель отличий

Запускается из командной строки и вычисляет отличия между двумя файлами. На данный момент работает с JSON и YAML.

Установка Через клонирование репозитория

$ git clone git@github.com:kazyamov/python-project-50.git
And install dependencies

$ make install
or

$ poetry install
Запуск справки:

gendiff -h

Запуск скрипта c настройками по-умолчанию:

gendiff <file_path1> <file_path2>

Сравнение двух плоских файлов: JSON. asciicast

Сравнение двух плоских файлов: YAML(YML). asciicast

Сравнение двух файлов c рекурсивной структурой: YAML(YML) или JSON. asciicast

Плоский формат отображения - cравнение двух файлов c рекурсивной структурой YAML(YML) или JSON. asciicast

Вывод результата сравнения в формате JSON. asciicast