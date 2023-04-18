import json


def load_data_file(filename) -> dict:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    data = load_data_file('data/2023-04-11-05-11.json')
    print(data)
