from typing import Any
from unittest.mock import patch

import pytest

from src.utils import get_json_file


@pytest.fixture
def get_test_ok() -> Any:
    return "../data/operations.json"


@pytest.fixture
def get_test_none() -> Any:
    return "None"


@pytest.fixture
def get_test_wrong() -> Any:
    return "../data/wrong_operations.json"


@patch("builtins.open")
def test_get_json_ok(open_mock: Any) -> Any:
    open_mock.return_value.__enter__.return_value.read.return_value = (
        '[{"name": "dict_test"}, {"name": ' '"one_more"}]'
    )
    assert get_json_file("any_path") == [{"name": "dict_test"}, {"name": "one_more"}]


def test_get_json_none(get_test_wrong: Any) -> Any:
    assert get_json_file(get_test_wrong) == []


def test_get_json_wrong(get_test_wrong: Any) -> Any:
    assert get_json_file(get_test_wrong) == []
