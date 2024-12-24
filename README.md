### Hexlet tests and linter status:
[![Actions Status](https://github.com/RatiborM/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/RatiborM/python-project-50/actions)

### Maintainability status

<a href="https://codeclimate.com/github/RatiborM/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/acd05649de1fc98c22bc/maintainability" /></a>
### Test Coverage status
<a href="https://codeclimate.com/github/RatiborM/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/acd05649de1fc98c22bc/test_coverage" /></a>


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