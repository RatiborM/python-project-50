import json
import yaml
from pathlib import Path
from .diff import build_diff
from .formatters.stylish import format_stylish


def parse_file(file_path):
    file_path = Path(file_path)
    if file_path.suffix in ('.yaml', '.yml'):
        return read_yaml(file_path)
    elif file_path.suffix == '.json':
        return read_json(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    if format_name == 'stylish':
        return format_stylish(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")


def flatten(data, parent_key='', sep='.'):
    """Функция для преобразования вложенного словаря в плоский словарь."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
