import os
import json
import yaml


def load_json(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        raise ValueError("Ошибка декодирования JSON")


def load_yaml(data):
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError:
        raise ValueError("Ошибка декодирования YAML")


def read_file(filepath):
    with open(filepath, 'r') as file:
            return file.read()


def get_data_format(file_path):
    ext = os.path.splitext(file_path)[1][1:].lower()
    if ext not in ['json', 'yaml', 'yml']:
        raise ValueError(f"Неподдерживаемый формат: {ext}")
    return ext


def parse_data(data, data_format):
    if data_format == 'json':
        return load_json(data)
    elif data_format in ['yaml', 'yml']:
        return load_yaml(data)
    raise ValueError(f"Неподдерживаемый формат: {data_format}")
