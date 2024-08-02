import os

import requests
from dotenv import load_dotenv

load_dotenv()

apilayer_token = os.getenv("API_KEY")


def fnc_convert_rud(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях."""

    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return round(float(amount), 2)
    elif currency == "USD" or currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": apilayer_token}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data_result = response.json()
        return round(float(data_result["result"]), 2)
    else:
        raise ValueError(f"Неизвестная валюта: {currency}")


if __name__ == "__main__":
    user_dict_rub = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    print(f"Сумма в рублях (RUB): {fnc_convert_rud(user_dict_rub)}")
    user_dict_usd = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    print(f"Сумма в рублях (USD): {fnc_convert_rud(user_dict_usd)}")
    user_dict_eur = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    print(f"Сумма в рублях (EUR): {fnc_convert_rud(user_dict_eur)}")
