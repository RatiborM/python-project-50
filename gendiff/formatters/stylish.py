def format_stylish(diff, depth=0):
    indent = '    ' * depth
    lines = []

    for key, value in diff.items():
        if value['type'] == 'nested':
            lines.append(f"{indent}    {key}: {format_stylish(value['children'], depth + 1)}")
        elif value['type'] == 'added':
            lines.append(f"{indent}  + {key}: {value['value']}")
        elif value['type'] == 'removed':
            lines.append(f"{indent}  - {key}: {value['value']}")
        elif value['type'] == 'changed':
            lines.append(f"{indent}  - {key}: {value['old_value']}")
            lines.append(f"{indent}  + {key}: {value['new_value']}")
        else:
            lines.append(f"{indent}    {key}: {value['value']}")

    return "{\n" + "\n".join(lines) + "\n" + indent + "}"
