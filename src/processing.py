from typing import Any, Dict, List


def filter_by_state(user_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция возвращает новый список словарей у которых соответствует ключ state.
    :param user_list: Принимает список словарей.
    :param state: Принимает опционально значение для ключа state (по умолчанию 'EXECUTED').
    :return: Возвращает новый список словарей, содержащий только те словари, 
    у которых ключ state соответствует указанному значению.
    """

    new_list = []

    for item in user_list:
        if item.get("state") == state:
            new_list.append(item)

    return new_list


def sort_by_date(user_list: List[Dict[str, Any]], is_descending: bool = True) -> List[Dict[str, Any]]:
    """
    Функция сортирует список словарей по date.
    :param user_list: Принимает список словарей.
    :param is_descending: Принимает необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    :return: Возвращает новый список, отсортированный по дате (date).
    """

    new_list_sorted = sorted(user_list, key=lambda item: item["date"], reverse=is_descending)
    return new_list_sorted
