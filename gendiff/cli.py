import argparse
from gendiff.generate_diff import generate_diff


def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Generate diff')

    # Добавляем аргументы для файлов
    parser.add_argument('first_file', type=str, help='path to first file')
    parser.add_argument('second_file', type=str, help='path to second file')

    # Добавляем опцию для выбора формата вывода
    parser.add_argument('-f', '--format', default='stylish', help='set format of output')

    # Парсим аргументы
    args = parser.parse_args()

    # Генерируем diff и выводим его
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
