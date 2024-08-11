from typing import Any, Dict, Generator, List


def filter_by_currency(transaction: List[Dict[str, Any]], currency: str) -> Generator[Any, None, None]:
    """
    Функция фильтрующая словарь по заданному значению.
    :param transaction: Принимает на вход список словарей, представляющих транзакции.
    :param currency: Принимает наименование валюты (например, USD).
    :return: Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
    """

    for item in transaction:
        if item.get("operationAmount").get("currency").get("code") == currency:
            yield item


def transaction_descriptions(transaction: List[Dict[str, Any]]) -> Generator[Any, None, None]:
    """
    Генератор возвращает описание каждой операции по очереди из списка словарей с транзакциями.
    :param transaction: Принимает список словарей с транзакциями.
    :return: Возвращает описание каждой операции по очереди.
    """

    for key in transaction:
        yield key.get("description")


def card_number_generator(start: int, finish: int) -> Generator[str, None, None]:
    """
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    :param start: Принимает начальное значение для генерации диапазона номеров.
    :param finish: Принимает конечное значения для генерации диапазона номеров.
    :return: Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    """

    for number in range(start, finish + 1):
        card_numbers = str(number)
        while len(card_numbers) < 16:
            card_numbers = "0" + card_numbers
        formatted_card_number = f"{card_numbers[:4]} {card_numbers[4:8]} {card_numbers[8:12]} {card_numbers[12:]}"
        yield formatted_card_number


if __name__ == "__main__":
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
    ]

    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions))
    print()
    descriptions = transaction_descriptions(transactions)
    for _ in range(2):
        print(next(descriptions))
    print()
    for card_number in card_number_generator(1, 5):
        print(card_number)
