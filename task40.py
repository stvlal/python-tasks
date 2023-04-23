# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.

from calendar import monthrange, weekday, day_abbr

def dates(year, month):
    first_day, num_day = monthrange(year, month)
    return [(day, day_abbr[weekday(year, month, day)]) for day in range(1, num_day + 1)]

print(dates(2023, 4))
