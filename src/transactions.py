import re
from collections import Counter
from typing import Any, Dict, List

user_dict = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на карту",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
        "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 10848359769870775355",
        "to": "Счет 21969751544412966366",
    },
    {
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-07-12T20:41:47.882230",
        "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "from": "Счет 48894435694657014368",
        "to": "Счет 38976430693692818358",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
]


def get_transactions_fnc(transactions: List[Dict], search_bar: str) -> Any:
    """
    Функция для поиска в списке словарей операций по заданной строке.
    :param transactions: Принимает список словарей с данными о банковских операциях.
    :param search_bar: Принимает строку поиска.
    :return: Возвращает список словарей, у которых в описании есть данная строка.
    """

    pattern = rf"{search_bar}"
    result_dict = []
    for item in transactions:
        if re.findall(pattern, item.get("description"), flags=re.I):
            result_dict.append(item)

    return result_dict


def get_transactions_key(transactions: List[Dict], descriptions: List[str]) -> Counter[Any | None]:
    """
    Функция для подсчета количества банковских операций определенного типа.
    :param transactions: Принимает список словарей с данными о банковских операциях.
    :param descriptions: Принимает список категорий операций.
    :return: Возвращает словарь, в котором ключи — это названия категорий,
             а значения — это количество операций в каждой категории.
    """

    result_dict = []
    for transaction in transactions:
        for description in descriptions:
            pattern = rf"{description}"
            if re.findall(pattern, transaction.get("description"), flags=re.I):
                result_dict.append(transaction.get("description"))

    result_counter = Counter(result_dict)
    return result_counter


if __name__ == "__main__":
    print(get_transactions_fnc(user_dict, "вклад"))
    print()
    print(get_transactions_key(user_dict, ["Карт", "Счет", "Открытие"]))
