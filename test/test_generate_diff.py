import pytest
from gendiff.generate_diff import generate_diff

def test_generate_diff_plain():
    file_path1 = 'test/fixtures/file1.json'
    file_path2 = 'test/fixtures/file2.json'
    expected_diff = (
        "Property 'follow' was removed\n"
        "Property 'host' was unchanged\n"
        "Property 'proxy' was removed\n"
        "Property 'timeout' was updated. From 50 to 20\n"
        "Property 'verbose' was added with value: true"
    )
    result = generate_diff(file_path1, file_path2, 'plain')
    assert result == expected_diff, f"Expected:\n{expected_diff}\nResult:\n{result}"
