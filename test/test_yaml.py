def generate_diff(file1, file2, format_type):
    # Предыдущий код

    if format_type == "stylish":
        result = ["{"]
        for prop, info in properties.items():
            if info["status"] == "removed":
                result.append(f"  - {prop}: {str(info['value']).lower()}")
            elif info["status"] == "unchanged":
                result.append(f"    {prop}: {info['value']}")
            elif info["status"] == "changed":
                result.append(f"  - {prop}: {info['old_value']}")
                result.append(f"  + {prop}: {info['new_value']}")
            elif info["status"] == "added":
                result.append(f"  + {prop}: {str(info['value']).lower()}")
        result.append("}")
        return "\n".join(result)
