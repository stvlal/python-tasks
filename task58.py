#todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, velocity, own_cost):
        self.velocity = velocity
        self.own_cost = own_cost
        self.cost = None

    @abstractmethod
    def Cost(self):
        pass

    @abstractmethod
    def Info(self):
        pass


class Marine(Transport):
    def __init__(self, velocity, own_cost):
        super().__init__(velocity, own_cost)

    def Cost(self):
        self.cost = int(self.velocity * self.own_cost / 3)

    def Info(self):
        return f"{self.__class__.__name__}: velocity - {self.velocity}; own_cost - {self.own_cost}; cost - {self.cost}"


class Ground(Transport):
    def __init__(self, velocity, own_cost):
        super().__init__(velocity, own_cost)

    def Cost(self):
        self.cost = int(self.velocity * self.own_cost / 8)

    def Info(self):
        return f"{self.__class__.__name__}: velocity - {self.velocity}; own_cost - {self.own_cost}; cost - {self.cost}"


m = Marine(5, 400)
m.Cost()
print(m.Info())

g = Ground(9, 400)
g.Cost()
print(g.Info())
