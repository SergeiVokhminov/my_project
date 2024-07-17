import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 68319824767376580987", "Счет **0987"),
        ("Счет 6831982476737658", "Введены неверные данные"),
        ("Visa 6831982476737658", "Visa 6831 98** **** 7658"),
        ("1", "Введены неверные данные"),
        ("123 234", "Введены неверные данные"),
        ("Visa 12345", "Неверный номер карты"),
        ("Maestro 1234567890098765", "Maestro 1234 56** **** 8765"),
    ],
)
def test_mask_account_card(string: str, expected_result: str) -> None:
    """Тестирование функции маскировки номера карты или счета"""
    assert mask_account_card(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-04-12T02:26:18.671408", "12.04.2024"),
    ],
)
def tests_get_date(string: str, expected_result: str) -> None:
    """Тестирование функции преобразования даты."""
    assert get_date(string) == expected_result
