#todo 1: создайте модуль serializer

# В модуле реализуйте три функции сериализации

# Функция сериализует объект в байтовый поток pickle
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.pkl"
# def to_pickle(obj, file):
    # pass
    # ваш код

#  Функция сериализует объект в json
#  Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.json"
# def to_json(obj, file):
    # pass
    # ваш код

# Функция сериализует объект в yaml
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.yml"
# def to_yaml(obj, file):
    # pass
    # ваш код


#todo 2: Cоздайте модуль deserializer. В модуле реализуйте три функции десериализации


# Функция десериализует объект из файла типа pickle
# file - файл для десериализации к примеру "data.pkl"
# def from_pickle(file):
    # pass
    # ваш код

# Функция десериализует объект из файла типа json
# from_json - функция сереализует объект в json
# Параметры
# file - файл для десериализации к примеру "data.json"
# def from_json(file):
    # pass
    # ваш код


# Функция десериализует объект из файла типа yaml
# Параметры
# file - файл для десериализации к примеру "data.yml"
# def from_yaml(file):
    # pass
    # ваш код

#todo 3: Cоздайте пакет из двух модулей serializer и deserializer.

# Импортируйте модули пакета в отдельный файл и протестируйте все функции.

from my_package import serializer, deserializer

obj_for_pickle = {"one": 123, "two": [1, 2, 3]}
obj_for_json = {"three": 456, "four": [4, 5, 6]}
obj_for_yaml = {"five": 789, "six": [7, 8, 9]}


serializer.to_pickle(obj_for_pickle, 'data.pkl')
serializer.to_json(obj_for_json, 'data.json')
serializer.to_yaml(obj_for_yaml, 'data.yml')


print(deserializer.from_pickle('data.pkl'))
print(deserializer.from_json('data.json'))
print(deserializer.from_yaml('data.yml'))