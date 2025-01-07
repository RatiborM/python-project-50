def check_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def added(key, value):
    return {
        'key': key,
        'type': 'added',
        'new_value': value
    }


def deleted(key, value):
    return {
        'key': key,
        'type': 'deleted',
        'old_value': value
    }


def changed(key, old_value, new_value):
    return {
        'key': key,
        'type': 'changed',
        'old_value': old_value,
        'new_value': new_value
    }


def unchanged(key, value):
    return {
        'key': key,
        'type': 'unchanged',
        'value': value
    }


def nested(key, value_1, value_2):
    return {
        'key': key,
        'type': 'nested',
        'children': calculate_diff(value_1, value_2)
    }


def calculate_diff(file_data1, file_data2):
    all_keys = file_data1.keys() | file_data2.keys()
    added_keys = file_data2.keys() - file_data1.keys()
    deleted_keys = file_data1.keys() - file_data2.keys()

    return [get_diff_entry(key, file_data1, file_data2, added_keys, deleted_keys) for key in all_keys]


def get_diff_entry(key, file_data1, file_data2, added_keys, deleted_keys):
    if key in added_keys:
        return {'key': key, 'type': 'added', 'value': file_data2[key]}
    elif key in deleted_keys:
        return {'key': key, 'type': 'removed', 'value': file_data1[key]}
    elif file_data1[key] != file_data2[key]:
        return {'key': key, 'type': 'changed', 'old_value': file_data1[key], 'new_value': file_data2[key]}
    return {'key': key, 'type': 'unchanged', 'value': file_data1[key]}
