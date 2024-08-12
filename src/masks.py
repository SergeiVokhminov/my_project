import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

my_logger = logging.getLogger("masks")
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
my_logger.addHandler(file_handler)
my_logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str | int) -> str:
    """
    Функция маскирует номер карты.
    :param card_number: Получает номер карты.
    :return: Маскирует номер карты.
    """

    my_logger.info(f"Начало работы функции, получен номер карты: {card_number}")
    if str(card_number).isdigit() and len(str(card_number)) == 16:
        my_logger.info("Номер указанной карты замаскирован")
        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** {'*' * 4} {str(card_number)[-4:]}"
    else:
        my_logger.error("Указан неверный номер карты")
        return "Неверный номер карты"


def get_mask_account(account_number: str | int) -> str:
    """
    Функция маскирует номер счета.
    :param account_number: Получает номер счета.
    :return: Замаскированный счет.
    """

    my_logger.info(f"Начало работы функции, получен номер счёта: {account_number}")
    if str(account_number).isdigit() and len(str(account_number)) == 20:
        my_logger.info("Номер указанного счёта замаскирован")
        return f"**{str(account_number)[-4:]}"
    else:
        my_logger.error("Указан неверный номер счёта")
        return "Неверный номер счёта"


if __name__ == "__main__":
    print(get_mask_card_number(6831982476737650))
    print()
    print(get_mask_account(68319824767376581234))
