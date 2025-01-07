def format_stylish(diff, depth=0):
    indent = '    ' * depth
    lines = [format_single_value(key, value, indent, depth) for key, value in diff.items()]
    return '{\n' + '\n'.join(lines) + '\n' + indent + '}'


def format_single_value(key, value, indent, depth):
    if isinstance(value, dict) and 'type' in value:
        return handle_value_type(key, value, indent, depth)
    return f"{indent}  {key}: {format_value(value)}"


def handle_value_type(key, value, indent, depth):
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
    return f"{indent}    {key}: {format_value(value['old_value'])} -> {format_value(value['new_value'])}"


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return str(value)
