from application import work_with_files
from application import project_paths


def print_content():
    content = work_with_files.read_file(project_paths.PATH_TO_TEXT_DATA)
    return content


def write_content():
    work_with_files.write_data_in_file(project_paths.PATH_TO_TEXT_DATA, project_paths.PATH_TO_FILES_OUTPUT)


if __name__ == "__main__":

    print(print_content())
    print()
    write_content()
