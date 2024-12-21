from ex_1 import TransportService, TransportCompany


class DrunkDriverService(TransportService):
    """Класс сервиса: пьяный водитель"""

    def __init__(self, name: str, base_rate: float) -> None:
        super().__init__(name)
        self.base_rate = base_rate

    def cost_transportation(self, distance: float) -> float:
        return self.base_rate + (distance * 0.5)

    def __str__(self):
        return f"Фирма {self.name}, базовая ставка {self.base_rate}"

# Новая компания для услуги "пьяный водитель"
class DrunkDriverCompany(TransportCompany):
    """Класс компании: пьяный водитель"""

    def create(self, name: str, base_rate: float) -> DrunkDriverService:
        return DrunkDriverService(self.name, base_rate)

# Точка входа
if __name__ == "__main__":
    # Новая услуга
    drunk_driver_company = DrunkDriverCompany("Служба 'пьяный водитель'")
    drunk_driver_service = drunk_driver_company.create("Пьяный водитель", 200)
    distance = 20
    print(f"Компания {drunk_driver_service}, расстояние: {distance} км, стоимость: {drunk_driver_service.cost_transportation(distance):.2f} руб.")
