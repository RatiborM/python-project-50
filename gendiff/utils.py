import json
import yaml
from .diff import build_diff
from .formatters.stylish import format_stylish
from .formatters.plain import format_plain


def load_data(file_path):
    with open(file_path) as file:
        if file_path.endswith('.json'):
            return json.load(file)
        return yaml.safe_load(file)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return json.dumps(diff, indent=4)
    else:
        raise ValueError(f"Unknown format: {format_name}")
