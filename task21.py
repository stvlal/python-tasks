#todo:  Напишите программу, которая получает на вход строку, и определяет,
# является ли строка панграммой (т.е. содержатся ли в ней все 33 буквы русского алфавита).

s = input("Enter your string: ")

a = set()

for symbol in s:
    if symbol.isalpha(): a.add(symbol.lower())

if len(a) == 33:
    print("Pangram")
else:
    print("Not a pangram")