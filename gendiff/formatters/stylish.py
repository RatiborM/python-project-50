from typing import Any

DEFAULT_INDENT = 4

def to_str(value: Any, depth: int) -> str:
    indent = ' ' * depth
    if isinstance(value, dict):
        lines = ['{']
        for key, nested_value in value.items():
            lines.append(f"{indent}    {key}: {to_str(nested_value, depth + DEFAULT_INDENT)}")
        lines.append(f'{indent}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)

def line_forming(dictionary: dict, key: Any, depth: int, sign: str) -> str:
    indent = ' ' * depth
    return f'{indent}{sign} {dictionary["key"]}: {to_str(dictionary[key], depth + DEFAULT_INDENT)}'

def build_stylish_iter(diff: dict, depth=0) -> str:
    indent = ' ' * depth
    lines = ['{']
    for dictionary in diff:
        operation = dictionary['operation']
        if operation == 'same':
            lines.append(line_forming(dictionary, 'value', depth + DEFAULT_INDENT, sign='    '))
        elif operation == 'add':
            lines.append(line_forming(dictionary, 'new', depth + DEFAULT_INDENT, sign='+'))
        elif operation == 'removed':
            lines.append(line_forming(dictionary, 'old', depth + DEFAULT_INDENT, sign='-'))
        elif operation == 'changed':
            lines.append(line_forming(dictionary, 'old', depth + DEFAULT_INDENT, sign='-'))
            lines.append(line_forming(dictionary, 'new', depth + DEFAULT_INDENT, sign='+'))
        elif operation == 'nested':
            nested_value = build_stylish_iter(dictionary['value'], depth + DEFAULT_INDENT)
            lines.append(f'{indent}    {dictionary["key"]}: {nested_value}')
    lines.append(f'{indent}}}')
    return '\n'.join(lines)

def render_stylish(diff: dict) -> str:
    return build_stylish_iter(diff)