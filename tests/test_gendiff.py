import pytest

from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, format_name, expected_file",
    [
        (
            "tests/test_data/file1.json",
            "tests/test_data/file2.json",
            "stylish",
            "tests/expected/file1.txt",
        ),
        (
            "tests/test_data/file1.yml",
            "tests/test_data/file2.yaml",
            "stylish",
            "tests/expected/file1.txt",
        ),
        (
            "tests/test_data/file3.json",
            "tests/test_data/file4.json",
            "stylish",
            "tests/expected/file2.txt",
        ),
        (
            "tests/test_data/file3.yaml",
            "tests/test_data/file4.json",
            "stylish",
            "tests/expected/file2.txt",
        ),
        (
            "tests/test_data/empty.json",
            "tests/test_data/empty.json",
            "stylish",
            None,
        ),
        (
            "tests/test_data/empty.json",
            "tests/test_data/file4.json",
            "stylish",
            "tests/expected/file3.txt",
        ),
        (
            "tests/test_data/file3.json",
            "tests/test_data/file4.json",
            "plain",
            "tests/expected/plain1.txt",
        ),
        (
            "tests/test_data/file3.json",
            "tests/test_data/file4.json",
            "json",
            "tests/expected/json1.txt",
        ),
    ],
)
def test_generate_diff(file1, file2, format_name, expected_file):
    expected = open(expected_file).read() if expected_file else "{\n\n}"
    assert generate_diff(file1, file2, format_name) == expected


@pytest.mark.parametrize(
    "file1, file2, expected_exception, match",
    [
        (
            "tests/test_data/file1.txt",
            "tests/test_data/file2.txt",
            RuntimeError,
            "Unsupported file format",
        ),
        (
            "tests/test_data/non_existent.json",
            "tests/test_data/file2.json",
            RuntimeError,
            "File not found",
        ),
        (
            "tests/test_data/invalid.json",
            "tests/test_data/file2.json",
            RuntimeError,
            "Error decoding JSON file",
        ),
        (
            "tests/test_data/invalid.yaml",
            "tests/test_data/file2.yaml",
            RuntimeError,
            "Error decoding YAML file",
        ),
    ],
)
def test_generate_diff_exceptions(file1, file2, expected_exception, match):
    with pytest.raises(expected_exception, match=match):
        generate_diff(file1, file2)
