# Вставьте пустую строку перед функцией calculate_diff_entry
def calculate_diff(file_data1, file_data2):
    all_keys = file_data1.keys() | file_data2.keys()
    diff_list = [calculate_diff_entry(file_data1, file_data2, key) for key in all_keys]
    return diff_list


def calculate_diff_entry(file_data1, file_data2, key):
    if key in file_data1 and key not in file_data2:
        return {'type': 'removed', 'key': key, 'value': file_data1[key]}
    if key in file_data2 and key not in file_data1:
        return {'type': 'added', 'key': key, 'value': file_data2[key]}
    if file_data1[key] != file_data2[key]:
        return {'type': 'changed', 'key': key, 'old_value': file_data1[key], 'new_value': file_data2[key]}
    return {'type': 'unchanged', 'key': key, 'value': file_data1[key]}
