import pytest
import json
from gendiff.generate_diff import generate_diff

def test_generate_diff_plain():
    file_path1 = 'test/fixtures/file1.json'
    file_path2 = 'test/fixtures/file2.json'
    expected_diff = (
        "Property 'follow' was removed\n"
        "Property 'host' was unchanged\n"
        "Property 'proxy' was removed\n"
        "Property 'timeout' was updated. From 50 to 20\n"
        "Property 'verbose' was added with value: true"
    )
    result = generate_diff(file_path1, file_path2, 'plain')
    assert result == expected_diff, f"Expected:\n{expected_diff}\nResult:\n{result}"

def test_generate_diff_json():
    file_path1 = 'test/fixtures/file1.json'
    file_path2 = 'test/fixtures/file2.json'
    expected_diff = json.dumps({
        "follow": {"type": "removed", "value": False},
        "host": {"type": "unchanged", "value": "hexlet.io"},
        "proxy": {"type": "removed", "value": "123.234.53.22"},
        "timeout": {"type": "changed", "old_value": 50, "new_value": 20},
        "verbose": {"type": "added", "value": True}
    }, indent=4)
    result = generate_diff(file_path1, file_path2, 'json')
    assert result == expected_diff, f"Expected:\n{expected_diff}\nResult:\n{result}"
