import os

def get_path(file_name: str) -> str:
    """
    Возвращает абсолютный путь к файлу.
    """
    return os.path.join(os.path.dirname(__file__), "..", "test", "fixtures", file_name)

def get_expected_result(format_type: str) -> str:
    """
    Получает ожидаемый результат для указанного формата.
    Файл должен быть в test/fixtures/ и называться expected_{format_type}.txt
    """
    file_path = get_path(f"expected_{format_type}.txt")
    with open(file_path) as f:
        return f.read()
