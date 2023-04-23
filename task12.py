# # Написать игру "Поле чудес"
#
# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:
#

import random
import sys

def print_word(word):
    for el in word:
        print(el, end=" ")
    print('\n')

words = ["оператор", "конструкция", "объект"]
desc_ = [
    "Это слово обозначает наименьшую автономную часть языка программирования",
    "Любую программу можно составить только из структур трех типов: следования, ветвления и цикла, которые называются базывыми...",
    "Каждое значение переменной это..."
]

n_try = 0

while True:
    current_word_desc = random.choice(desc_)
    current_word_index = desc_.index(current_word_desc)
    current_word = words[current_word_index]

    print(current_word_desc)

    word_on_screen = ["#" for el in current_word]

    print_word(word_on_screen)

    while True:
        if n_try >= 10:
            sys.exit("Использовано 10 попыток")
        letter = input("Введите букву: ")
        if letter in current_word and len(letter) == 1:
            letter_idx = [idx for idx, value in enumerate(current_word) if value == letter]
            for idx in letter_idx:
                word_on_screen[idx] = letter
            print_word(word_on_screen)
            if word_on_screen == list(current_word):
                print("Слово угадано")
                print('\n')
                break
        else:
            print('Нет такой буквы')
            n_try = n_try + 1
            if n_try != 10:
                print(f"У вас осталось {10 - n_try} попыток !")

    del words[current_word_index]
    del desc_[current_word_index]

    if len(words) == 0:
        print("Game over")
        break
