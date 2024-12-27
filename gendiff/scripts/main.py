from gendiff.cli import parse
from gendiff.diff_with_formatter import generate_diff

def main():
    args = parse()
    print(
        generate_diff(args.first_file, args.second_file, formater=args.format)
    )

if __name__ == "__main__":
    main()

