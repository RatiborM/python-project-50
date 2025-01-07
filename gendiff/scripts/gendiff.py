import argparse


def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    # Добавляем позиционные аргументы для файлов
    parser.add_argument('first_file', type=str, help='path to first file')
    parser.add_argument('second_file', type=str, help='path to second file')

    # Парсим аргументы
    args = parser.parse_args()

    # Здесь должна быть логика вашего приложения
    print(f"Comparing {args.first_file} and {args.second_file}")


if __name__ == "__main__":
    main()
