import json
import yaml

def parse_file(file_path):
    """Определяет формат файла по его расширению и парсит содержимое."""
    if file_path.endswith(('.yaml', '.yml')):
        return read_yaml(file_path)
    elif file_path.endswith('.json'):
        return read_json(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")

def read_json(file_path):
    """Читает и парсит JSON-файл."""
    with open(file_path, 'r') as file:
        return json.load(file)

def read_yaml(file_path):
    """Читает и парсит YAML-файл."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
