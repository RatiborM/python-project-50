from gendiff import generate_diff

if __name__ == "__main__":
    file1 = 'file1.json'  # Путь к первому файлу
    file2 = 'file2.json'  # Путь ко второму файлу

    diff = generate_diff(file1, file2)
    print(diff)