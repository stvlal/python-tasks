#todo Задача 1. Транспонирование матрицы, transpose(matrix)
# Создайте списковое включение, которое генерирует следующую последовательность: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10


#todo Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])

# [[1, 4], [2, 5], [3, 6]]


# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
            #    ||3 6||



#todo Задача 3. Найти сумму элементов матрицы
# Написать msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)

# Задача 1
print([el for el in range(1, 10 + 1) for _ in range(el)])
print('\n')

# Задача 2
def transpose(matrix):
    print('initial matrix:')
    for el in matrix:
        print(el)
    
    print('\ntransposed matrix:')
    transposed_matrix = [[el1, el2] for el1, el2 in list(zip(matrix[0], matrix[1]))]
    for el in transposed_matrix:
        print(el)


transpose([[1, 2, 3], [4, 5, 6]])
print('\n')

# Задача 3
def msum(matrix):
    return sum([col for row in matrix for col in row])


print(msum([[1, 2, 3], [4, 5, 6]]))
