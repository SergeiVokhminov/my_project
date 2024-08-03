import json
import os

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def get_json_file(path: str) -> list:
    """Функция, которая принимает JSON-файл и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                data = []
                return data
    except FileNotFoundError:
        data = []
        return data


if __name__ == "__main__":
    print(get_json_file(PATH_TO_FILE))
