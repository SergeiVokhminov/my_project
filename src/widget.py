from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """
    Функция обрабатывает номер карты или счета и маскирует их.
    :param number: Принимает строку, содержащую тип и номер карты или счета.
    :return: Возвращает строку с замаскированным номером.
    """

    number_split = number.split()
    if "Счет" in number_split and len(number_split[1]) == 20:
        return f"{number_split[0]} {get_mask_account(number_split[1])}"
    elif number_split[0] in ["Visa", "MasterCard", "Maestro", "Visa Classic", "Visa Platinum", "Visa Gold"]:
        name_card = " ".join(number_split)[:-16]
        return f"{name_card}{get_mask_card_number(''.join(number_split)[-16:])}"
    else:
        return "Введены неверные данные"


def get_date(user_date: str) -> str:
    """
    Функция преобразует строку с датой в дату.
    :param user_date: Принимает строку с датой в формате "2024-03-11T02:26:18.671407".
    :return: Возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """

    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    date_obj = datetime.strptime(user_date, date_format)
    return date_obj.strftime("%d.%m.%Y")


if __name__ == '__main__':
    print(mask_account_card('MasterCard 1234567890098765'))
    print(mask_account_card('Счет 12345678900987654321'))
    print()
    print(get_date("2028-11-25T02:26:18.671407"))
