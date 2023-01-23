from application.logging.loggers import get_core_logger
from application.project_paths.paths import PATH_TO_FILES_INPUT


def create_new_txt_file(name="test.txt"):

    path_to_new_file = PATH_TO_FILES_INPUT.joinpath(name)
    create_logger = get_core_logger("create_logger")
    create_logger.info(f'Creating file "{name}" -> {path_to_new_file}')
    content = "Greetings ! I am a file with useless information"

    with open(path_to_new_file, "w", encoding="UTF-8") as new_file:

        new_file.writelines(content)
        print(f"Successfully ! File {name} is ready\n")


def read_file(path_to_file):

    read_logger = get_core_logger("read_logger")

    with open(path_to_file) as file:
        read_logger.info(f"Reading file {path_to_file}")
        return file.read()


def write_data_in_file(data, file):

    with open(data) as opened_file:

        read_logger = get_core_logger("read_logger")
        read_logger.info(f"Reading file {data}")

        strings = opened_file.readlines()

        with open(file, "w", encoding="UTF-8") as file_to_write:

            write_logger = get_core_logger("write_logger")
            write_logger.info(f"Writing data to file {file}")

            file_to_write.writelines(strings)

            write_logger.info("Successfully\n")
