import pytest
from gendiff.file_formatter import format_to_json, format_to_yaml

def test_format_to_json():
    data = {'a': 1, 'b': 2}
    expected_json = '{\n  "a": 1,\n  "b": 2\n}'
    assert format_to_json(data) == expected_json

def test_format_to_yaml():
    data = {'a': 1, 'b': 2}
    expected_yaml = 'a: 1\nb: 2\n'
    assert format_to_yaml(data) == expected_yaml
    