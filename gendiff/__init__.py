from gendiff.diff_with_formatter import generate_diff as generate_diff_with_formatter


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Wrapper function for generating diff with formatter.
    """
    return generate_diff_with_formatter(file_path1, file_path2, format_name)