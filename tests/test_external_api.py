from typing import Any
from unittest.mock import patch

from src.external_api import fnc_convert_rud


@patch("requests.get")
def test_fnc_convert_rub(mock_test: Any) -> Any:
    transaction = {"amount": 200, "currency": "RUB"}
    mock_test.return_value.json.return_value = {"result": 200}
    assert fnc_convert_rud(transaction) == 200


@patch("requests.get")
def test_fnc_convert_usd(mock_test: Any) -> Any:
    transaction = {"amount": 100, "currency": "USD"}
    mock_test.return_value.json.return_value = {"result": 12312.21}
    assert fnc_convert_rud(transaction) == 12312.21


@patch("requests.get")
def test_fnc_convert_eur(mock_test: Any) -> Any:
    transaction = {"amount": 100, "currency": "EUR"}
    mock_test.return_value.json.return_value = {"result": 15321.33}
    assert fnc_convert_rud(transaction) == 15321.33
