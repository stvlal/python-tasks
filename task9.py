# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

date_1 = 1917
date_2 = 2023
date_3 = 77
date_4 = 1603

lst = [date_1, date_2,  date_3, date_4]

for date in lst:
    print(f'{date} belongs to the {date // 100 + 1}th century')