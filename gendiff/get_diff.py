def get_diff(file1, file2):
    all_keys = sorted(set(file1.keys()).union(set(file2.keys())))
    result = []

    for key in all_keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            result.append({
                'key': key,
                'value': get_diff(value1, value2),
                'status': 'nested'
            })

        else:
            if key not in file1:
                result.append({
                    'key': key,
                    'value': value2,
                    'status': 'added'
                })

            elif key not in file2:
                result.append({
                    'key': key,
                    'value': value1,
                    'status': 'deleted'
                })

            elif value1 != value2:
                result.append({
                    'key': key,
                    'old_value': value1,
                    'new_value': value2,
                    'status': 'changed'
                })
            else:
                result.append({
                    'key': key,
                    'value': value1,
                    'status': 'unchanged'
                })

    return result
