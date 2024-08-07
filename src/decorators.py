from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    :param filename: Принимает необязательный аргумент filename.
    :return:Если filename задан, логи записываются в указанный файл.
            Если filename не задан, логи выводятся в консоль.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} OK. Результат: {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                    print(log_message)
                else:
                    print(log_message)
            except Exception as f:
                error_message = f"{func.__name__} error: {f}. Inputs:{args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)

        return wrapper

    return decorator


@log(filename="../mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    my_function(10, 0)
