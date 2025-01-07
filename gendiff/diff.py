def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    return {key: get_diff_entry(key, data1, data2) for key in keys}


def get_diff_entry(key, data1, data2):
    if key in data1 and key not in data2:
        return {'type': 'removed', 'value': data1[key]}
    elif key not in data1 and key in data2:
        return {'type': 'added', 'value': data2[key]}
    elif data1[key] != data2[key]:
        return {'type': 'changed', 'old_value': data1[key], 'new_value': data2[key]}
    return {'type': 'unchanged', 'value': data1.get(key)}
