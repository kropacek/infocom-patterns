from abc import ABC, abstractmethod


class ITemperatureSensor(ABC):
    """Интерфейс датчика температур"""

    @abstractmethod
    def get_temperature(self) -> float:
        raise NotImplementedError


class FahrenheitSensor(ITemperatureSensor):
    """Класс датчика температур по Фаренгейту"""

    def __init__(self, temperature) -> None:
        self.temperature = temperature

    def get_temperature(self) -> float:
        return self.temperature


class TemperatureAdapter(ITemperatureSensor):
    """Адаптер для сенсора температур по цельсию"""

    def __init__(self, fahrenheit_sensor) -> None:
        self.fahrenheit_sensor = fahrenheit_sensor

    def get_temperature(self) -> float:
        temperature_f = self.fahrenheit_sensor.get_temperature()
        temperature_c = (temperature_f - 32) * 5 / 9
        return temperature_c


if __name__ == "__main__":
    fahrenheit_sensor = FahrenheitSensor(212.2)
    adapter = TemperatureAdapter(fahrenheit_sensor)

    print(f"Температура в Фаренгейтах: {fahrenheit_sensor.get_temperature():.2f}")
    print(f"Температура в Цельсиях: {adapter.get_temperature():.2f}")