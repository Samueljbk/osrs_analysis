# "attack": {
#                     "rank": 280980,
#                     "level": 99,
#                     "experience": 13040695,
#                     "next_level_exp": 14391160,
#                     "exp_to_next_level": 1350465


class SkillData:
    def __init__(
        self,
        skill_name: str,
        experience: int,
        rank: int,
        next_level_exp: int,
        exp_to_next_level: int,
    ):
        self.skill_name = skill_name
        self.experience = experience
        self.rank = rank
        self.next_level_exp = next_level_exp
        self.exp_to_next_level = exp_to_next_level

    def __repr__(self):
        return str(
            [
                self.skill_name,
                self.experience,
                self.rank,
                self.next_level_exp,
                self.exp_to_next_level,
            ]
        )


def get_user_data(username: str, data: dict) -> dict:
    for entry in data["users"]:
        if entry["username"] == username:
            return entry
    raise Exception("Couldn't find user")


def get_skill_data(skill: str, user_data: dict) -> SkillData:
    if skill in user_data["skills"]:
        a = SkillData(
            skill,
            user_data["skills"][skill]["experience"],
            user_data["skills"][skill]["rank"],
            user_data["skills"][skill]["next_level_exp"],
            user_data["skills"][skill]["exp_to_next_level"],
        )
        return a
        # return user_data['skills'][skill]


def get_skill_time_series(
    username: str, skill: str, all_data: list, skill_attribute: str
):
    time_stamps = []
    skill_attribute_values = []
