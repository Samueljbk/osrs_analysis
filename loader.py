import json
import os


def load_data_file(filename) -> dict:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
