def get_formatter(format_type):
    if format_type == 'json':
        from gendiff.formatters.json import format_json
        return format_json
    elif format_type == 'plain':
        from gendiff.formatters.plain import format_plain
        return format_plain
    elif format_type == 'stylish':
        from gendiff.formatters.stylish import format_stylish
        return format_stylish
    else:
        raise ValueError(f"Unknown format type: {format_type}")

