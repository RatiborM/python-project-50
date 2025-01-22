from gendiff import generate_diff


def test_gennerate_diff():
    comparison = 'tests/test_data/tests.txt'
    file1 = 'tests/test_data/file1.json'
    file2 = 'tests/test_data/file2.json'

    with open(comparison,'r') as txt:
        text = ''.join(txt.readlines())

    gd_text = generate_diff.generate_diff(file1, file2)

    assert gd_text == text
