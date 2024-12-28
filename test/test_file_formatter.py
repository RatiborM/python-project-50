import pytest
import os
from gendiff.generate_diff import generate_diff

def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)

def read(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def test_plain_format_nested_json():
    file_path_1 = get_fixture_path('nested_file_1.json')
    file_path_2 = get_fixture_path('nested_file_2.json')
    expected = read(get_fixture_path('plain_diff_nested_json.txt')).strip()
    result = generate_diff(file_path_1, file_path_2, 'plain').strip()
    assert expected == result, f"Expected:\n{expected}\nResult:\n{result}"
