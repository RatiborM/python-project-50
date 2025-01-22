import json

import yaml

from gendiff.build_diff import build_diff
from gendiff.formatters.format_json import format_json
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_stylish import format_stylish


def read_file(file):
    try:
        if file.endswith(".json"):
            with open(file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                return json.loads(content) if content else {}
        elif file.endswith((".yaml", ".yml")):
            with open(file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                return yaml.safe_load(content) if content else {}
        else:
            raise ValueError(
                """Unsupported file format.
*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
Supported formats: .json, .yaml, .yml"""
            )
    except FileNotFoundError:
        raise RuntimeError(f"File not found: {file}")
    except json.JSONDecodeError:
        raise RuntimeError(f"Error decoding JSON file: {file}")
    except yaml.YAMLError:
        raise RuntimeError(f"Error decoding YAML file: {file}")
    except Exception as e:
        raise RuntimeError(f"Error reading file {file}: {e}")


def format_diff(diff, format_name):
    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    elif format_name == "json":
        return format_json(diff)
    else:
        return "Unsupported format name"


def generate_diff(file1, file2, format_name="stylish"):
    data1 = read_file(file1)
    data2 = read_file(file2)

    diff = build_diff(data1, data2)

    return format_diff(diff, format_name)
