import json
import os

DATA_FILE = "flashcard_data.json"

def load_words():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_words(words):
    with open(DATA_FILE, "w") as f:
        json.dump(words, f, indent=2)