#todo:
#  Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
#
# Проблема.
# Преподаватель каждый урок задает некоторое количество задач в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета?
# Разработайте систему
# классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа?);
# атрибутов для каждого состояния каждого объекта;
# методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи – спецификации или технического задания. Затем спроектируйте классы, атрибуты, методы. Протестируйте систему.


import random


class Teacher:
    """"содержит два метода: один для проверки верно ли решена задача,
        второй для печати результатов проверки данной задачи для данного студента
    """
    @staticmethod
    def check_if_task_is_solved_right(student):
        if student.is_task_solved:
            student.is_task_solved_right = random.choice([True, False])

    @staticmethod
    def print_result(student):
        print(f"Student {student.name}; Lesson #{student.number}; Is task solved right: {student.is_task_solved_right}")


class Lesson:
    """содержит порядковый номер лекции, который соответствует номеру задачи"""
    def __init__(self, number):
        self.number = number


class Task(Lesson):
    """"содержит номер задачи который равен номеру лекции;
        содержит статус задачи (изначально 'нерешена' т.е. False)
        содержит статус задачи после проверки преподавателем
    """
    def __init__(self, number):
        super().__init__(number)
        self.is_task_solved = False
        self.is_task_solved_right = None


class Student(Task):
    """содержит все поля класса Task и дополнительно имя студента"""
    def __init__(self, name, number):
        super().__init__(number)
        self.name = name

    def solve_task(self):
        """переводит статус задачи на 'решена'"""
        self.is_task_solved = True


# список студентов в группе
students = ['Dima', "Vlad", "Alina", "Boris"]

student1 = Student(students[1], 3)
student1.solve_task()
Teacher.check_if_task_is_solved_right(student1)
Teacher.print_result(student1)

student2 = Student(students[2], 5)
student2.solve_task()
Teacher.check_if_task_is_solved_right(student2)
Teacher.print_result(student2)



