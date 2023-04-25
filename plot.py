from extract import load_data
from transform import get_skill_time_series
import matplotlib.pyplot as plt

all_data = load_data("data/")
user_list = ["shupwup", "telemascope", "jerome-o"]


def main():
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
    plt.show()


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
