def format_stylish(diff):
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

                    # Обработка значений None и булевых
                    if value is None:
                        value = 'null'
                    elif isinstance(value, bool):
                        value = 'false' if value is False else 'true'

                    if status == 'added':
                        lines.append(f"{indent}  + {key}: {value}")
                    elif status == 'removed':
                        lines.append(f"{indent}  - {key}: {value}")
                    elif status == 'unchanged':
                        lines.append(f"{indent}    {key}: {value}")
                    elif status == 'nested':
                        nested_diff = iter_diff(value, depth + 1)
                        lines.append(f"{indent}    {key}: {{\n{nested_diff}\n{indent}    }}")
                else:
                    lines.append(f"{indent}  {item}")
        elif isinstance(diff, dict):
            for key, (status, value) in sorted(diff.items()):
                # Обработка значений None и булевых
                if value is None:
                    value = 'null'
                elif isinstance(value, bool):
                    value = 'false' if value is False else 'true'

                if status == 'added':
                    lines.append(f"{indent}  + {key}: {value}")
                elif status == 'removed':
                    lines.append(f"{indent}  - {key}: {value}")
                elif status == 'unchanged':
                    lines.append(f"{indent}    {key}: {value}")
                elif status == 'nested':
                    nested_diff = iter_diff(value, depth + 1)
                    lines.append(f"{indent}    {key}: {{\n{nested_diff}\n{indent}    }}")

        return '\n'.join(lines)

    return f"{{\n{iter_diff(diff)}\n}}"
