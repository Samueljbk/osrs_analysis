from typing import List, Dict, Callable, Tuple


def get_user_data(username: str, data: dict) -> dict:
    for entry in data["users"]:
        if entry["username"] == username:
            return entry
    raise Exception("Couldn't find user")


def get_skill_data(skill: str, user_data: dict) -> dict:
    if skill in user_data["skills"]:
        return user_data["skills"][skill]


def get_skill_time_series(
    username: str, skill: str, all_data: List[dict], skill_attribute: str
):
    timestamp_list = []
    skill_attribute_value_list = []
    for data in all_data:
        user_data = get_user_data(username, data)
        skill_data = get_skill_data(skill, user_data)
        skill_attribute_value = skill_data.get(skill_attribute)
        timestamp = data.get("timestamp")
        timestamp_list.append(timestamp)
        skill_attribute_value_list.append(skill_attribute_value)
    return timestamp_list, skill_attribute_value_list
