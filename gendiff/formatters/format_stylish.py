def format_stylish(diff):
    return '{\n' + tree(diff) + '\n}'


def tree(diff, depth=1):
    lines = []
    indent = ' ' * (4 * depth - 2)

    for key, (type, value) in sorted(diff.items()):
        if type == 'nested':
            nested_view = tree(value, depth + 1)
            lines.append(f"{indent}  {key}: {{\n{nested_view}\n{indent}  }}")
        elif type == 'changed':
            old, new = value
            lines.append(format_line(key, old, depth, '- '))
            lines.append(format_line(key, new, depth, '+ '))
        else:
            prefix = {'added': '+ ', 'removed': '- ', 'unchanged': '  '}[type]
            lines.append(format_line(key, value, depth, prefix))

    return '\n'.join(lines)


def format_line(key, value, depth, prefix):
    indent = ' ' * (4 * depth - 2)
    formatted_value = format_value(value, depth + 1)
    return f"{indent}{prefix}{key}: {formatted_value}"


def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        indent = ' ' * (4 * depth - 4)
        child_indent = ' ' * (4 * depth)
        for key, val in value.items():
            formatted_val = format_value(val, depth + 1)
            lines.append(f"{child_indent}{key}: {formatted_val}")
        return f"{{\n{'\n'.join(lines)}\n{indent}}}"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
