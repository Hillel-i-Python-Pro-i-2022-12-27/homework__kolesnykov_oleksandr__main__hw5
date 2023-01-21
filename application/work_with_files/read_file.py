def read_file(path_to_file):

    with open(path_to_file) as file:
        print(f"Читаю содержимое файла {path_to_file}...")
        return file.read()
