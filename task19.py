#todo: Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.

inp = input("Your input: ")
inp_lst = inp.split(" ")
a = float(inp_lst[0])
b = float(inp_lst[-1])
operation = inp_lst[1]

match operation:
    case '+' : print(a + b)
    case '-' : print(a - b)
    case '*' : print(a * b)
    case '/' : print(a / b)