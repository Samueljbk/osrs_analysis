def get_user_data(username, data):
    for entry in data['users']:
        if entry['username'] == username:
            return entry
    raise Exception('Couldn\'t find user')


# def get_skill_data(skill, data):
