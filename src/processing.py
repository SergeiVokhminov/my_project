from typing import Any


def filter_by_state(user_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция возвращает новый список словарей у которых соответствует ключ"""

    new_list = []

    for i in user_list:
        if i["state"] == state:
            new_list.append(i)

    return new_list


def sort_by_date(user_list: list[dict[str, Any]], date: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует список словарей по date"""
    new_list_sorted = sorted(user_list, key=lambda i: i["date"], reverse=date)
    return new_list_sorted
