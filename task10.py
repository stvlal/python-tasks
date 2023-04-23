# Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
# Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
# >4

# Введите  массу тела
# >1
#
# Ответ: 1000 кг

import sys

mass_unit = int(input("""Enter mass unit 
                    1 - kilogram, 
                    2 - milligram, 
                    3 - gram, 
                    4 - ton, 
                    5 - centner
> """))

if mass_unit not in [1, 2, 3, 4, 5]:
    sys.exit("wrong mass unit")

mass = float(input("""Enter mass
> """))

match mass_unit:
    case 1: print(f'Response: {mass} kilograms')
    case 2: print(f'Response: {mass * 1e-3 / 1e3} kilograms')
    case 3: print(f'Response: {mass / 1e3} kilograms')
    case 4: print(f'Response: {mass * 1e3} kilograms')
    case 5: print(f'Response: {mass * 100} kilograms')

