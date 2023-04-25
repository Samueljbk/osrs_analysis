from extract import load_data
from transform import get_skill_time_series
import matplotlib.pyplot as plt

all_data = load_data("data/")
user_list = ["shupwup", "jerome-o", "ryan the ant"]
timestamp_list, skill_attribute_value_list = get_skill_time_series(
    "shupwup", "defense", all_data, "level"
)


def main():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(
        timestamp_list, skill_attribute_value_list, label="Defense Level"
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
