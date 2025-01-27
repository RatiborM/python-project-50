def gen_stylish_format(diff, sep=' ', sep_count=4, depth=0):
    initial_depth = depth
    depth += sep_count
    result_string = '{\n'

    for value in diff:
        key = value['key']
        status = value.get('status')

        if status == 'nested':
            formatted_value = gen_stylish_format(
                value["value"], sep, sep_count, depth
            )
            result_string += (
                f'{depth * sep}{key}:'
                f' {formatted_value}\n'
            )

        elif status == 'added':
            result_string += (
                f'{(depth - 2) * sep}+ {key}:'
                f' {to_str(value["value"], depth, sep_count, sep)}\n'
            )

        elif status == 'deleted':
            result_string += (
                f'{(depth - 2) * sep}- {key}:'
                f' {to_str(value["value"], depth, sep_count, sep)}\n'
            )

        elif status == 'changed':
            result_string += (
                f'{(depth - 2) * sep}- {key}:'
                f' {to_str(value["old_value"], depth, sep_count, sep)}\n'
            )
            result_string += (
                f'{(depth - 2) * sep}+ {key}:'
                f' {to_str(value["new_value"], depth, sep_count, sep)}\n'
            )

        elif status == 'unchanged':
            result_string += (
                f'{depth * sep}{key}:'
                f' {to_str(value["value"], depth, sep_count, sep)}\n'
            )

    result_string += f'{initial_depth * sep}}}'
    return result_string


def dict_to_str(data, depth, sep_count, sep):
    depth += sep_count
    result_string = ''

    for key, value in data.items():
        if isinstance(value, dict):
            result_string += (
                f'{depth * sep}'
                f'{key}: {dict_to_str(value, depth, sep_count, sep)}\n'
            )
        else:
            result_string += (f'{depth * sep}'
                              f'{key}: {value}\n')

    result = '{\n' + result_string + (sep * (depth - sep_count)) + '}\n'
    return result.strip('\n')


def to_str(value, depth, sep_count, sep):
    if isinstance(value, dict):
        return dict_to_str(value, depth, sep_count, sep)
    elif value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value
