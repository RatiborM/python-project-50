import json
import pytest
from gendiff.generate_diff import generate_diff

@pytest.fixture
def setup_files(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    return file1, file2

def test_generate_diff_identical_files(setup_files):
    file1, file2 = setup_files
    content = '{\n  "key": "value"\n}'
    file1.write_text(content)
    file2.write_text(content)

    expected = '{}'
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_empty_files(setup_files):
    file1, file2 = setup_files
    file1.write_text('{}')
    file2.write_text('{}')

    expected = '{}'
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_nested_structures(setup_files):
    file1, file2 = setup_files
    file1.write_text('{"common": {"setting1": "Value 1", "setting2": 200}}')
    file2.write_text('{"common": {"setting1": "Value 2", "setting3": 300}}')

    expected = '{\n  - common.setting1: "Value 1"\n  + common.setting1: "Value 2"\n  - common.setting2: 200\n  + common.setting3: 300\n}'
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_different_keys(setup_files):
    file1, file2 = setup_files
    file1.write_text('{"key1": "value1"}')
    file2.write_text('{"key2": "value2"}')

    expected = '{\n  - key1: "value1"\n  + key2: "value2"\n}'
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_changed_values(setup_files):
    file1, file2 = setup_files
    file1.write_text('{"key": "value1"}')
    file2.write_text('{"key": "value2"}')

    expected = '{\n  - key: "value1"\n  + key: "value2"\n}'
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_file_not_found():
    with pytest.raises(FileNotFoundError):
        generate_diff('non_existent_file1.json', 'non_existent_file2.json')

def test_generate_diff_invalid_json(tmp_path):
    invalid_json_content = 'invalid json'
    file1 = tmp_path / "invalid1.json"
    file2 = tmp_path / "invalid2.json"
    file1.write_text(invalid_json_content)
    file2.write_text(invalid_json_content)

    with pytest.raises(json.JSONDecodeError):
        generate_diff(file1, file2)