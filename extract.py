import json
import os
from transform import get_user_data, get_skill_data


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

    usernames_data = [get_user_data(username, file_data) for file_data in data if get_user_data(
        username, file_data) is not None]
    # print(usernames_data)

    skill = 'attack'
    user_data = usernames_data[0]
    skill_data = get_skill_data(skill, user_data)
    print(skill_data)
