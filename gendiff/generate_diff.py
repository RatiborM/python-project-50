#!usr/bin/env python3
import argparse
import json


def parse_argumet():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        epilog='set format of output')
    # Добавляем аргументы
    parser.add_argument('first_file', help='First file to compare.')
    parser.add_argument('second_file', help='Second file to compare.')
    parser.add_argument('-f', '--format')
    # Обрабатываем аргументы
    args = parser.parse_args()

    return {
        'first_file': args.first_file,
        'second_file': args.second_file,
    }


# Читаем и получаем данные из *.json файла
def get_data_from_file(file_json):
    with open(file_json) as handle_file:
        data = json.load(handle_file)
    return data


def generate_diff(file1_path, file2_path):
    file1 = get_data_from_file(file1_path)
    file2 = get_data_from_file(file2_path)
    keys = sorted(set(file1.keys()).union(file2.keys()))
    elem = [f'gendiff {file1_path} {file2_path}', '{']

    for key in keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if value1 == value2:
            elem.append(f'    {key}: {value1}')

        if value1 != value2:
            if value1 is not None:
                elem.append(f'  - {key}: {value1}')  # Значение из первого файла
            if value2 is not None:
                elem.append(f'  + {key}: {value2}')  # Значение из второго файла

    elem.append('}')
    return '\n'.join(elem)


def maindiff():
    arg_data = parse_argumet()
    result = generate_diff(
        arg_data['first_file'],
        arg_data['second_file'],
    )
    print(result)
