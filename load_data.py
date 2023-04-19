import json
import os
from loader import load_data_file
from pprint import pprint


def load_data(directory):
    data = {}
    # TODO: Make into list comprehension
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            file_data = load_data_file(file_path)
            data[filename] = file_data
    return data


if __name__ == '__main__':
    data = load_data('data/')
    pprint(data)
