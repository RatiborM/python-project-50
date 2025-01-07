import json
import yaml

from .diff import build_diff
from .formatters.stylish import format_stylish
from .formatters.plain import format_plain


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


def generate_diff(file_path1, file_path2, format_name='stylish'):
    with open(file_path1) as f1, open(file_path2) as f2:
        if file_path1.endswith('.json'):
            data1 = json.load(f1)
            data2 = json.load(f2)
        else:
            data1 = yaml.safe_load(f1)
            data2 = yaml.safe_load(f2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return json.dumps(diff, indent=4)
    else:
        raise ValueError(f"Unknown format: {format_name}")
