from typing import Any, Dict, Generator, List


def filter_by_currency(transaction: List[Dict[str, Any]], currency: str) -> Generator[Any, None, None]:
    """Функция фильтрующая словарь по заданному значению."""
    for item in transaction:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


def transaction_descriptions(transaction: List[Dict[str, Any]]) -> Generator[Any, None, None]:
    """Функция, которая возвращает описание каждой операции по очереди."""
    for key in transaction:
        yield key.get("description")


def card_number_generator(start: int, finish: int) -> Generator[str, None, None]:
    """Функция, которая генерирует номера карт."""
    for number in range(start, finish + 1):
        card_numbers = str(number)
        while len(card_numbers) < 16:
            card_numbers = "0" + card_numbers
        formatted_card_number = f"{card_numbers[:4]} {card_numbers[4:8]} {card_numbers[8:12]} {card_numbers[12:]}"
        yield formatted_card_number
