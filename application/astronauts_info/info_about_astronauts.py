import requests


def make_json_request():

    response = requests.get("http://api.open-notify.org/astros.json")

    if response.status_code == 200:
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
