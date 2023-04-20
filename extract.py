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


if __name__ == "__main__":
    data = load_data("data/")

    username = "shupwup"

    usernames_data = [get_user_data(username, file_data) for file_data in data]
    print(usernames_data)
