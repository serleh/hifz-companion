import json
from pathlib import Path


def load_ayah(path):
    with Path(path).open(encoding='utf-8') as file:
        return json.load(file)