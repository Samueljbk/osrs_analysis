from extract import load_data
from transform import get_skill_time_series
import matplotlib.pyplot as plt


def main():
    all_data = load_data("data/")
    user_list = ["shupwup", "telemascope", "jerome-o", "ryan the ant"]
    skill = "total"
    skill_attribute = "experience"

    plot_relative_data(all_data, user_list, skill, skill_attribute)
    plot_absolute_data(all_data, user_list, skill, skill_attribute)
    plt.show()


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
