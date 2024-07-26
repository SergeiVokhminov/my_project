from typing import Any, Callable
from functools import wraps


def log(filename: Any) -> Callable:
    """Декоратор, который логирует начало или конец работы."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f'{func.__name__} OK. Результат: {result}'
                with open(filename, "a", encoding='utf-8') as f:
                    f.write(log_message + '\n')
                print(log_message)
            except Exception as f:
                error_message = f"{func.__name__} error: {f}. Inputs:{args}, {kwargs}"
                with open(filename, "a", encoding='utf-8') as f:
                    f.write(error_message + '\n')
                print(error_message)
        return wrapper
    return decorator


@log(filename='../mylog.txt')
def my_function(x, y):
    return int(x / y)


my_function(10, 0)
# print(my_function(10, 0))
