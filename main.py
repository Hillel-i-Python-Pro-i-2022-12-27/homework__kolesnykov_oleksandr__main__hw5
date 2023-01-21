from application import work_with_files
from application import project_paths
from application import users_generator


if __name__ == "__main__":

    print(work_with_files.read_file(project_paths.PATH_TO_TEXT_DATA) + "\n")
    work_with_files.write_data_in_file(project_paths.PATH_TO_TEXT_DATA, project_paths.PATH_TO_FILES_OUTPUT)
    generator = users_generator.create_users_generator(10)  # создастся генератор 10ти случайных имён
    # generator = users_generator.create_users_generator()  # создастся генератор 100 случайных имён
    print(*users_generator.get_random_users_email(generator), sep="\n")  # распечатается генератор 10 случайных имён
    # print(*users_generator.get_random_users_email(generator), sep='\n') # распечатается генератор 100 случайных имён
