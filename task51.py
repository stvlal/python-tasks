#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ


class Person:
    def __init__(self, name, surname, dad_name):
        self.name = name
        self.surname = surname
        self.dad_name = dad_name

    def __str__(self):
        return (self.name + self.surname + self.dad_name)[::-1]


p = Person('Иванов', 'Михаил', 'Федорович')

print(p)
