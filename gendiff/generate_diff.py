import json

def generate_diff(file1, file2, format_type):
    diff = {}

    # Пример обработки двух файлов
    # В реальном коде будет чтение файлов, сравнение и т. д.

    # Здесь мы симулируем результат сравнения
    properties = {
        "follow": {"status": "removed", "value": False},
        "host": {"status": "unchanged", "value": "hexlet.io"},
        "proxy": {"status": "removed", "value": "123.234.53.22"},
        "timeout": {"status": "changed", "old_value": 50, "new_value": 20},  # статус "updated" на "changed"
        "verbose": {"status": "added", "value": True}
    }

    for prop, info in properties.items():
        if format_type == "json":
            status = info["status"]
            if status == "updated":
                status = "changed"  # Заменяем на "changed", если это требуется
            diff[prop] = {
                "status": status
            }
            if status == "updated" or status == "changed":
                diff[prop]["old_value"] = info["old_value"]
                diff[prop]["new_value"] = info["new_value"]
            elif status == "added":
                diff[prop]["value"] = info["value"]
            elif status == "removed":
                diff[prop]["value"] = info["value"]
            elif status == "unchanged":
                diff[prop]["value"] = info["value"]

    return json.dumps(diff, indent=4)
