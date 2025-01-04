import pytest
import json
from gendiff.generate_diff import generate_diff

@pytest.fixture
def setup_files(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    return file1, file2

def test_generate_diff():
    file_path1 = 'test/fixtures/file1.json'
    file_path2 = 'test/fixtures/file2.json'
    with open('test/fixtures/expected_diff.txt') as f:
        expected_diff = f.read().strip()
    assert generate_diff(file_path1, file_path2) == expected_diff

def test_generate_diff_identical_files(setup_files):
    file1, file2 = setup_files
    content = '{\n  "key": "value"\n}'
    file1.write_text(content)
    file2.write_text(content)
    expected = '{\n    key: value\n}'
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_empty_files(setup_files):
    file1, file2 = setup_files
    file1.write_text('{}')
    file2.write_text('{}')
    expected = '{\n\n}'
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_nested_structures(setup_files):
    file1, file2 = setup_files
    file1.write_text('{"common": {"setting1": "Value 1", "setting2": 200}}')
    file2.write_text('{"common": {"setting1": "Value 2", "setting3": 300}}')
    expected = '''{
    common: {
      - setting1: Value 1
      + setting1: Value 2
      - setting2: 200
      + setting3: 300
    }
}'''
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_different_keys(setup_files):
    file1, file2 = setup_files
    file1.write_text('{"key1": "value1"}')
    file2.write_text('{"key2": "value2"}')
    expected = '''{
  - key1: value1
  + key2: value2
}'''
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_changed_values(setup_files):
    file1, file2 = setup_files
    file1.write_text('{"key": "value1"}')
    file2.write_text('{"key": "value2"}')
    expected = '''{
  - key: value1
  + key: value2
}'''
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected:\n{expected}\nResult:\n{result}"

def test_generate_diff_invalid_json(tmp_path):
    invalid_json_content = 'invalid json'
    file1 = tmp_path / "invalid1.json"
    file2 = tmp_path / "invalid2.json"
    file1.write_text(invalid_json_content)
    file2.write_text(invalid_json_content)
    with pytest.raises(json.JSONDecodeError):
        generate_diff(file1, file2)
