import sys
from gendiff.parser import read_file, get_data_format, parse_data
from gendiff.generate_diff import generate_diff
from gendiff.cli import cli_parser


def main():
    args = cli_parser()
    try:
        result =  generate_diff(args.first_file, args.second_file, args.format)
        print(result)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)