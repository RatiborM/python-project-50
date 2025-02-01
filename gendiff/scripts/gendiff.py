import sys
from gendiff.parser import read_file, get_data_format, parse_data
from gendiff.generate_diff import generate_diff

def main():
    ...
    try:
        file1_data = read_file(args.first_file)
        file2_data = read_file(args.second_file)

        file1_format = get_data_format(args.first_file)
        file2_format = get_data_format(args.second_file)

        data1 = parse_data(file1_data, file1_format)
        data2 = parse_data(file2_data, file2_format)

        result = generate_diff(data1, data2, formatter)
        print(result)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)