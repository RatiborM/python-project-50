import pytest
from gendiff.generate_diff import generate_diff
from gendiff.parser import read_file, get_data_format, parse_data


def get_result(path_file):
    with open(path_file, "r") as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, formatter, result", [
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "json",
            "tests/fixtures/result_json.txt",
        ),
        (
            "tests/fixtures/file1.yml",
            "tests/fixtures/file2.yml",
            "json",
            "tests/fixtures/result_json.txt",
        ),
        (
            "tests/fixtures/file1.yml",
            "tests/fixtures/file2.json",
            "json",
            "tests/fixtures/result_json.txt",
        ),
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "stylish",
            "tests/fixtures/result_stylish.txt",
        ),
        (
            "tests/fixtures/file1.yml",
            "tests/fixtures/file2.yml",
            "stylish",
            "tests/fixtures/result_stylish.txt",
        ),
        (
            "tests/fixtures/file1.yml",
            "tests/fixtures/file2.json",
            "stylish",
            "tests/fixtures/result_stylish.txt",
        ),
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "plain",
            "tests/fixtures/result_plain.txt",
        ),
        (
            "tests/fixtures/file1.yml",
            "tests/fixtures/file2.yml",
            "plain",
            "tests/fixtures/result_plain.txt",
        ),
        (
            "tests/fixtures/file1.yml",
            "tests/fixtures/file2.json",
            "plain",
            "tests/fixtures/result_plain.txt",
        )
    ]
)


def test_generate_diff_formatters(file1, file2, formatter, result):
    assert generate_diff(file1, file2, formatter) == get_result(result)


def test_unsupported_file_extension():
    with pytest.raises(
            ValueError,
            match=(
                    "Unsupported file format: .some_extension "
                    "Expected '.yaml', '.yml' or '.json'."
            )
    ):
        file_data = read_file('file.some_extension')
        file_format = get_data_format('file.some_extension')
        parse_data(file_data, file_format)


def test_unsupported_file_extension():
    with pytest.raises(
            ValueError,
            match=(
                    "Неподдерживаемый формат: some_extension"
            )
    ):
        # Прямо вызываем get_data_format для неподдерживаемого расширения
        file_format = get_data_format('file.some_extension')

