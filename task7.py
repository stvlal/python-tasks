# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

lst = [x, y, z]

print(f'max number is {max(lst)}')