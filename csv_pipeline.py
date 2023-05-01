import csv
from collections import defaultdict

import pandas as pd

from extract import load_data

_DATA_DIR = "data/"


def csv_tidy_csvwriter():
    data = load_data(_DATA_DIR)
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

    pd.DataFrame(data_dict).to_csv("pandas_skills.csv", index=False)


def main():
    csv_tidy_csvwriter()


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
