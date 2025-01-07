import pytest
from gendiff.utils import flatten  # Импортируем flatten из utils

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
    flat_dict = {
        'a': 1,
        'b.c': 2,
        'b.d.e': 3
    }
    assert flatten(nested_dict) == flat_dict
