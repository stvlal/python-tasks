# todo:
#     Напишите программу, которая определяет и печатает «похожие» слова. Слово называется похожим на другое слово,
#     если его гласные буквы находятся там же, где находятся гласные буквы другого слова, например:
#     дорога и пароход - похожие слова (гласные буквы на втором, четвертом и шестом местах),
#     станок и прыжок - похожие слова, питон и удав непохожие слова.
#     Считаем, что в русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е).
#     Ввод: x –первое слово, например, питон. n – количество слов для сравнения, например 6.
#     Дальше вводятся 6 слов, например: поросенок, титан, итог, лавка, погост, кино.
#     Вывод - слова, похожие на питон: титан, погост, кино

vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

user_word = input('your word: ')
# n = input('n = ') useless thing 
words_to_compare = input('words to compare: ')

user_word_vowels_positions = [idx for idx, el in enumerate(user_word) if el in vowels]
words_to_compare_lst = [el.strip() for el in words_to_compare.split(',')]
for word in words_to_compare_lst:
    if [idx for idx, el in enumerate(word) if el in vowels] == user_word_vowels_positions:
        print(word, end=' ')
