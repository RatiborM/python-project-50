import pytest
from gendiff.file_parser import parse_file

def test_parse_json_file():
    filepath = 'test/fixtures/file1.json'
    expected = {'key': 'value'}
    assert parse_file(filepath) == expected
