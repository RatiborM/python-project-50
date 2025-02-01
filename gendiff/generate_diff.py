from gendiff.get_diff import get_diff
from gendiff.parser import read_file, get_data_format, parse_data
from gendiff.formatters import get_format


def generate_diff(file1_path, file2_path, format_name='stylish'):
    file1_data = read_file(file1_path)
    file2_data = read_file(file2_path)

    file1_format = get_data_format(file1_path)
    file2_format = get_data_format(file2_path)

    data1 = parse_data(file1_data, file1_format)
    data2 = parse_data(file2_data, file2_format)

    formatter = get_format(format_name)
    return formatter(get_diff(data1, data2))
