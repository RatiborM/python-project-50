from gendiff.dicts_diff import build_diff
from gendiff.parser import parse
from gendiff.formatters import get_formatter
from gendiff.data import prepare_data


def generate_diff(path_file1: str, path_file2: str,
                  formatter: str = 'stylish') -> str:
    data1, format1 = prepare_data(path_file1)
    data2, format2 = prepare_data(path_file2)
    parsed_data1 = parse(data1, format1)
    parsed_data2 = parse(data2, format2)
    diff = build_diff(parsed_data1, parsed_data2)
    return get_formatter(formatter)(diff)
