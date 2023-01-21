from application import work_with_files
from application import project_paths
from application import users_generator
from application import astronauts_info
from application import find_average


if __name__ == "__main__":

    print(work_with_files.read_file(project_paths.PATH_TO_FILES_INPUT) + "\n")
    work_with_files.write_data_in_file(project_paths.PATH_TO_FILES_INPUT, project_paths.PATH_TO_FILES_OUTPUT)
    generator = users_generator.create_users_generator(10)  # создастся генератор 10ти случайных имён
    print(*users_generator.get_random_users_email(generator), sep="\n")  # распечатается генератор 10 случайных имейлов
    print()
    print(astronauts_info.get_info())
    print()
    print(find_average.find_average_height(find_average.url))
    print(find_average.find_average_weight(find_average.url))
