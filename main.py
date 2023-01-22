from application.work_with_files.actions import read_file, write_data_in_file
from application.project_paths.paths import PATH_TO_FILES_INPUT, PATH_TO_FILES_OUTPUT
from application.users_generator.users_generator import create_users_generator, get_random_users_email
from application import astronauts_info
from application.find_average.find_average import find_average_weight, find_average_height, url
from application.logging.init_logging import init_logging


def main_func():

    print(read_file(PATH_TO_FILES_INPUT) + "\n")
    write_data_in_file(PATH_TO_FILES_INPUT, PATH_TO_FILES_OUTPUT)
    generator = create_users_generator(10)  # создастся генератор 10ти случайных имён
    print(*get_random_users_email(generator), sep="\n")  # распечатается генератор 10 случайных имейлов
    print()
    print(astronauts_info.get_info())
    print()
    print(find_average_height(url))
    print(find_average_weight(url))


if __name__ == "__main__":
    init_logging()
    main_func()
