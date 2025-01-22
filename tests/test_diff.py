import pytest
from gendiff.diff import generate_diff
from pathlib import Path

FILE1 = 'file1'
FILE2 = 'file2'
FILE1_RECURSIVE = 'file1_recursive'
FILE2_RECURSIVE = 'file2_recursive'
FORMATS = ['json', 'yaml', 'yml']
RESULT = 'expected_result.txt'
RESULT_RECURSIVE = 'expected_result_recursive.txt'

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def get_test_data_path():
    return Path('tests/test_data')

@pytest.mark.parametrize("format", FORMATS)
def test_generate_diff(format):
    expected = read_file(RESULT)
    test_data_path = get_test_data_path()

    file_path1 = str(test_data_path / f"{FILE1}.{format}")
    file_path2 = str(test_data_path / f"{FILE2}.{format}")
    actual = generate_diff(file_path1, file_path2)
    assert actual == expected

@pytest.mark.parametrize("format", FORMATS)
def test_generate_diff_recursive(format):
    expected = read_file(RESULT_RECURSIVE)
    test_data_path = get_test_data_path()

    file_path1 = str(test_data_path / f"{FILE1_RECURSIVE}.{format}")
    file_path2 = str(test_data_path / f"{FILE2_RECURSIVE}.{format}")
    actual = generate_diff(file_path1, file_path2)
    assert actual == expected
