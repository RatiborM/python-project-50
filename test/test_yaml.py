import pytest
from gendiff import generate_diff

def test_generate_diff_yaml():
    file1_path = 'test/fixtures/file1.yaml'
    file2_path = 'test/fixtures/file2.yaml'
    expected_output = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(file1_path, file2_path) == expected_output
