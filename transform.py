def get_user_data(username: str, data: dict) -> dict:
    for entry in data['users']:
        if entry['username'] == username:
            return entry
    raise Exception('Couldn\'t find user')


def get_skill_data(skill: str, data: dict) -> dict:
    if skill in data['skills']:
        return data['skills'][skill]
