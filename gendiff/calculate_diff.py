def calculate_diff(data1, data2):
    diff = {}
    for key in data1.keys() | data2.keys():
        if key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        elif key not in data1:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif data1[key] != data2[key]:
            diff[key] = {'status': 'updated', 'old_value': data1[key], 'new_value': data2[key]}
        else:
            diff[key] = {'status': 'unchanged', 'value': data1[key]}
    return diff


def calculate_diff_entry(file_data1, file_data2, key):
    if key in file_data1 and key not in file_data2:
        return {'type': 'removed', 'key': key, 'value': file_data1[key]}
    if key in file_data2 and key not in file_data1:
        return {'type': 'added', 'key': key, 'value': file_data2[key]}
    if file_data1[key] != file_data2[key]:
        return {'type': 'changed', 'key': key, 'old_value': file_data1[key], 'new_value': file_data2[key]}
    return {'type': 'unchanged', 'key': key, 'value': file_data1[key]}
