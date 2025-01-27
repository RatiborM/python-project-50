from gendiff.formatters.json import gen_json_format
from gendiff.formatters.stylish import gen_stylish_format
from gendiff.formatters.plain import gen_plain_format


def get_format(formatter):
    if formatter == "json":
        return gen_json_format
    elif formatter == "stylish":
        return gen_stylish_format
    elif formatter == "plain":
        return gen_plain_format
    else:
        raise ValueError(f"Unsupported format: {formatter}. "
                         "Expected 'json', 'stylish', or 'plain'")
