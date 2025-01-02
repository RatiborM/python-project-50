import json
from .generate_diff import generate_diff


def read_json(file_path):
    """Читает и парсит JSON-файл."""
    with open(file_path, 'r') as file:
        return json.load(file)
