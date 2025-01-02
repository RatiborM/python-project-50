import os
from gendiff import generate_diff


# Путь к директории, содержащей JSON и YAML файлы
base_dir = os.path.dirname(os.path.abspath(__file__))
fixtures_dir = os.path.abspath(os.path.join(base_dir, '../../test/fixtures'))


# Путь к файлам
file1_path = os.path.join(fixtures_dir, 'file1.yaml')
file2_path = os.path.join(fixtures_dir, 'file2.yaml')


# Генерация и вывод диффа
diff = generate_diff(file1_path, file2_path)
print(diff)
