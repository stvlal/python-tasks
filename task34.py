# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.


def sumn(n):
    return n + sumn(n-1) if n else 0

n = 5
print(sumn(n))