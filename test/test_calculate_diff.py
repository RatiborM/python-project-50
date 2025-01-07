import pytest
from gendiff.calculate_diff import check_value, added, deleted, changed, unchanged, nested, calculate_diff

def test_check_value():
    assert check_value(True) == 'true'
    assert check_value(False) == 'false'
    assert check_value(None) == 'null'
    assert check_value(42) == 42
    assert check_value("string") == "string"

def test_added():
    result = added('key', 'value')
    assert result == {'key': 'key', 'type': 'added', 'new_value': 'value'}

def test_deleted():
    result = deleted('key', 'value')
    assert result == {'key': 'key', 'type': 'deleted', 'old_value': 'value'}

def test_changed():
    result = changed('key', 'old_value', 'new_value')
    assert result == {'key': 'key', 'type': 'changed', 'old_value': 'old_value', 'new_value': 'new_value'}

def test_unchanged():
    result = unchanged('key', 'value')
    assert result == {'key': 'key', 'type': 'unchanged', 'value': 'value'}

def test_nested():
    result = nested('key', {'a': 1}, {'a': 1})
    expected = {
        'key': 'key',
        'type': 'nested',
        'children': [
            {'key': 'a', 'type': 'unchanged', 'value': 1}
        ]
    }
    assert result == expected

def test_calculate_diff():
    file_data1 = {
        'a': 1,
        'b': 2,
        'c': {'d': 4}
    }
    file_data2 = {
        'a': 1,
        'b': 3,
        'c': {'d': 4},
        'e': 5
    }
    expected_diff = [
        {'key': 'a', 'type': 'unchanged', 'value': 1},
        {'key': 'b', 'type': 'changed', 'old_value': 2, 'new_value': 3},
        {'key': 'c', 'type': 'nested', 'children': [
            {'key': 'd', 'type': 'unchanged', 'value': 4}
        ]},
        {'key': 'e', 'type': 'added', 'new_value': 5}
    ]
    result = calculate_diff(file_data1, file_data2)
    assert result == expected_diff
