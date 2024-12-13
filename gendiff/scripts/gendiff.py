import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="Path to the first file")
    parser.add_argument("second_file", help="Path to the second file")
    parser.add_argument(
        "-f", "--format",
        help="Set format of output",
        dest="format",
        default="plain"  # Установите "plain" как формат по умолчанию
    )
    args = parser.parse_args()
    print(f"Comparing {args.first_file} and {args.second_file}")
    print(f"Output format: {args.format}")

if __name__ == "__main__":
    main()