from application import astronauts_info
from application.logging.init_logging import init_logging
from application.project_paths.paths import PATH_TO_FILES_INPUT, PATH_TO_FILES_OUTPUT
from application.users_generator.users_generator import create_users_generator, get_random_users_email
from application.work_with_files.actions import read_file, write_data_in_file, create_new_txt_file
from application.find_average.find_average import get_formatted_parameters


def main_func():

    create_new_txt_file("text_data.txt")
    print(read_file(PATH_TO_FILES_INPUT.joinpath("text_data.txt")) + "\n")
    write_data_in_file(
        PATH_TO_FILES_INPUT.joinpath("text_data.txt"), PATH_TO_FILES_OUTPUT.joinpath("recorded_data.txt")
    )
    generator = create_users_generator(10)  # создастся генератор 10ти случайных имён
    print(*get_random_users_email(generator), sep="\n")  # распечатается генератор 10 случайных имейлов
    print()
    print(astronauts_info.get_info())
    print()
    print(get_formatted_parameters())


if __name__ == "__main__":
    init_logging()
    main_func()
