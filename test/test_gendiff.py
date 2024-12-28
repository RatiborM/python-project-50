import pytest
from test.utils import get_fixture_path, read
from gendiff import generate_diff

def test_plain_format_nested_json():
    file_path_1 = get_fixture_path('nested_file_1.json')
    file_path_2 = get_fixture_path('nested_file_2.json')
    expected = read(get_fixture_path('plain_diff_nested_json.txt')).strip()
    result = generate_diff(file_path_1, file_path_2, 'plain').strip()
    assert expected == result

