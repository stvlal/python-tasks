# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
#
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
#
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше 9 символов
# LetterError, если в нем все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
#
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.
#
#
# Sample Input 1:
#
# arr1
# Arrrrrrrrrrr
# arrrrrrrrrrrrrrr1
# Arrrrrrr1
# Sample Output 1:
#
# LengthError
# DigitError
# LetterError
# Success!
#
# Sample Input 2:
#
# beegeek
# Beegeek123
# Beegeek2022
# Beegeek2023
# Beegeek2024
# Sample Output 2:
# LengthError
# Success!

class LengthError(Exception):
    pass


class LetterError(Exception):
    pass


class DigitError(Exception):
    pass


def check_length(string):
    if len(string) < 9:
        raise LengthError('LengthError')
    else:
        return True


def check_letters(string):
    flag_lowercase = False
    flag_uppercase = False
    for letter in string:
        if letter.isalpha():
            if letter.islower():
                flag_lowercase = True
            elif letter.isupper():
                flag_uppercase = True

    if not (flag_lowercase and flag_uppercase):
        raise LetterError('LetterError')
    else:
        return True


def check_digit(string):
    flag_digit = False
    for letter in string:
        if letter.isdigit():
            flag_digit = True
            break
    if not flag_digit:
        raise DigitError('DigitError')
    else:
        return True


while True:
    try:
        passwd = input('enter your password: ')
        if check_length(passwd) and check_letters(passwd) and check_digit(passwd):
            print('Success!')
            break
    except LengthError as ex:
        print(ex)
    except LetterError as ex:
        print(ex)
    except DigitError as ex:
        print(ex)
