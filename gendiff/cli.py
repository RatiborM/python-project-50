import argparse


def cli_parser():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 10.0')
    parser.add_argument(
        '-f', '--format',
        metavar='[type]',
        choices=['stylish', 'plain', 'json'],
        default='stylish',
        help='output format (default: "stylish")'
    )

    return parser.parse_args()
