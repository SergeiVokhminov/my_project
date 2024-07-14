# from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

user_number = "Visa Classic 6831982476737658"

user_date_str = "2024-03-11T02:26:18.671407"

user_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# print(mask_account_card(user_number))

# print(get_date(user_date_str))

print(filter_by_state(user_list, "CANCELED"))

print(sort_by_date(user_list))
