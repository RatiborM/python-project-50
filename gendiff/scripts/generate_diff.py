from .parser import parse_file

def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    keys = sorted(data1.keys() | data2.keys())
    diff_lines = []

    for key in keys:
        if key not in data2:
            diff_lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            diff_lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff_lines.append(f"  - {key}: {data1[key]}")
            diff_lines.append(f"  + {key}: {data2[key]}")
        else:
            diff_lines.append(f"    {key}: {data1[key]}")

    return "\n".join(["{"] + diff_lines + ["}"])
