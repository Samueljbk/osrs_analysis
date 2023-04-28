from extract import load_data
from transform import get_skill_time_series, get_user_data
import matplotlib.pyplot as plt
import numpy as np


def main():
    all_data = load_data("data/")
    user_list = ["shupwup", "telemascope", "jerome-o", "ryan the ant"]
    username = "shupwup"
    skill = "total"
    skill_attribute = "experience"

    plot_relative_data(all_data, user_list, skill, skill_attribute)
    plot_absolute_data(all_data, user_list, skill, skill_attribute)
    plot_all_skill_xp(all_data, username)
    plot_skill_xp_bar(all_data, username)
    plt.show()


def plot_skill_xp_bar(all_data, username):
    fig, ax = plt.subplots()

    user_data = get_user_data(username, all_data[0])
    skills = user_data["skills"].keys()

    skill_xp_gains = []
    skill_labels = []

    for skill in skills:
        _, skill_attribute_value_list = get_skill_time_series(
            username, skill, all_data, "experience"
        )
        xp_gain = skill_attribute_value_list[-1] - skill_attribute_value_list[0]

        if xp_gain > 0:
            skill_xp_gains.append(xp_gain)
            skill_labels.append(skill)

    ax.bar(skill_labels, skill_xp_gains)

    ax.set_title(f"Skill XP gains for {username}")
    ax.set_ylabel("XP gained")
    ax.set_xlabel("Skills")
    plt.xticks(rotation=45)


def plot_all_skill_xp(all_data, username):
    fig, ax = plt.subplots()

    user_data = get_user_data(username, all_data[0])
    skills = user_data["skills"].keys()

    for skill in skills:
        timestamp_list, skill_attribute_value_list = get_skill_time_series(
            username, skill, all_data, "experience"
        )
        first_xp_value = skill_attribute_value_list[0]
        offset_xp_value = [
            xp_value - first_xp_value for xp_value in skill_attribute_value_list
        ]
        if not all(np.array(offset_xp_value) == 0):
            ax.plot(
                timestamp_list, offset_xp_value, label=skill
            )  # Plot some data on the axes.

    ax.set_title(f"All skill XP for {username}")
    ax.legend()
    ax.set_ylabel("Skill experience")
    ax.set_xlabel("Timestamp")


def plot_relative_data(all_data, user_list, skill, skill_attribute):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.

    for user in user_list:
        timestamp_list, skill_attribute_value_list = get_skill_time_series(
            user, skill, all_data, skill_attribute
        )

        first_xp_value = skill_attribute_value_list[0]
        offset_xp_value = [
            xp_value - first_xp_value for xp_value in skill_attribute_value_list
        ]

        ax.plot(
            timestamp_list, offset_xp_value, label=user
        )  # Plot some data on the axes.

    ax.set_title(f"This is a plot of {skill} {skill_attribute}")
    ax.legend()
    ax.set_ylabel(f"{skill} {skill_attribute}")
    ax.set_xlabel("Timestamp")


def plot_absolute_data(all_data, user_list, skill, skill_attribute):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.

    for user in user_list:
        timestamp_list, skill_attribute_value_list = get_skill_time_series(
            user, skill, all_data, skill_attribute
        )
        ax.plot(
            timestamp_list, skill_attribute_value_list, label=user
        )  # Plot some data on the axes.

    ax.set_title(f"This is a plot of {skill} {skill_attribute}")
    ax.legend()
    ax.set_ylabel(f"{skill} {skill_attribute}")
    ax.set_xlabel("Timestamp")


if __name__ == "__main__":
    main()
