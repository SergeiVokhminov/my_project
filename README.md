# Домашний проект. Виджет банковских операций.

## Описание:

Данный проект включает в себя выполнение ряда домашних заданий. 
Выполнение домашних заданий, поможет написать виджет банковских операций.
В проекте реализованы функции, которые:
1. в модуле masks.py маскирует номер счета или карты пользователя;
2. в модуле widget.py принимает название карты и номер или счет и номер и маскирует номер;
3. в модуле processing.py создается новый список словарей у которых ключ соответствует значению, а также список словарей сортируется по 'date'.
4. в модуле generators.py реализованы три генератора.
5. в модуле decorators.py реализован декоратор log.
6. в модуле external_api.py выводит сумму транзакции в рублях. Если транзакция в долларах или евро, то конвектирует в рубли.
7. в модуле utils.py принимает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

## Используемые зависимости в проекте:

- версия Python 3.12.4
- black==24.4.2
- click==8.1.7
- coverage==7.6.0
- flake8==7.1.0
- iniconfig==2.0.0
- isort==5.13.2
- mccabe==0.7.0
- mypy==1.10.1
- mypy-extensions==1.0.0
- packaging==24.1
- pathspec==0.12.1
- platformdirs==4.2.2
- pluggy==1.5.0
- pycodestyle==2.12.0
- pyflakes==3.2.0
- pytest==8.2.2
- pytest-cov==5.0.0
- typing_extensions==4.12.2

## Установка

1. Клонируйте репозиторий:
'''
git clone https://github.com/SergeiVokhminov/my_project.git
'''

2. Установите зависимости:
```
pip install -r requirements.txt
```

## Использование модуля main.py

1. откройте модуль main.py.
2. заполните переменные user_numbers, user_date_srt, user_list.
3. запустите модуль main.py.

## Использование модуля external_api.py

1. откройте модуль external_api.py
2. запустите для примера:
'''
if __name__ == "__main__":
    print(f"Сумма в рублях (RUB): {fnc_convert_rud({'amount': 100, 'currency': 'RUB'})}")
    print(f"Сумма в рублях (USD): {fnc_convert_rud({'amount': 100, 'currency': 'USD'})}")
    print(f"Сумма в рублях (EUR): {fnc_convert_rud({'amount': 100, 'currency': 'EUR'})}")
    print(f"Сумма в рублях (CURRENCY): {fnc_convert_rud({'amount': 100, 'currency': 'E'})}")
'''

## Использование модуля utils.py

1. откройте модуль utils.py
2. запустите для примера:
'''
if __name__ == "__main__":
    print(get_json_file(PATH_TO_FILE))
'''

## Проверка работы генераторов:

1. откройте модуль tests/test_generators.py
2. запустите для примера:
'''
def test_filter_by_currency(coll: List[Dict[str, dict]]) -> None:
    """Тестирование функции вывода списка по ключевому значению."""
    usd_transaction = filter_by_currency(transactions, "USD")
    for key in range(3):
        assert next(usd_transaction)
'''

## Работа декоратора

1. откройте модуль decorators.py
2. запустите для примера:
'''
if __name__ == "__main__":
    my_function(10, 0)
'''

## Тестирование:

1. в проекте используется фреймворк тестирования pytest.
2. для запуска тестов выполните команду: pytest.
3. для просмотра покрытия тестов, выполните команду: pytest --cov

## Логирование:

1. в функциях masks.py и utils.py реализовано логирование с помощью библиотеки logging.

## Документация

Для получения дополнительной информации обратитесь к [документации](README.md)

