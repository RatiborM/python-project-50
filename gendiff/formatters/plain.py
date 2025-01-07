def format_plain(diff, parent=''):
    lines = []
    for key, value in sorted(diff.items()):
        name = f"{parent}.{key}" if parent else key
        if isinstance(value, dict) and 'type' in value:
            line = handle_value_type(name, value)
            if line is not None:
                lines.append(line)
    return '\n'.join(lines)


def handle_value_type(name, value):
    value_type = value['type']
    if value_type == 'added':
        return f"Property '{name}' was added with value: {format_value(value['value'])}"
    elif value_type == 'removed':
        return f"Property '{name}' was removed"
    elif value_type == 'changed':
        return f"Property '{name}' was updated. From {format_value(value['old_value'])} to {format_value(value['new_value'])}"
    elif value_type == 'unchanged':
        return f"Property '{name}' was unchanged"
    elif value_type == 'nested':
        return format_plain(value['children'], name)
    return None


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return value
