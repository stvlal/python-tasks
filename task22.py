#todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. 
# Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.

import string

alphabet_lowercase = list(string.ascii_lowercase)
alphabet_uppercase = list(string.ascii_uppercase)

def code(string, n):
    output_lst = []
    num_of_letters = len(alphabet_lowercase)
    for symbol in string:
        if symbol.isalpha():
            symbol_idx = alphabet_lowercase.index(symbol.lower())
            idx = symbol_idx + n 
            if idx >= num_of_letters:
                idx = abs(idx - num_of_letters) * 2 - idx
            if symbol.islower():
                output_lst.append(alphabet_lowercase[idx])
            else: 
                output_lst.append(alphabet_uppercase[idx])
        else:
            output_lst.append(symbol)
    print(''.join(output_lst))


my_string = input("Your string: ")
n = int(input("n = "))

code(my_string, n)



