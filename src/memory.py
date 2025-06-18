import os
import json

FILE_PATH = "shopping_list.json"

def load_shopping_list():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return {}

def save_shopping_list(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)
