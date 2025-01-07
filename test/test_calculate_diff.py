import pytest
from gendiff.calculate_diff import calculate_diff

def test_calculate_diff():
    data1 = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    data2 = {
        'b': 2,
        'c': 4,
        'd': 5
    }
    expected_diff = {
        'a': {'status': 'removed', 'value': 1},
        'b': {'status': 'unchanged', 'value': 2},
        'c': {'status': 'updated', 'old_value': 3, 'new_value': 4},
        'd': {'status': 'added', 'value': 5}
    }
    assert calculate_diff(data1, data2) == expected_diff
    