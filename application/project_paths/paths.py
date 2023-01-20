from pathlib import Path
from typing import Final


ROOT_PATH: Final[Path] = Path(__file__).parents[2].absolute()
PATH_TO_TEXT_DATA: Final[Path] = ROOT_PATH.joinpath("text_data")
PATH_TO_FILES_OUTPUT: Final[Path] = ROOT_PATH.joinpath("files_output")
