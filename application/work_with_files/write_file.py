def write_data_in_file(data, file):

    with open(data) as opened_file:

        strings = opened_file.readlines()

        with open(file, "w") as file_to_write:

            for string in strings:
                file_to_write.write(string)

    print(f"Запись всех данных из файла \n{data} \nв файл \n{file} \nпрошла успешно")
