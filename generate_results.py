from gendiff.diff_with_formatter import generate_diff


def generate_expected_results():
    # Передайте пути к файлам
    file1_path = 'file1.json'
    file2_path = 'file2.json'

    stylish_result = generate_diff(file1_path, file2_path, formater='stylish')

    # Сохранение результата
    with open('test/correct_result.txt', 'w') as file:
        file.write(stylish_result)
