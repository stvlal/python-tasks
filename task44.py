#todo: Напишите программу, в которой используется две функции. В одной программа «спит» 2 секунды, в другой – 3 секунды. Пусть каждая функция возвращает время, которое она «проспала».
# Главная программа запускает цикл от 0 до 10, если число четное, то запускает функцию с 2 секундами, если нечетное, то функцию с 3 секундами. 
# Накапливает сон обеих функций отдельно и печатает две суммы.

import time

def sleep_2_sec():
    sleep_time = 2
    time.sleep(sleep_time)
    return sleep_time


def sleep_3_sec():
    sleep_time = 3
    time.sleep(sleep_time)
    return sleep_time


def main():
    sleep_2_sec_total = 0
    sleep_3_sec_total = 0
    for idx in range(0, 10 + 1):
        if idx % 2 == 0:
            sleep_2_sec_total += sleep_2_sec()
        else:
            sleep_3_sec_total += sleep_3_sec()
    print(f'sleep_2_sec_total = {sleep_2_sec_total}')
    print(f'sleep_3_sec_total = {sleep_3_sec_total}')

main()