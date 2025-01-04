import pytest
from gendiff.generate_diff import flatten

def test_flatten():
    nested_dict = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3
            }
        }
    }
    expected_flat_dict = {
        'a': 1,
        'b.c': 2,
        'b.d.e': 3
    }
    assert flatten(nested_dict) == expected_flat_dict
