import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file', help='First file')
    parser.add_argument('second_file', help='Second file')
    args = parser.parse_args()

    # Здесь будет логика сравнения файлов
    print(f"Comparing {args.first_file} and {args.second_file}")

if __name__ == '__main__':
    main()