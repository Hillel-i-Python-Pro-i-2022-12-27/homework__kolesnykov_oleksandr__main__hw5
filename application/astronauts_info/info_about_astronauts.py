from application.logging.loggers import get_core_logger
import requests


astronauts_api = "http://api.open-notify.org/astros.json"


def make_json_request():

    read_logger = get_core_logger("read_logger")
    response = requests.get(astronauts_api)

    if response.status_code == 200:
        read_logger.info(f"Reading data from {astronauts_api}")
        response = response.json()
        return response

    return f"Что-то пошло не так, код проблемы: {response.status_code}"


def get_info():

    response = make_json_request()

    if isinstance(response, dict):
        list_of_names = []
        count_of_astronauts = response["number"]
        for astronaut in response["people"]:
            list_of_names.append(astronaut["name"])

        info_string = f"В настоящий момент космонавтов: {count_of_astronauts}\n" + "\n".join(list_of_names)

        return info_string

    return response
