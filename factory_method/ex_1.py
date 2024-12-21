from abc import ABC, abstractmethod


class TransportService(ABC):
    """Абстрактный класс транспортного сервиса"""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def cost_transportation(self, distance: float) -> float:
        raise NotImplementedError


class TransportCompany(ABC):
    """Абстрактный класс транспортной компании"""

    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def create(self, name: str, coefficient: float) -> TransportService:
        raise NotImplementedError


class TaxiService(TransportService):
    """Класс такси сервиса"""

    def __init__(self, name: str, category: float) -> None:
        super().__init__(name)
        self.category = category

    def cost_transportation(self, distance: float) -> float:
        return distance * self.category

    def __str__(self):
        return f"Фирма {self.name}, поездка категории {self.category}"


class ShippingService(TransportService):
    """Класс перевозки сервиса"""

    def __init__(self, name: str, tariff: float) -> None:
        super().__init__(name)
        self.tariff = tariff

    def cost_transportation(self, distance: float) -> float:
        return distance * self.tariff

    def __str__(self):
        return f"Фирма {self.name}, доставка по тарифу {self.tariff}"


class TaxiTransportCompany(TransportCompany):
    """Класс транспортной компании: такси"""

    def create(self, name: str, category: float) -> TransportService:
        return TaxiService(name, category)


class ShippingTransportCompany(TransportCompany):
    """Класс транспортной компании: перевозка"""

    def create(self, name: str, tariff: float) -> TransportService:
        return ShippingService(name, tariff)


if __name__ == "__main__":
    taxi_company = TaxiTransportCompany("Служба такси")
    taxi_service = taxi_company.create("Такси", 1)
    distance = 15.5
    print(f"Компания {taxi_service}, расстояние: {distance} км, стоимость: {taxi_service.cost_transportation(distance):.2f} руб.")

    # Создаем транспортную компанию (грузоперевозки)
    shipping_company = ShippingTransportCompany("Служба перевозок")
    shipping_service = shipping_company.create("Грузоперевозки", 1.5)
    distance = 150.5
    print(f"Компания {shipping_service}, расстояние: {distance} км, стоимость: {shipping_service.cost_transportation(distance):.2f} руб.")