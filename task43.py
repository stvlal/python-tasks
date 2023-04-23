#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.

from calendar import monthrange, weekday, day_abbr, month_name

def make_lst(year=2023):
    result = {}
    for month in range(1, 12 + 1):
        first_day, num_day = monthrange(year, month)
        month_days = [(day, day_abbr[weekday(year, month, day)]) for day in range(1, num_day + 1)]
        third_thu = list( filter(lambda x: True if x[1] == 'Thu' else False, month_days) )[2]
        result[month_name[month]] = third_thu
    return result


print( make_lst() )