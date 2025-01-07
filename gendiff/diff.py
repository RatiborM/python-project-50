def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}
    for key in keys:
        if key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        elif key not in data1:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif data1[key] == data2[key]:
            diff[key] = {'status': 'unchanged', 'value': data1[key]}
        else:
            diff[key] = {'status': 'updated', 'old_value': data1[key], 'new_value': data2[key]}
    return diff


def build_diff_entry(data1, data2, key):
    if key not in data1:
        return {'type': 'added', 'value': data2[key]}
    if key not in data2:
        return {'type': 'removed', 'value': data1[key]}
    if isinstance(data1[key], dict) and isinstance(data2[key], dict):
        return {'type': 'nested', 'children': build_diff(data1[key], data2[key])}
    if data1[key] != data2[key]:
        return {'type': 'changed', 'old_value': data1[key], 'new_value': data2[key]}
    return {'type': 'unchanged', 'value': data1[key]}
