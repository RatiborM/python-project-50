import pytest
from tests.utils import get_fixture_path, read  # Абсолютный путь
from gendiff import generate_diff

def test_plain_json():
    file_path_1 = get_fixture_path('plain_file_1.json')
    file_path_2 = get_fixture_path('plain_file_2.json')
    expected = read(get_fixture_path('plain_diff_json.txt'))
    result = generate_diff(file_path_1, file_path_2, 'stylish')
    assert expected == result

def test_plain_yaml():
    file_path_1 = get_fixture_path('plain_file_1.yml')
    file_path_2 = get_fixture_path('plain_file_2.yml')
    expected = read(get_fixture_path('plain_diff_json.txt'))
    result = generate_diff(file_path_1, file_path_2, 'stylish')
    assert expected == result

def test_nested_json():
    file_path_1 = get_fixture_path('nested_file_1.json')
    file_path_2 = get_fixture_path('nested_file_2.json')
    expected = read(get_fixture_path('nested_diff_json.txt'))
    result = generate_diff(file_path_1, file_path_2, 'stylish')
    assert expected == result

def test_plain_format_nested_json():
    file_path_1 = get_fixture_path('nested_file_1.json')
    file_path_2 = get_fixture_path('nested_file_2.json')
    expected = read(get_fixture_path('plain_diff_nested_json.txt'))
    result = generate_diff(file_path_1, file_path_2, 'plain')
    assert expected == result
