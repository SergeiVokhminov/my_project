import os

import requests
from dotenv import load_dotenv

load_dotenv()

apilayer_token = os.getenv("API_KEY")


def fnc_convert_rud(transaction: dict) -> float | str:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях."""

    amount = transaction["amount"]
    currency = transaction["currency"]

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
        return "Неизвестная валюта"


if __name__ == "__main__":
    print(f"Сумма в рублях (RUB): {fnc_convert_rud({'amount': 100, 'currency': 'RUB'})}")
    print(f"Сумма в рублях (USD): {fnc_convert_rud({'amount': 100, 'currency': 'USD'})}")
    print(f"Сумма в рублях (EUR): {fnc_convert_rud({'amount': 100, 'currency': 'EUR'})}")
    print(f"Сумма в рублях (CURRENCY): {fnc_convert_rud({'amount': 100, 'currency': 'E'})}")
