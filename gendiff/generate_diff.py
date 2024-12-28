from gendiff.file_parser import parse_file
from gendiff.calculate_diff import calculate_diff
from gendiff.file_formatter import stylish_format, plain_format, json_format


def generate_diff(file_path_1, file_path_2, format='stylish'):
    # Parse the files to get their contents
    data1 = parse_file(file_path_1)
    data2 = parse_file(file_path_2)

    # Calculate the difference
    diff = calculate_diff(data1, data2)

    # Format the difference in the specified format
    if format == 'stylish':
        return stylish_format(diff)
    elif format == 'plain':
        return plain_format(diff)
    elif format == 'json':
        return json_format(diff)
    else:
        raise ValueError(f"Unknown format: {format}")
