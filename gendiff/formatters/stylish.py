def format_stylish(diff):
    """
    Formats the diff into a stylish format.
    """
    def iter_diff(diff, depth=0):
        lines = []
        indent = '    ' * depth

        # Если diff - это список
        if isinstance(diff, list):
            for item in diff:
                if isinstance(item, dict):
                    key = item.get('key')
                    status = item.get('operation')
                    value = item.get('value', None)
                    if status == 'added':
                        lines.append(f"{indent}  + {key}: {value}")
                    elif status == 'removed':
                        lines.append(f"{indent}  - {key}: {value}")
                    elif status == 'unchanged':
                        lines.append(f"{indent}    {key}: {value}")
                    elif status == 'nested':
                        nested_diff = iter_diff(item.get('value'), depth + 1)
                        lines.append(f"{indent}    {key}: {{\n{nested_diff}\n{indent}    }}")
                else:
                    lines.append(f"{indent}  {item}")
        elif isinstance(diff, dict):
            # Если diff - это словарь
            for key, value in sorted(diff.items()):
                if isinstance(value, dict) or isinstance(value, list):
                    nested_diff = iter_diff(value, depth + 1)
                    lines.append(f"{indent}    {key}: {{\n{nested_diff}\n{indent}    }}")
                else:
                    lines.append(f"{indent}    {key}: {value}")

        return '\n'.join(lines)

    return f"{{\n{iter_diff(diff)}\n}}"
