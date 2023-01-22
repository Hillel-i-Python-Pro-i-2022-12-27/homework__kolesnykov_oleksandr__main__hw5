from application.logging.loggers import get_core_logger


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

        with open(file, "w") as file_to_write:

            write_logger = get_core_logger("write_logger")
            write_logger.info(f"Writing data to file {file}")

            file_to_write.writelines(strings)

            write_logger.info("Successfully\n")
