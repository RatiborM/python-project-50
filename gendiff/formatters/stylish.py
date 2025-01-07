def format_stylish(diff):
    lines = []
    for key, value in diff.items():
        status = value['status']
        if status == 'removed':
            lines.append(f"  - {key}: {value['value']}")
        elif status == 'added':
            lines.append(f"  + {key}: {value['value']}")
        elif status == 'unchanged':
            lines.append(f"    {key}: {value['value']}")
        elif status == 'updated':
            lines.append(f"  - {key}: {value['old_value']}")
            lines.append(f"  + {key}: {value['new_value']}")
    return "{\n" + '\n'.join(lines) + "\n}"


def format_stylish_value(key, value, indent, depth):
    if isinstance(value, dict) and 'type' in value:
        return handle_stylish_type(key, value, indent, depth)
    return f"{indent}  {key}: {format_value(value)}"


def handle_stylish_type(key, value, indent, depth):
    value_type = value['type']
    if value_type == 'added':
        return f"{indent}  + {key}: {format_value(value['value'])}"
    elif value_type == 'removed':
        return f"{indent}  - {key}: {format_value(value['value'])}"
    elif value_type == 'unchanged':
        return f"{indent}    {key}: {format_value(value['value'])}"
    elif value_type == 'nested':
        return f"{indent}  {key}: {format_stylish(value['children'], depth + 1)}"
    elif value_type == 'changed':
        return f"{indent}  - {key}: {format_value(value['old_value'])}\n{indent}  + {key}: {format_value(value['new_value'])}"


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return str(value)
