from gendiff import parse_file

if __name__ == "__main__":
    file1_data = parse_file('file1.json')
    file2_data = parse_file('file2.json')

    print("File 1 data:", file1_data)
    print("File 2 data:", file2_data)