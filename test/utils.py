import os

def get_fixture_path(filename):
    """Возвращает полный путь к файлу в директории fixtures."""
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)

def read(filepath):
    """Читает содержимое файла и возвращает его как строку."""
    with open(filepath, 'r') as file:
        return file.read()

