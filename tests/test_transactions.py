import pytest

from typing import Any, Dict, List
from src.transactions import get_transactions_fnc, get_transactions_key

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
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
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


@pytest.fixture
def coll_fnc() -> List[Dict[str, Any]]:
    return [
            {"id": 41428829, "state": "EXECUTED", "description": "Перевод организации"},
            {"id": 939719570, "state": "EXECUTED", "description": "Перевод организации"},
            {"id": 594226727, "state": "CANCELED", "description": "Перевод с карты на карту"},
            {"id": 615064591, "state": "CANCELED", "description": "Открытие вклада"}
    ]


def tests_transactions_fnc(coll_fnc: List[Dict[str, Any]]) -> Any:
    assert get_transactions_fnc(coll_fnc, 'открытие') == [
        {"id": 615064591, "state": "CANCELED", "description": "Открытие вклада"}
    ]


@pytest.mark.parametrize(
    "transactions, description, expected",
    [
        (transactions,
         ["перевод с карты", "перевод Организации"],
         {"Перевод организации": 2, "Перевод с карты на карту": 1}),
        (transactions,
         ["перевод с карты"],
         {"Перевод с карты на карту": 1}),
        (transactions, [], {}),
        ([], ["перевод с карты", "перевод организации"], {}),
    ],
)
def tests_transactions_key(transactions, description, expected):
    assert get_transactions_key(transactions, description) == expected
