import csv
from extract import load_data
import pandas as pd


_DATA_DIR = "data/"


def csv_tidy_csvwriter():
    data = load_data(_DATA_DIR)

    with open("skill_data.csv", "w", newline="") as csvfile:
        skill_writer = csv.writer(csvfile, delimiter=",", quotechar='"')

        headers = ["username", "timestamp", "skill", "experience", "level"]
        skill_writer.writerow(headers)

        for scrape in data:
            timestamp = scrape["timestamp"]
            for user in scrape["users"]:
                username = user["username"]
                for skill, skill_data in user["skills"].items():
                    level = skill_data["level"]
                    experience = skill_data["experience"]

                    skill_writer.writerow(
                        [
                            username,
                            timestamp,
                            skill,
                            experience,
                            level,
                        ]
                    )


# from collections import defaultdict

# def csv_tidy_pandas():
#     data = load_data(_DATA_DIR)
#     data_dict = defaultdict(list)

#     for scrape in data:
#         timestamp = scrape["timestamp"]
#         for user in scrape["users"]:
#             username = user["username"]
#             for skill, skill_data in user["skills"].items():
#                 level = skill_data["level"]
#                 experience = skill_data["experience"]

#                 skill_writer.writerow([])


def main():
    csv_tidy_csvwriter()


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
