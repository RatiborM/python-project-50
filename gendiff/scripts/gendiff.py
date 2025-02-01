import sys
import argparse
from gendiff.parser import read_file, get_data_format, parse_data
from gendiff.generate_diff import generate_diff


def main():
    # Инициализация парсера аргументов командной строки
    parser = argparse.ArgumentParser(
        description="Сравнение файлов для генерации различий"
    )
    parser.add_argument('first_file', help="Первый файл для сравнения")
    parser.add_argument('second_file', help="Второй файл для сравнения")
    parser.add_argument(
        '--formatter',
        choices=['json', 'plain', 'stylish'],
        default='stylish',
        help="Формат вывода"
    )

    # Получаем аргументы командной строки
    args = parser.parse_args()

    # Определяем formatter
    formatter = args.formatter

    try:
        # Чтение данных из файлов
        file1_data = read_file(args.first_file)
        file2_data = read_file(args.second_file)

        # Получение форматов данных из файлов
        file1_format = get_data_format(args.first_file)
        file2_format = get_data_format(args.second_file)

        # Парсинг данных
        data1 = parse_data(file1_data, file1_format)
        data2 = parse_data(file2_data, file2_format)

        # Генерация различий и вывод результата
        result = generate_diff(data1, data2, formatter)
        print(result)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
