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


if __name__ == '__main__':
    print(filter_by_state(
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    )
    )
    print()
    print(sort_by_date(
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    )
    )
