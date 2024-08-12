from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """
    Функция обрабатывает номер карты или счета и маскирует их.
    :param number: Принимает строку, содержащую тип и номер карты или счета.
    :return: Возвращает строку с замаскированным номером.
    """

    number_split = number.split()
    if number_split[0] == "Счет" and len(number_split[-1]) == 20:
        return f"{number_split[0]} {get_mask_account(number_split[-1])}"
    elif len(number_split[-1]) == 16:
        name_card = " ".join(number_split[:-1])
        return f"{name_card} {get_mask_card_number(''.join(number_split[-1]))}"
    else:
        return "Введены неверные данные"


def get_date(user_date: str) -> str:
    """
    Функция преобразует строку с датой в дату.
    :param user_date: Принимает строку с датой в формате "2024-03-11T02:26:18.671407".
    :return: Возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """

    date_obj = datetime.fromisoformat(user_date)
    return date_obj.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("MasterCard 1234567890098765"))
    print()
    print(mask_account_card("Счет 12345678900987654321"))
    print()
    print(get_date("2028-11-25T02:26:18.671407"))
