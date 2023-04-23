# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

a = 1234
b = 3443
c = 9898

lst = [a, b, c]

for el in lst:
    if list(str(el)) == list(str(el))[::-1]:
        print(f'number {el} is a palindrome')
    else:
        print(f'number {el} is NOT a palindrome')
