import json

def parse_file(file_path):
    """Читает JSON-файл и возвращает его содержимое как словарь."""
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_diff(file_path1, file_path2):
    """Генерирует строку с разницей между двумя JSON-файлами."""
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    # Получаем объединенные ключи из обоих файлов
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key in data1 and key not in data2:
            diff.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            diff.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff.append(f"  - {key}: {data1[key]}")
            diff.append(f"  + {key}: {data2[key]}")

    return '\n'.join(diff)