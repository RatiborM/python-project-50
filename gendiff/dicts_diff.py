def build_diff(parced_data1: dict, parced_data2: dict):
    diff = []
    sorted_keys = sorted(list(set(parced_data1.keys()) | set(parced_data2.keys())))

    for key in sorted_keys:
        if key not in parced_data1:
            diff.append({
                'key': key,
                'operation': 'add',
                'new': parced_data2[key] if parced_data2[key] is not None else 'null'
            })
        elif key not in parced_data2:
            diff.append({
                'key': key,
                'operation': 'removed',
                'old': parced_data1[key] if parced_data1[key] is not None else 'null'
            })
        elif isinstance(parced_data1[key], dict) and isinstance(parced_data2[key], dict):
            child = build_diff(parced_data1[key], parced_data2[key])
            diff.append({
                'key': key,
                'operation': 'nested',
                'value': child
            })
        elif parced_data1[key] == parced_data2[key]:
            diff.append({
                'key': key,
                'operation': 'same',
                'value': parced_data1[key]
            })
        else:
            diff.append({
                'key': key,
                'operation': 'changed',
                'old': parced_data1[key] if parced_data1[key] is not None else 'null',
                'new': parced_data2[key] if parced_data2[key] is not None else 'null'
            })

    return diff
