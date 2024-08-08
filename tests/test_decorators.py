from typing import Any

from src.decorators import log


def test_log_sum(capsys: Any) -> None:
    @log(filename="../mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(6, 2)
    captured = capsys.readouterr()
    assert "my_function OK. Результат: 8" in captured.out


def test_log_subtraction(capsys: Any) -> None:
    @log(filename="../mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x - y

    my_function(6, 2)
    captured = capsys.readouterr()
    assert "my_function OK. Результат: 4" in captured.out


def test_log_multiplication(capsys: Any) -> None:
    @log(filename="../mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x * y

    my_function(6, 2)
    captured = capsys.readouterr()
    assert "my_function OK. Результат: 12" in captured.out


def test_log_division(capsys: Any) -> None:
    @log(filename="../mylog.txt")
    def my_function(x: int, y: int) -> float:
        return x / y

    my_function(6, 2)
    captured = capsys.readouterr()
    assert "my_function OK. Результат: 3.0" in captured.out

    my_function(6, 0)
    with open("../mylog.txt", "r") as f:
        data = f.read().split("\n")
    assert data[-2] == "my_function error: division by zero. Inputs:(6, 0), {}"


def test_log_sum_error(capsys: Any) -> None:
    @log(filename="../mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(6, "0")
    with open("../mylog.txt", "r") as f:
        data = f.read().split("\n")
    assert data[-2] == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs:(6, '0'), {}"


def test_log_not_file(capsys: Any) -> None:
    @log(filename="")
    def my_function(x: int, y: int) -> float:
        return x / y

    my_function(6, 2)
    captured = capsys.readouterr()
    assert "my_function OK. Результат: 3" in captured.out

    my_function(6, 0)
    captured = capsys.readouterr()
    assert "my_function error: division by zero. Inputs:(6, 0), {}\n" in captured.out


@log()
def test_log() -> str:
    return "test"
