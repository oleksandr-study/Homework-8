from collections import defaultdict

from datetime import date, datetime, timedelta

def get_period(start_date: date, days: int) -> dict:
    result = {}
    for _ in range(days + 1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    return result

def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    Birthday_people = defaultdict(list)

    start_date = date.today()
    period = get_period(start_date, 7)

    for user in users:
        birthday: date = user["birthday"]
        date_birthday = birthday.day, birthday.month
        if date_birthday in list(period):
            full_date = datetime(year=period[date_birthday], month=birthday.month, day=birthday.day)
            print(full_date.weekday())
            if full_date.weekday() == 5 or full_date.weekday() == 6:
                Birthday_people["Monday"].append(user["name"])
            else:
                Birthday_people[full_date.strftime('%A')].append(user["name"])

    return Birthday_people


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 31).date()},
        {"name": "Kim", "birthday": datetime(1976, 11, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
