import os

import pandas as pd

PATH_TO_FILE_CSV = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


def get_file_csv(filename: str) -> list[dict]:
    """
    Функция для считывания финансовых операций из CSV.
    :param filename: Принимает путь к файлу CSV в качестве аргумента.
    :return: Выводит список словарей с транзакциями.
    """

    try:
        pd_csv = pd.read_csv(filename)
        return pd_csv.to_dict(orient="records")
    except Exception as ex:
        print(f"Произошла ошибка {ex}")
        return []


if __name__ == "__main__":
    print(get_file_csv(PATH_TO_FILE_CSV))


def get_file_xlsx(filename: str) -> list[dict]:
    """
    Функция для считывания финансовых операций из Excel.
    :param filename: Принимает путь к файлу Excel в качестве аргумента.
    :return: Выводит список словарей с транзакциями.
    """

    try:
        pd_excel = pd.read_excel(filename)
        return pd_excel.to_dict(orient="records")
    except Exception as ex:
        print(f"Произошла ошибка {ex}")
        return []


if __name__ == "__main__":
    print(get_file_xlsx(PATH_TO_FILE_EXCEL))
