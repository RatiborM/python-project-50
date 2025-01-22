def format_plain(diff):
    return '\n'.join(formatter(diff))


def formatter(diff, path=""):
    lines = []

    for key, (status, value) in diff.items():
        full_key = f"{path}.{key}" if path else key

        if status == "nested":
            lines.extend(formatter(value, full_key))
        elif status == "added":
            lines.append(f"Property '{full_key}' was added with value: \
{format_value(value)}")
        elif status == "removed":
            lines.append(f"Property '{full_key}' was removed")
        elif status == "changed":
            old, new = map(format_value, value)
            lines.append(
                f"Property '{full_key}' was updated. From {old} to {new}")

    return lines


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    return str(value).lower()
