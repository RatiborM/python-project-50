from gendiff.generate_diff import generate_diff

def test_generate_diff():
    file_path_1 = 'test/fixtures/file1.json'
    file_path_2 = 'test/fixtures/file2.json'

    # Создаем фиктивный файл file1.json
    with open(file_path_1, 'w') as file:
        file.write('{\n  "key": "value1"\n}')

    # Создаем фиктивный файл file2.json
    with open(file_path_2, 'w') as file:
        file.write('{\n  "key": "value2"\n}')

    expected = '{\n  - key: "value1"\n  + key: "value2"\n}'
    result = generate_diff(file_path_1, file_path_2, 'stylish')

    assert result == expected