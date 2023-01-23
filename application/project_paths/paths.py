from pathlib import Path
from typing import Final


ROOT_PATH: Final[Path] = Path(__file__).parents[2]
PATH_APPLICATION: Final[Path] = ROOT_PATH.joinpath("application")
PATH_TO_FILES_INPUT: Final[Path] = ROOT_PATH.joinpath("files_input")
PATH_TO_FILES_OUTPUT: Final[Path] = ROOT_PATH.joinpath("files_output")
PATH_TO_CSV: Final[Path] = PATH_APPLICATION.joinpath("find_average").joinpath("people_data(extended).csv")
