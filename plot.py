from extract import load_data
from transform import get_skill_time_series
import matplotlib.pyplot as plt


def main():
    all_data = load_data("data/")
    user_list = ["shupwup", "telemascope", "jerome-o"]

    plot_relative_data(all_data, user_list)
    plot_absolute_data(all_data, user_list)
    plt.show()


def plot_relative_data(all_data, user_list):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.

    for user in user_list:
        timestamp_list, skill_attribute_value_list = get_skill_time_series(
            user, "total", all_data, "experience"
        )

        first_xp_value = skill_attribute_value_list[0]
        offset_xp_value = [
            xp_value - first_xp_value for xp_value in skill_attribute_value_list
        ]

        ax.plot(
            timestamp_list, offset_xp_value, label=user
        )  # Plot some data on the axes.

    ax.set_title("Defense Level for shupwup")
    ax.legend()
    ax.set_ylabel("Defense Level")
    ax.set_xlabel("Timestamp")


def plot_absolute_data(all_data, user_list):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.

    for user in user_list:
        timestamp_list, skill_attribute_value_list = get_skill_time_series(
            user, "total", all_data, "experience"
        )
        ax.plot(
            timestamp_list, skill_attribute_value_list, label=user
        )  # Plot some data on the axes.

    ax.set_title("Defense Level for shupwup")
    ax.legend()
    ax.set_ylabel("Defense Level")
    ax.set_xlabel("Timestamp")


if __name__ == "__main__":
    main()
