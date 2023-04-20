import json
import os
from transform import get_user_data


def load_data_file(filename: str) -> dict:
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def load_data(directory: str) -> list:
    return [
        load_data_file(os.path.join(directory, filename))
        for filename in os.listdir(directory)
        if filename.endswith(".json")
    ]

    # TODO: Make into list comprehension
    # for filename in os.listdir(directory):
    #    if filename.endswith('.json'):
    #        file_path = os.path.join(directory, filename)
    #        file_data = load_data_file(file_path)
    #        data.append(file_data)
    # return data


if __name__ == "__main__":
    data = load_data("data/")

    username = "shupwup"

    usernames_data = [get_user_data(username, file_data) for file_data in data]
    print(usernames_data)
