import json
from .diff import build_diff
from .formatters.stylish import format_stylish
from .formatters.plain import format_plain
from .utils import load_data

def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Генерирует различия между двумя файлами в заданном формате.

    :param file_path1: Путь к первому файлу.
    :param file_path2: Путь ко второму файлу.
    :param format_name: Формат вывода ('stylish', 'plain', 'json').
    :return: Строка с результатом различий.
    :raises ValueError: Если формат неизвестен.
    """
    try:
        data1 = load_data(file_path1)
        data2 = load_data(file_path2)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Ошибка: файл не найден. {e}")
    except Exception as e:
        raise RuntimeError(f"Ошибка при загрузке данных: {e}")

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return json.dumps(diff, indent=4)
    else:
        raise ValueError(f"Неизвестный формат: {format_name}")