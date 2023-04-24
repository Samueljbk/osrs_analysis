from typing import Dict, List


class UserSkill:
    def __init__(
        self,
        rank: int,
        level: int,
        experience: int,
        next_level_exp: int,
        exp_to_next_level: int,
    ):
        self.rank = rank
        self.level = level
        self.experience = experience
        self.next_level_exp = next_level_exp
        self.exp_to_next_level = exp_to_next_level


class UserBoss:
    def __init__(self, rank: int, kills: int):
        self.rank = rank
        self.kills = kills


class UserData:
    def __init__(
        self, username: str, skills: Dict[str, UserSkill], bosses: Dict[str, UserBoss]
    ):
        self.username = username
        self.skills = skills
        self.bosses = bosses


class Data:
    def __init__(self, timestamp: float, users: List[UserData]):
        self.timestamp = timestamp
        self.users = users


import json
from typing import Dict, Union


def create_data_from_json(json_data: str) -> Data:
    parsed_data: Dict[
        str, Union[float, List[Dict[str, Union[str, Dict[str, Union[int, float]]]]]]
    ] = json.loads(json_data)
    timestamp = parsed_data["timestamp"]
    users_data = parsed_data["users"]

    users: List[UserData] = []
    for user_data in users_data:
        username = user_data["username"]

        skills_data = user_data["skills"]
        skills: Dict[str, UserSkill] = {}
        for skill_name, skill_data in skills_data.items():
            skill = UserSkill(
                rank=skill_data["rank"],
                level=skill_data["level"],
                experience=skill_data["experience"],
                next_level_exp=skill_data["next_level_exp"],
                exp_to_next_level=skill_data["exp_to_next_level"],
            )
            skills[skill_name] = skill

        bosses_data = user_data["bosses"]
        bosses: Dict[str, UserBoss] = {}
        for boss_name, boss_data in bosses_data.items():
            boss = UserBoss(rank=boss_data["rank"], kills=boss_data["kills"])
            bosses[boss_name] = boss

        user = UserData(username=username, skills=skills, bosses=bosses)
        users.append(user)

    return Data(timestamp=timestamp, users=users)


if __name__ == "__main__":
    with open("data/2023-04-11-05-06.json") as f:
        data = create_data_from_json(f.read())
    print(data)

    data.users[0].skills["attack"].experience
