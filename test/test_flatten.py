from gendiff.generate_diff import flatten

def test_flatten_empty():
    data = {}
    expected = {}
    assert flatten(data) == expected

def test_flatten_single_level():
    data = {'a': 1, 'b': 2}
    expected = {'a': 1, 'b': 2}
    assert flatten(data) == expected

def test_flatten_nested():
    data = {'a': {'b': 1, 'c': {'d': 2}}}
    expected = {'a.b': 1, 'a.c.d': 2}
    assert flatten(data) == expected

def test_flatten_custom_separator():
    data = {'a': {'b': 1, 'c': {'d': 2}}}
    expected = {'a/b': 1, 'a/c/d': 2}
    assert flatten(data, sep='/') == expected
