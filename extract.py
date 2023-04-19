import json
import os


def load_data_file(filename) -> dict:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def load_data(directory):
    data = []
    # TODO: Make into list comprehension
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            file_data = load_data_file(file_path)
            data.append(file_data)
    return data


if __name__ == '__main__':
    data = load_data('data/')
    print(data)
