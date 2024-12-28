import json


def flatten(data, parent_key='', sep='.'):
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def generate_diff(file1, file2, format='stylish'):
    with open(file1, 'r') as f1:
        data1 = json.load(f1)

    with open(file2, 'r') as f2:
        data2 = json.load(f2)

    flat_data1 = flatten(data1)
    flat_data2 = flatten(data2)

    diff = []

    all_keys = set(flat_data1.keys()).union(flat_data2.keys())

    for key in all_keys:
        if key not in flat_data1:
            diff.append(f"  + {key}: {json.dumps(flat_data2[key])}")
        elif key not in flat_data2:
            diff.append(f"  - {key}: {json.dumps(flat_data1[key])}")
        elif flat_data1[key] != flat_data2[key]:
            diff.append(f"  - {key}: {json.dumps(flat_data1[key])}")
            diff.append(f"  + {key}: {json.dumps(flat_data2[key])}")

    return '{\n' + '\n'.join(diff) + '\n}'
