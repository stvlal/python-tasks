#todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.


def my_decorator(func):
    def wrapper(*args, **kwargs):
        output_args = [el.upper() for el in args if isinstance(el, str)]
        output_kwargs = [el.upper() for el in kwargs.values() if isinstance(el, str)]
        func(*args, **kwargs)
        return output_args + output_kwargs
    return wrapper


@my_decorator
def my_function(*args, **kwargs):
    print('hello work')


print(my_function('qwerty', False, 65, 'arg1', id=43, flag='flag'))

