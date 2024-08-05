import json
import logging
import os
from typing import Any

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)
PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")

my_logger = logging.getLogger("utils")
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
my_logger.addHandler(file_handler)
my_logger.setLevel(logging.INFO)


def get_json_file(path: str) -> Any:
    """
    Функция принимает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    :param path: Получает JSON-файл.
    :return: Возвращает список словарей с данными о финансовых транзакциях.
    """

    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                my_logger.info("Открытие файла")
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                my_logger.error("Неверный формат файла")
                return []
    except FileNotFoundError:
        my_logger.error("Файл не найден")
        return []


if __name__ == "__main__":
    print(get_json_file(PATH_TO_FILE))
