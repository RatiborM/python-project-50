import json
import os

def read_json(file_path):
    """Читает и парсит JSON-файл."""
    with open(file_path, 'r') as file:
        return json.load(file)

# Путь к директории, содержащей JSON-файлы
base_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(base_dir, '../../test/fixtures'))

# Путь к файлам
file1_path = os.path.join(project_dir, 'file1.json')
file2_path = os.path.join(project_dir, 'file2.json')

# Чтение и парсинг файлов
data1 = read_json(file1_path)
data2 = read_json(file2_path)

# Вывод данных для проверки
print("Содержимое file1.json:")
print(data1)
print("\nСодержимое file2.json:")
print(data2)
