import json
import yaml
import os
import sys


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File is not a valid JSON - {file_path}")
        sys.exit(1)


def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except yaml.YAMLError:
        print(f"Error: File is not a valid YAML - {file_path}")
        sys.exit(1)


def get_file_extension(file):
    return os.path.splitext(file)[1]


def load_files(file_path):
    extension = get_file_extension(file_path)
    if extension == '.json':
        return load_json(file_path)
    elif extension == '.yaml' or extension == '.yml':
        return load_yaml(file_path)
    else:
        raise ValueError(
            f"Unsupported file format: {extension} "
            "Expected '.yaml', '.yml' or '.json'."
        )
