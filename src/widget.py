from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция, которая обрабатывает номер карты или счета и маскирует их."""

    number_split = number.split()
    if "Счет" in number_split and len(number_split[1]) == 20:
        return f"{number_split[0]} {get_mask_account(number_split[1])}"
    elif number_split[0] in ["Visa", "MasterCard", "Maestro", "Visa Classic", "Visa Platinum", "Visa Gold"]:
        name_card = " ".join(number_split)[:-16]
        return f"{name_card}{get_mask_card_number(''.join(number_split)[-16:])}"
    else:
        return "Введены неверные данные"


def get_date(user_date: str) -> str:
    """Функция, которая преобразует строку в дату."""

    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    date_obj = datetime.strptime(user_date, date_format)
    return date_obj.strftime("%d.%m.%Y")
