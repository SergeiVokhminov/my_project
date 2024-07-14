def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты."""

    if card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** {'*' * 4} {card_number[-4:]}"
    else:
        return "Неверный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета."""

    if account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        return "Неверный номер счета"
