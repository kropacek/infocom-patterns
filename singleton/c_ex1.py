from abc import ABCMeta

from ex_1 import SingletonMeta
from abstract_factory.ex_1 import CarFactory, FordCar, FordEngine, Client


class CombinedMeta(SingletonMeta, ABCMeta):
    pass


class SingletonFordFactory(CarFactory, metaclass=CombinedMeta):

    def create_car(self):
        return FordCar("Ford")

    def create_engine(self):
        return FordEngine()


if __name__ == "__main__":
    ford_factory_1 = SingletonFordFactory()
    ford_factory_2 = SingletonFordFactory()

    # Проверяем, что это один и тот же объект
    print(f"Один объект: {ford_factory_1 is ford_factory_2}")

    # Работаем с фабрикой
    client = Client(ford_factory_1)
    print(f"Максимальная скорость {client} составляет {client.run_max_speed()} км/час")
