import pytest
from gendiff.calculate_diff import calculate_diff

def test_calculate_diff_with_empty_dicts():
    assert calculate_diff({}, {}) == []

def test_calculate_diff_with_same_dicts():
    dict1 = {'key': 'value'}
    assert calculate_diff(dict1, dict1) == [{'key': 'key', 'type': 'unchanged', 'value': 'value'}]

def test_calculate_diff_with_different_dicts():
    dict1 = {'key1': 'value1'}
    dict2 = {'key2': 'value2'}
    expected = [
        {'key': 'key1', 'type': 'deleted', 'old_value': 'value1'},
        {'key': 'key2', 'type': 'added', 'new_value': 'value2'}
    ]
    assert calculate_diff(dict1, dict2) == expected
