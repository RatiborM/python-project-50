import pytest
from gendiff.file_parser import parse_json, parse_yaml

def test_parse_json(tmp_path):
    data = {'a': 1, 'b': 2}
    file_path = tmp_path / 'test.json'
    file_path.write_text('{"a": 1, "b": 2}')
    assert parse_json(file_path) == data

def test_parse_yaml(tmp_path):
    data = {'a': 1, 'b': 2}
    file_path = tmp_path / 'test.yaml'
    file_path.write_text('a: 1\nb: 2\n')
    assert parse_yaml(file_path) == data
