import json
import random
from pathlib import Path


def load_account() -> dict[str, str]:
    with open(Path().resolve() / "data/accounts.json", encoding="utf-8") as f:
        accounts = json.load(f)
    return random.choice(accounts)
