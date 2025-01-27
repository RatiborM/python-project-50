#!usr/bin/env python3

from gendiff.cli import cli_parser
from gendiff.generate_diff import generate_diff


def main():
    args = cli_parser()
    formatter = args.format
    print(generate_diff(args.first_file,
                        args.second_file,
                        formatter)
          )


if __name__ == '__main__':
    main()
