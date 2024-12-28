import json
import yaml


def parse_file(filepath):
    if filepath.endswith('.json'):
        return parse_json(filepath)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return parse_yaml(filepath)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")


def parse_json(filepath):
    with open(filepath) as file:
        return json.load(file)


def parse_yaml(filepath):
    with open(filepath) as file:
        return yaml.safe_load(file)
