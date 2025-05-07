# database/db.py

import json
import os

from models.vocabulary import Vocabulary

DB_PATH = "data/vocab.json"


def save_vocab_list(vocab_list):
    data = [vars(v) for v in vocab_list]
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_vocab_list():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [Vocabulary(**item) for item in data]
        except json.JSONDecodeError:
            return []
