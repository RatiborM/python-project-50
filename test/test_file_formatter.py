import pytest
from gendiff.file_formatter import file_formatter, stylish_format_item, stylish_format, plain_format_item, plain_format, json_format

def test_file_formatter_stylish():
    data = [{'key': 'a', 'type': 'unchanged', 'value': 1}]
    result = file_formatter(data, 'stylish')
    expected = "{\n    a: 1\n}"
    assert result == expected

def test_stylish_format_item():
    data = {'a': 1, 'b': {'c': 2}}
    result = stylish_format_item(data, 0)
    expected = "{\n    a: 1\n    b: {\n        c: 2\n    }\n}"
    assert result == expected

def test_stylish_format():
    data = [
        {'key': 'a', 'type': 'unchanged', 'value': 1},
        {'key': 'b', 'type': 'changed', 'old_value': 2, 'new_value': 3},
        {'key': 'c', 'type': 'added', 'new_value': 4},
        {'key': 'd', 'type': 'deleted', 'old_value': 5},
        {'key': 'e', 'type': 'nested', 'children': [{'key': 'f', 'type': 'unchanged', 'value': 6}]}
    ]
    result = stylish_format(data)
    expected = "{\n    a: 1\n  - b: 2\n  + b: 3\n  + c: 4\n  - d: 5\n    e: {\n        f: 6\n    }\n}"
    assert result == expected

def test_plain_format_item():
    assert plain_format_item({'a': 1}) == '[complex value]'
    assert plain_format_item('true') == 'true'
    assert plain_format_item('some string') == "'some string'"
    assert plain_format_item(42) == '42'

def test_plain_format():
    data = [
        {'key': 'a', 'type': 'unchanged', 'value': 1},
        {'key': 'b', 'type': 'changed', 'old_value': 2, 'new_value': 3},
        {'key': 'c', 'type': 'added', 'new_value': 4},
        {'key': 'd', 'type': 'deleted', 'old_value': 5},
        {'key': 'e', 'type': 'nested', 'children': [{'key': 'f', 'type': 'unchanged', 'value': 6}]}
    ]
    result = plain_format(data)
    expected = ("Property 'b' was updated. From 2 to 3\n"
                "Property 'c' was added with value: 4\n"
                "Property 'd' was removed")
    assert result == expected


def test_plain_format_item():
    assert plain_format_item({'a': 1}) == '[complex value]'
    assert plain_format_item('true') == 'true'
    assert plain_format_item('some string') == "'some string'"
    assert plain_format_item(42) == '42'


def test_json_format():
    data = [{'key': 'a', 'type': 'unchanged', 'value': 1}]
    result = json_format(data)
    expected = '[\n    {\n        "key": "a",\n        "type": "unchanged",\n        "value": 1\n    }\n]'
    assert result == expected
