#todo: Дан список из кортежей (Фамилия, премия). Напечатать эти кортежи в порядке убывания премии.
# Тех, у кого одинаковая премия, то печатать в алфавитном порядке.
#  Пример ввода:
# [(Иванов, 100), (Петров, 200), (Сидоров, 200), (Воробьев, 100), (Лунин, 200)]
# Вывод:
#     Лунин 200
#     Петров 200
#     Сидоров 200
#     Воробьев 100
#     Иванов 100
#
#     Примечание:
#     https://pythonist.ru/lyambda-funkczii-dlya-sortirovki-razlichnyh-spiskov-v-python/

lst = [('Иванов', 100), ('Петров', 200), ('Сидоров', 200), ('Воробьев', 100), ('Лунин', 200)]

lst_by_award = sorted(lst, key = lambda x: x[1], reverse=True)

output_lst = []
while len(lst_by_award) != 0:
    award = lst_by_award[0][1] 
    sublist_by_name = sorted([el for el in lst if el[1] == award], key = lambda x: x[0])
    output_lst.extend(sublist_by_name)
    lst_by_award = [el for el in lst_by_award if el not in output_lst]

print(output_lst)

