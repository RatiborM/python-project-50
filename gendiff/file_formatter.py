import json
import yaml
import itertools


ADD = '+ '
DELETE = '- '
REPLACER = ' '
SPACESCOUNT = 4


def file_formatter(value, format_):
    output = eval(f'{format_}_format')(value)
    return output


def stylish_format_item(value, depth):
    curr_indent = depth * REPLACER
    if isinstance(value, (dict, list)):
        deep_indent_size = depth + SPACESCOUNT
        deep_indent = deep_indent_size * REPLACER
        new_lines = []
        for key, val in value.items():
            new_value = stylish_format_item(val, deep_indent_size)
            new_lines.append(f'{deep_indent}{key}: {str(new_value)}')
        return '\n'.join(itertools.chain("{", new_lines, [curr_indent + "}"]))
    return f'{str(value)}'


def stylish_format(value, depth=0):
    lines = []
    current_indent = depth * REPLACER
    deep_indent_size = depth + SPACESCOUNT
    deep_indent = deep_indent_size * REPLACER
    for i in value:
        type_ = i['type']
        key_ = i['key']
        old_value = stylish_format_item(i.get('old_value'), deep_indent_size)
        new_value = stylish_format_item(i.get('new_value'), deep_indent_size)
        value_ = stylish_format_item(i.get('value'), depth)
        children_ = i.get('children')
        match type_:
            case 'unchanged':
                lines.append(f'{deep_indent}{key_}: {value_}')
            case 'changed':
                lines.append(f'{deep_indent[:-2]}{DELETE}{key_}: {old_value}')
                lines.append(f'{deep_indent[:-2]}{ADD}{key_}: {new_value}')
            case 'added':
                lines.append(f'{deep_indent[:-2]}{ADD}{key_}: {new_value}')
            case 'deleted':
                lines.append(f'{deep_indent[:-2]}{DELETE}{key_}: {old_value}')
            case 'nested':
                lines.append(f'{deep_indent}{key_}: '
                             f'{stylish_format(children_, deep_indent_size)}')
    return '\n'.join(itertools.chain("{", lines, [current_indent + "}"]))


def plain_format_item(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif value in ('true', 'false', 'null'):
        return value
    elif isinstance(value, str):
        return f"'{str(value)}'"
    else:
        return str(value)


def plain_format(value, path=''):
    lines = []
    current_path = path
    for i in value:
        type_ = i['type']
        key_ = i['key']
        old_value = plain_format_item(i.get('old_value'))
        new_value = plain_format_item(i.get('new_value'))
        children_ = i.get('children')

        if current_path != '':
            deep_path = f'{current_path}.{key_}'
        else:
            deep_path = key_

        if type_ == 'changed':
            lines.append(f"Property '{deep_path}' was updated. From {old_value} to {new_value}")
        elif type_ == 'added':
            lines.append(f"Property '{deep_path}' was added with value: {new_value}")
        elif type_ == 'deleted':
            lines.append(f"Property '{deep_path}' was removed")
        elif type_ == 'nested':
            lines.extend(plain_format(children_, deep_path).split('\n'))
    return '\n'.join(lines).strip()


def json_format(value):
    result = json.dumps(value, indent=SPACESCOUNT)
    return result


def format_to_json(data):
    """Форматирует данные в JSON."""
    return json.dumps(data, indent=2)


def format_to_yaml(data):
    """Форматирует данные в YAML."""
    return yaml.dump(data, default_flow_style=False)
