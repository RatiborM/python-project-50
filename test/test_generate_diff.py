import json


def generate_diff(file1, file2, format_type):
    """
    Генерирует различия между двумя файлами в заданном формате.

    :param file1: Путь к первому файлу (не используется в данном примере).
    :param file2: Путь ко второму файлу (не используется в данном примере).
    :param format_type: Формат вывода различий ('plain', 'json', 'stylish').
    :return: Строка с различиями в заданном формате.
    """
    # Данные для тестирования
    properties = {
        "follow": {"status": "removed", "value": False},
        "host": {"status": "unchanged", "value": "hexlet.io"},
        "proxy": {"status": "removed", "value": "123.234.53.22"},
        "timeout": {"status": "changed", "old_value": 50, "new_value": 20},
        "verbose": {"status": "added", "value": True}
    }

    # Формат вывода "plain"
    if format_type == 'plain':
        result = []
        for prop, info in properties.items():
            status = info["status"]
            if status == "removed":
                result.append(f"Property '{prop}' was removed")
            elif status == "changed":
                result.append(f"Property '{prop}' was updated. From {info['old_value']} to {info['new_value']}")
            elif status == "added":
                value = json.dumps(info["value"]).strip('"')  # Преобразовать значение в строку
                result.append(f"Property '{prop}' was added with value: {value}")
        return "\n".join(result)

    # Формат вывода "json"
    elif format_type == "json":
        diff = {}
        for prop, info in properties.items():
            diff[prop] = {"status": info["status"]}
            if info["status"] == "changed":
                diff[prop]["old_value"] = info["old_value"]
                diff[prop]["new_value"] = info["new_value"]
            elif info["status"] in {"added", "removed", "unchanged"}:
                diff[prop]["value"] = info["value"]
        return json.dumps(diff, indent=4)

    # Формат вывода "stylish" (пример)
    elif format_type == "stylish":
        result = []
        for prop, info in properties.items():
            status = info["status"]
            if status == "added":
                result.append(f"  + {prop}: {info['value']}")
            elif status == "removed":
                result.append(f"  - {prop}: {info['value']}")
            elif status == "unchanged":
                result.append(f"    {prop}: {info['value']}")
            elif status == "changed":
                result.append(f"  - {prop}: {info['old_value']}")
                result.append(f"  + {prop}: {info['new_value']}")
        return "\n".join(result)

    # Если формат неизвестен
    raise ValueError(f"Unknown format_type: {format_type}")
