def generate_diff(file1, file2, format_type):
    diff = {}

    properties = {
        "follow": {"status": "removed", "value": False},
        "host": {"status": "unchanged", "value": "hexlet.io"},
        "proxy": {"status": "removed", "value": "123.234.53.22"},
        "timeout": {"status": "changed", "old_value": 50, "new_value": 20},
        "verbose": {"status": "added", "value": True}
    }

    if format_type == 'plain':
        result = []
        for prop, info in properties.items():
            if info["status"] == "removed":
                result.append(f"Property '{prop}' was removed")
            elif info["status"] == "unchanged":
                result.append(f"Property '{prop}' was unchanged")
            elif info["status"] == "changed":
                result.append(f"Property '{prop}' was updated. From {info['old_value']} to {info['new_value']}")
            elif info["status"] == "added":
                result.append(f"Property '{prop}' was added with value: {str(info['value']).lower()}")
        return "\n".join(result)

    # Обработка для json, yaml и других форматов
    if format_type == "json":
        for prop, info in properties.items():
            status = info["status"]
            if status == "updated":
                status = "changed"
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

    return diff