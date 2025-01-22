import argparse

from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        dest="format",
        help="set format of output",
    )
    args = parser.parse_args()
    file1 = args.first_file
    file2 = args.second_file
    format = args.format

    diff = generate_diff(file1, file2, format)

    print(diff)


if __name__ == "__main__":
    main()
