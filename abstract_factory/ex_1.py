from abc import ABC, abstractmethod


class AbstractEngine(ABC):
    """Абстрактный класс двигателя"""

    def __init__(self, max_speed: float) -> None:
        self.max_speed = max_speed


class AbstractCar(ABC):
    """Абстрактный класс машины"""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def max_speed(self, engine: AbstractEngine) -> float:
        raise NotImplementedError


class CarFactory(ABC):
    """Абстрактная фабрика для машин"""

    @abstractmethod
    def create_car(self) -> AbstractCar:
        raise NotImplementedError

    @abstractmethod
    def create_engine(self) -> AbstractEngine:
        raise NotImplementedError


class FordFactory(CarFactory):
    """Фабрика для создания машины: Форд"""

    def create_car(self) -> AbstractCar:
        return FordCar("Форд")

    def create_engine(self) -> AbstractEngine:
        return FordEngine()


class FordCar(AbstractCar):
    """Класс для машины: Форд"""

    def __str__(self):
        return f"Автомобиль: {self.name}"

    def max_speed(self, engine: AbstractEngine) -> float:
        return engine.max_speed


class FordEngine(AbstractEngine):
    """Клас для двигателя машины: Форд"""

    def __init__(self) -> None:
        super().__init__(max_speed=220)


class Client:
    def __init__(self, car_factory):
        self.car = car_factory.create_car()
        self.engine = car_factory.create_engine()

    def run_max_speed(self):
        return self.car.max_speed(self.engine)

    def __str__(self):
        return str(self.car)


if __name__ == "__main__":
    ford_factory = FordFactory()
    client = Client(ford_factory)

    print(f"Максимальная скорость {client} составляет {client.run_max_speed()} км/час")