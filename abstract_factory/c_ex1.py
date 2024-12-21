from ex_1 import CarFactory, AbstractCar, AbstractEngine, Client


class AudiFactory(CarFactory):
    """Фабрика для создания машины: Ауди"""

    def create_car(self):
        return AudiCar("Ауди", "Седан")

    def create_engine(self):
        return AudiEngine()


class AudiCar(AbstractCar):
    """Класс для машины: Ауди"""
    def __init__(self, name, body_type):
        super().__init__(name)
        self.body_type = body_type

    def max_speed(self, engine):
        return engine.max_speed

    def __str__(self):
        return f"Автомобиль {self.name} ({self.body_type})"


class AudiEngine(AbstractEngine):
    """Класс для двигателя машины: Ауди"""
    def __init__(self):
        super().__init__(max_speed=240)


if __name__ == "__main__":
    audi_factory = AudiFactory()
    audi_client = Client(audi_factory)
    print(f"Максимальная скорость {audi_client} составляет {audi_client.run_max_speed()} км/час")
