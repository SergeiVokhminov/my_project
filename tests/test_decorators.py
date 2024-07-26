from src.decorators import log


def test_log_sum(capsys):
    @log(filename="../mylog.txt")
    def my_function(x: int, y: int) -> int:
        return int(x + y)

    my_function(6, 2)
    captured = capsys.readouterr()
    assert "my_function OK. Результат: 8" in captured.out


def test_log_subtraction(capsys):
    @log(filename="../mylog.txt")
    def my_function(x: int, y: int) -> int:
        return int(x - y)

    my_function(6, 2)
    captured = capsys.readouterr()
    assert "my_function OK. Результат: 4" in captured.out


def test_log_multiplication(capsys):
    @log(filename="../mylog.txt")
    def my_function(x: int, y: int) -> int:
        return int(x * y)

    my_function(6, 2)
    captured = capsys.readouterr()
    assert "my_function OK. Результат: 12" in captured.out


def test_log_division(capsys):
    @log(filename="../mylog.txt")
    def my_function(x: int, y: int) -> int:
        return int(x / y)

    my_function(6, 2)
    captured = capsys.readouterr()
    assert "my_function OK. Результат: 3" in captured.out

    try:
        my_function(6, 0)
    except TypeError:
        captured = capsys.readouterr()
        assert "my_function error: Inputs: (6, 0) {}" in captured.out
