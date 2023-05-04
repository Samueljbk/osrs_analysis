import json
import os
from transform import get_user_data, get_skill_data, get_skill_time_series
from models import ScrapeData
from typing import List


def load_data_file(filename: str) -> ScrapeData:
    return ScrapeData.parse_file(filename)


def load_data(directory: str) -> List[ScrapeData]:
    return [
        load_data_file(os.path.join(directory, filename))
        for filename in os.listdir(directory)
        if filename.endswith(".json")
    ]


if __name__ == "__main__":
    all_data = load_data("data/")

    username = "shupwup"

    usernames_data = [get_user_data(username, file_data) for file_data in all_data]
    # print(usernames_data)

    skill = "defense"
    time_series = get_skill_time_series(username, skill, all_data, "experience")
    time_stamps, skill_values = time_series
    print(list(zip(time_stamps, skill_values)))
    # user_data = usernames_data[0]
    # skill_data = get_skill_data(skill, user_data)
    # print(skill_data)
