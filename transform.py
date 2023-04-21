def get_user_data(username: str, data: dict) -> dict:
    for entry in data["users"]:
        if entry["username"] == username:
            return entry
    raise Exception("Couldn't find user")


def get_skill_data(skill: str, user_data: dict) -> dict:
    if skill in user_data["skills"]:
        return user_data["skills"][skill]


def get_skill_time_series(
    username: str, skill: str, all_data: list, skill_attribute: str
):
    time_stamps = []
    skill_attribute_values = []
