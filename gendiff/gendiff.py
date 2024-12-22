import json

def parse_file(file_path):
    """
    Parses a JSON file and returns its contents as a dictionary.

    :param file_path: Path to the JSON file.
    :return: Parsed data as a dictionary.
    """
    with open(file_path, 'r') as file:
        return json.load(file)