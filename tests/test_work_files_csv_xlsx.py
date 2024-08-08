from typing import Any
from unittest.mock import patch

from src.work_files_csv_xlsx import get_file_csv, get_file_xlsx


@patch("pandas.read_csv")
def test_csv_none(mock_read_csv: Any) -> Any:
    mock_read_csv.return_value.to_dict.return_value = []
    assert get_file_csv("all_file") == []


@patch("pandas.read_csv")
def test_csv_ok(mock_read_csv: Any) -> Any:
    mock_read_csv.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]
    assert get_file_csv("all_file") == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]


@patch("pandas.read_excel")
def test_excel_ok(mock_read_excel: Any) -> Any:
    mock_read_excel.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]
    assert get_file_xlsx("all_file") == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]


@patch("pandas.read_excel")
def test_excel_error(mock_read_excel: Any) -> Any:
    mock_read_excel.return_value.to_dict.return_value = []
    assert get_file_xlsx("all_file") == []
