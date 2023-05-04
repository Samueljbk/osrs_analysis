from pydantic import BaseModel
from typing import Dict, List


class SkillData(BaseModel):
    rank: int
    level: int
    experience: int
    next_level_exp: int = None
    exp_to_next_level: int = None


class BossData(BaseModel):
    rank: int
    kills: int


class UserData(BaseModel):
    username: str
    skills: Dict[str, SkillData]
    bosses: Dict[str, BossData]


class ScrapeData(BaseModel):
    users: List[UserData]
    timestamp: float


def main():
    rawdata = """{
                    "rank": 450107,
                    "level": 1838,
                    "experience": 99750531,
                    "next_level_exp": null,
                    "exp_to_next_level": null
                }"""

    skill_data = SkillData.parse_raw(rawdata)
    print(skill_data)
    print(skill_data.experience)

    file_data = ScrapeData.parse_file("data/2023-04-24-09-00.json")
    print(file_data)
    users = file_data.users
    users[0].skills["defense"].experience


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
