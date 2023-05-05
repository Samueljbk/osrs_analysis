from typing import List, Dict, Callable, Tuple
from datetime import datetime
import models as m


def get_user_data(username: str, data: m.ScrapeData) -> m.UserData:
    for entry in data.users:
        if entry.username == username:
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
        timestamp = datetime.fromtimestamp(data.get("timestamp"))
        timestamp_list.append(timestamp)
        skill_attribute_value_list.append(skill_attribute_value)
    return timestamp_list, skill_attribute_value_list


def get_boss_data(boss: str, user_data: dict) -> dict:
    if boss in user_data["bosses"]:
        return user_data["bosses"][boss]


def get_boss_time_series(
    username: str, boss: str, all_data: List[dict], boss_attribute: str
):
    timestamp_list = []
    boss_attribute_value_list = []
    for data in all_data:
        user_data = get_user_data(username, data)
        boss_data = get_boss_data(boss, user_data)
        if boss_data is not None:
            boss_attribute_value = boss_data.get(boss_attribute)
        else:
            boss_attribute_value = 0
        timestamp = datetime.fromtimestamp(data.get("timestamp"))
        timestamp_list.append(timestamp)
        boss_attribute_value_list.append(boss_attribute_value)
    return timestamp_list, boss_attribute_value_list
