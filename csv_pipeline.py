from collections import defaultdict

import pandas as pd

from extract import load_data

_DATA_DIR = "data/"
_DEFAULT_SKILLS_FILE = "skills.csv"
_DEFAULT_UNTIDY_SKILLS_FILE = "skills_untidy.csv"


def write_csv_tidy(
    data_dir: str = None,
    fn: str = None,
):
    data_dir = data_dir or _DATA_DIR
    fn = fn or _DEFAULT_SKILLS_FILE

    data = load_data(data_dir)
    data_dict = defaultdict(list)

    for scrape in data:
        timestamp = scrape["timestamp"]
        for user in scrape["users"]:
            username = user["username"]
            for skill, skill_data in user["skills"].items():
                level = skill_data["level"]
                experience = skill_data["experience"]

                data_dict["username"].append(username)
                data_dict["timestamp"].append(timestamp)
                data_dict["skill"].append(skill)
                data_dict["experience"].append(experience)
                data_dict["level"].append(level)

    pd.DataFrame(data_dict).to_csv(fn, index=False)


def write_csv_untidy(
    data_dir: str = None,
    fn: str = None,
):
    data_dir = data_dir or _DATA_DIR
    fn = fn or _DEFAULT_UNTIDY_SKILLS_FILE

    data = load_data(data_dir)
    data_dict = defaultdict(list)

    for scrape in data:
        for user in scrape["users"]:
            data_dict["timestamp"].append(scrape["timestamp"])
            data_dict["username"].append(user["username"])

            for skill, skill_data in user["skills"].items():
                data_dict[skill].append(skill_data["experience"])

    pd.DataFrame(data_dict).to_csv(fn, index=False)


def main():
    df = pd.read_csv(_DEFAULT_UNTIDY_SKILLS_FILE)
    df = df.sort_values(by="timestamp")
    df = df.set_index("timestamp")

    # offset per "username" the defense skill by the first value
    df["defense"] = df["defense"] - df.groupby("username")["defense"].transform("min")

    df.groupby("username")["defense"].plot(legend=True)

    import matplotlib.pyplot as plt

    plt.show()


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
