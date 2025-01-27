from gendiff.get_diff import get_diff
from gendiff.load_files import load_files
from gendiff.formatters import get_format


def generate_diff(file1_pass, file2_pass, formatter='stylish'):
    file1, file2 = load_files(file1_pass), load_files(file2_pass)
    formatter = get_format(formatter)
    return formatter(get_diff(file1, file2))
