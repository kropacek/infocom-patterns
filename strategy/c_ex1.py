from abc import ABC, abstractmethod


class NavigationStrategy(ABC):

    @abstractmethod
    def find_route(self, start: str, end: str) -> str:
        raise NotImplementedError


class CarRoute(NavigationStrategy):
    def find_route(self, start: str, end: str) -> str:
        return f"Маршрут на автомобиле из {start} в {end}"

class WalkingRoute(NavigationStrategy):
    def find_route(self, start: str, end: str) -> str:
        return f"Пеший маршрут из {start} в {end}"

class BicycleRoute(NavigationStrategy):
    def find_route(self, start: str, end: str) -> str:
        return f"Велосипедный маршрут из {start} в {end}"


class Navigator:
    def __init__(self, strategy: NavigationStrategy) -> None:
        self.strategy = strategy

    def find_route(self, start: str, end: str) -> str:
        return self.strategy.find_route(start, end)

# Точка входа
if __name__ == "__main__":
    navigator = Navigator(CarRoute())
    print(navigator.find_route("Точка А", "Точка Б"))

    navigator = Navigator(WalkingRoute())
    print(navigator.find_route("Точка А", "Точка Б"))

    navigator = Navigator(BicycleRoute())
    print(navigator.find_route("Точка А", "Точка Б"))
