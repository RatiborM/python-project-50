import os
import json
import yaml


def load_json(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        raise ValueError("Ошибка декодирования JSON данных")


def load_yaml(data):
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError:
        raise ValueError("Ошибка декодирования YAML данных")


def get_file_extension(file):
    return os.path.splitext(file)[1]


def read_file(filepath):
    if not isinstance(filepath, str):
        raise TypeError(f"Ожидался строковый путь, получен {type(filepath)}")
    print(f"Открываем файл по пути: {filepath}")  # Это поможет отследить, что передается в функцию
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {filepath}")


def get_data_format(file_path):
    ext = os.path.splitext(file_path)[1][1:].lower()
    if ext not in ['json', 'yaml', 'yml']:
        raise ValueError(f"Неподдерживаемый формат данных: {ext}")
    return ext


def parse_data(data, data_format):
    if data_format == 'json':
        return load_json(data)
    elif data_format in ['yaml', 'yml']:
        return load_yaml(data)
    else:
        raise ValueError(f"Неподдерживаемый формат данных: {data_format}")
