from src.processing import filter_by_state, sort_by_date
from src.transactions import get_transactions_fnc
from src.utils import get_json_file
from src.widget import get_date, mask_account_card
from src.work_files_csv_xlsx import get_file_csv, get_file_xlsx


def main() -> None:
    """Функция, определяющая работу с конечным пользователем разработанной программы.
    Задаёт вопросы и в соответствии с полученными ответами работает с разработанными модулями."""

    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла.\n"
        "2. Получить информацию о транзакциях из CSV-файла.\n"
        "3. Получить информацию о транзакциях из XLSX-файла.\n"
    )
    while True:
        users_input = input("Введите выбранный пункт меню:\n")
        if users_input in ("1", "2", "3"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод.")
    menu = {
        "1": "JSON-файл.",
        "2": "CSV-файл.",
        "3": "XLSX-файл.",
    }
    print(f"Для обработки выбран {menu.get(users_input)}\n")
    if users_input == "1":
        transaction_list = get_json_file("data/operations.json")
    elif users_input == "2":
        transaction_list = get_file_csv("data/transactions.csv")
    elif users_input == "3":
        transaction_list = get_file_xlsx("data/transactions_excel.xlsx")

    # Фильтрация по статусу
    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n"
        )
        users_status = input("Введите выбранный статус:\n").upper()
        if users_status in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print("Введён некорректный статус. Повторите ввод.")
    filtred_transaction_data = filter_by_state(transaction_list, users_status)
    print(f"Операции отфильтрованы по статусу {users_status}.\n")

    # Фильтрация по дате
    while True:
        print("Отфильтровать операции по дате? Да/Нет\n")
        users_sort = input("Введите да или нет:\n").lower()
        if users_sort in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод.")
    if users_sort == "да":

        while True:
            print("Отфильтровать по возрастанию или убыванию?\n")
            users_sort_direction = input("Введите по возрастанию или по убыванию:\n").lower()
            if users_sort_direction in ("по возрастанию", "по убыванию"):
                break
            print("Введён некорректный ответ. Повторите ввод.")
        if users_sort_direction == "по возрастанию":
            direction = False
        elif users_sort_direction == "по убыванию":
            direction = True
        date_sorted_transactions = sort_by_date(filtred_transaction_data, direction)
    elif users_sort == "нет":
        date_sorted_transactions = filtred_transaction_data

    # Фильтрация по рублёвым транзакциям
    while True:
        print("Выводить только рублёвые транзакции?\n")
        users_rub = input("Введите да или нет:\n").lower()
        if users_rub in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод.")
    if users_rub == "да" and users_input == "1":
        rub_transactions = [
            transaction
            for transaction in date_sorted_transactions
            if transaction["operationAmount"]["currency"]["code"] == "RUB"
        ]
    elif users_rub == "да":
        rub_transactions = [
            transaction for transaction in date_sorted_transactions if transaction["currency_code"] == "RUB"
        ]
    else:
        rub_transactions = date_sorted_transactions

    # Фильтрация по определённому слову в описании
    while True:
        print("Отфильтровать список по определённому слову в описании?\n")
        users_description = input("Введите да или нет:\n").lower()
        if users_description in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод.\n")
    if users_description == "да":
        users_word = input("Введите слово для сортировки:\n").lower()
        sorted_by_description = get_transactions_fnc(rub_transactions, users_word)
        result_transactions = sorted_by_description
    elif users_description == "нет":
        result_transactions = rub_transactions

    # Вывод результата, если список не пустой
    if len(result_transactions) > 0:
        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке {len(result_transactions)}.\n")
        for item in result_transactions:
            if users_input == "1":
                if item["description"] == "Открытие вклада":
                    date_str = get_date(item["date"])
                    description_str = item["description"]
                    summa_str = item["operationAmount"]["amount"]
                    currency_str = item["operationAmount"]["currency"]["code"]
                    print(f"{date_str} {description_str}\nСумма: {summa_str} {currency_str}\n")
                else:
                    date_str = get_date(item["date"])
                    description_str = item["description"]
                    from_str = mask_account_card(item["from"])
                    to_str = mask_account_card(item["to"])
                    summa_str = item["operationAmount"]["amount"]
                    currency_str = item["operationAmount"]["currency"]["code"]
                    print(f"{date_str} {description_str}\n{from_str} -> {to_str}\nСумма: {summa_str} {currency_str}\n")
            elif item["description"] == "Открытие вклада":
                date_str = get_date(item["date"])
                description_str = item["description"]
                summa_str = item["amount"]
                currency_str = item["currency_code"]
                print(f"{date_str} {description_str}\nСумма: {summa_str} {currency_str}\n")
            else:
                date_str = get_date(item["date"])
                description_str = item["description"]
                from_str = mask_account_card(item["from"])
                to_str = mask_account_card(item["to"])
                summa_str = item["amount"]
                currency_str = item["currency_code"]
                print(f"{date_str} {description_str}\n{from_str} -> {to_str}\nСумма: {summa_str} {currency_str}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
