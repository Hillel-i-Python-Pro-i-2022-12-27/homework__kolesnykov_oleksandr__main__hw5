from application.logging.loggers import get_core_logger
import requests


url = "https://drive.google.com/uc?export=download&id=1yM0a4CSf0iuAGOGEljdb7qcWyz82RBxl"


def find_average_height(page):

    read_logger = get_core_logger("read_logger")
    response = requests.get(page)

    if response.status_code == 200:
        read_logger.info(f"Reading data from {url}")
        text = response.text
        text = text.split("\n")[1:]
        height_list = [float(height.split(", ")[1]) for height in text if height]

        return f"""Всего данных: {len(height_list)}
средний рост в см: {round((sum(height_list) / len(height_list)) * 2.54, 2)}
        """

    return f"Что-то пошло не так, код ошибки: {page.status_code}"


def find_average_weight(page):

    read_logger = get_core_logger("read_logger")
    response = requests.get(page)

    if response.status_code == 200:
        read_logger.info(f"Reading data from {url}")
        text = response.text
        text = text.split("\n")[1:]
        weight_list = [float(weight.split(", ")[2]) for weight in text if weight]

        return f"""Всего данных: {len(weight_list)}
средний вес в кг: {round((sum(weight_list) / len(weight_list)) * 0.453592, 2)}
        """

    return f"Что-то пошло не так, код ошибки: {page.status_code}"
