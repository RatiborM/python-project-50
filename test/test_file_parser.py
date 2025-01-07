import pytest
import json
import yaml
from gendiff.file_parser import parse_file, parse_json, parse_yaml


def test_parse_json(tmp_path):
    # Создаем временный файл JSON
    data = {'a': 1, 'b': 2}
    file_path = tmp_path / 'test.json'
    file_path.write_text(json.dumps(data))

    # Проверяем, что функция правильно парсит JSON
    assert parse_json(file_path) == data


def test_parse_yaml(tmp_path):
    # Создаем временный файл YAML
    data = {'a': 1, 'b': 2}
    file_path = tmp_path / 'test.yaml'
    file_path.write_text(yaml.dump(data))

    # Проверяем, что функция правильно парсит YAML
    assert parse_yaml(file_path) == data


def test_parse_file_json(tmp_path):
    # Создаем временный файл JSON
    data = {'a': 1, 'b': 2}
    file_path = tmp_path / 'test.json'
    file_path.write_text(json.dumps(data))

    # Проверяем, что функция parse_file правильно парсит JSON
    assert parse_file(file_path) == data


def test_parse_file_yaml(tmp_path):
    # Создаем временный файл YAML
    data = {'a': 1, 'b': 2}
    file_path = tmp_path / 'test.yaml'
    file_path.write_text(yaml.dump(data))

    # Проверяем, что функция parse_file правильно парсит YAML
    assert parse_file(file_path) == data


def test_parse_file_unsupported_format(tmp_path):
    # Создаем временный файл с неподдерживаемым форматом
    file_path = tmp_path / 'test.txt'
    file_path.write_text('unsupported format')

    # Проверяем, что функция parse_file выбрасывает исключение для неподдерживаемого формата
    with pytest.raises(ValueError, match=r"Unsupported file format: .*"):
        parse_file(file_path)
