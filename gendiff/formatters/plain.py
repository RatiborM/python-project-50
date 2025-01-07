import json


def format_plain(diff):
    lines = []
    for key, value in diff.items():
        status = value['status']
        if status == 'removed':
            lines.append(f"Property '{key}' was removed")
        elif status == 'added':
            value_repr = json.dumps(value['value'])
            lines.append(f"Property '{key}' was added with value: {value_repr}")
        elif status == 'unchanged':
            lines.append(f"Property '{key}' was unchanged")
        elif status == 'updated':
            old_value_repr = json.dumps(value['old_value'])
            new_value_repr = json.dumps(value['new_value'])
            lines.append(f"Property '{key}' was updated. From {old_value_repr} to {new_value_repr}")
    return '\n'.join(lines)


def format_plain_value(name, value):
    if isinstance(value, dict) and 'type' in value:
        return handle_plain_type(name, value)
    return None


def handle_plain_type(name, value):
    value_type = value['type']
    if value_type == 'added':
        return f"Property '{name}' was added with value: {format_value(value['value'])}"
    elif value_type == 'removed':
        return f"Property '{name}' was removed"
    elif value_type == 'unchanged':
        return None
    elif value_type == 'nested':
        return format_plain(value['children'], name)
    elif value_type == 'changed':
        return f"Property '{name}' was updated. From {format_value(value['old_value'])} to {format_value(value['new_value'])}"


def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
