from typing import Any, Dict, List


def filter_by_state(user_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей у которых соответствует ключ"""

    new_list = []

    for item in user_list:
        if item["state"] == state:
            new_list.append(item)

    return new_list


def sort_by_date(user_list: List[Dict[str, Any]], is_descending: bool = True) -> List[Dict[str, Any]]:
    """Функция сортирует список словарей по date"""
    new_list_sorted = sorted(user_list, key=lambda item: item["date"], reverse=is_descending)
    return new_list_sorted
