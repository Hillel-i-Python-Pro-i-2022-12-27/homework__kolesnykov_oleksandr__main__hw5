def write_data_in_file(data, file):

    with open(data) as opened_file:

        strings = opened_file.readlines()

        with open(file, "w") as file_to_write:

            file_to_write.writelines(strings)

    print(f"Запись всех данных из файла \n{data} \nв файл \n{file} \nпрошла успешно" + "\n")
