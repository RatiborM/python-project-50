def format_plain(diff, parent=''):
    lines = []
    for key, value in sorted(diff.items()):
        name = f"{parent}.{key}" if parent else key
        if isinstance(value, dict) and 'type' in value:
            value_type = value['type']
            if value_type == 'added':
                val = format_value(value['value'])
                lines.append(f"Property '{name}' was added with value: {val}")
            elif value_type == 'removed':
                lines.append(f"Property '{name}' was removed")
            elif value_type == 'changed':
                old_val = format_value(value['old_value'])
                new_val = format_value(value['new_value'])
                lines.append(f"Property '{name}' was updated. From {old_val} to {new_val}")
            elif value_type == 'nested':
                lines.extend(format_plain(value['children'], name))
            elif value_type == 'unchanged':
                lines.append(f"Property '{name}' was unchanged")
        elif isinstance(value, dict):
            lines.extend(format_plain(value, name))
    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value
