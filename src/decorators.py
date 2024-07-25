from typing import Any, Callable
from functools import wraps


def log(filename: Any) -> Callable:
    """Декоратор, который логирует начало и конец работы """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f'{func.__name__} вызывается с аргументами: {args} {kwargs}, {result}'
                print('my_function OK')
            except Exception as f:
                log_message = f'{func.__name__} error: {f}.'
                print(f'my_function error: {f}. Inputs:{args}, {kwargs}\n')
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(f'{log_message}\n')
            else:
                print(f'{log_message}\n')
            return result
        return wrapper
    return decorator


@log(filename='mylog.txt')
def my_funcs(x: int, y: int) -> int:
    return x + y


# my_funcs(1, 6)
print(my_funcs(1, 6))
