import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("6831982476737658", "6831 98** **** 7658"),
        ("123456789009876", "Неверный номер карты"),
        ("sadfg12345", "Неверный номер карты"),
        ("", "Неверный номер карты"),
    ],
)
def test_get_mask_card_number(string: str, expected_result: str) -> None:
    """Тестирование функции маскировки номера карты."""
    assert get_mask_card_number(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("12346831982476737658", "**7658"),
        ("123456789009876", "Неверный номер счета"),
        ("sadfg12345", "Неверный номер счета"),
        ("", "Неверный номер счета"),
    ],
)
def tests_get_mask_account(string: str, expected_result: str) -> None:
    """Тестирование функции маскировки счета."""
    assert get_mask_account(string) == expected_result
