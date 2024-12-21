import random
from abc import ABC, abstractmethod


class IGame(ABC):
    """Интерфейс для игры"""

    @abstractmethod
    def brosok(self) -> int:
        """Выполняет действие: бросок"""
        raise NotImplementedError


class Kost(IGame):
    """Класс игральной кости"""

    def brosok(self) -> int:
        """Возвращает результат броска игральной кости"""
        return random.randint(1, 6)


class Gamer:
    """Класс игрока"""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return self.name

    def seans_game(self, ig) -> int:
        """Выполняет действие бросок для игры"""
        return ig.brosok()


class Monet:
    """Класс монеты"""

    def brosok_m(self):
        """Возвращает результат броска монеты"""
        return random.randint(1, 2)


class AdapterGame(IGame):
    """Адаптер классов игр для класса монеты"""

    def __init__(self, monet: Monet) -> None:
        self.monet = monet

    def brosok(self) -> int:
        """Адаптирует метод brosok_m класса Monet для классов игр"""
        return self.monet.brosok_m()


if __name__ == '__main__':

    kub = Kost()
    gamer = Gamer('Иван')
    print(f"Выпало очков {gamer.seans_game(kub)} для игрока {gamer}")

    mon = Monet()
    bmon = AdapterGame(mon)
    print(f'Монета показала "{gamer.seans_game(bmon)}" для игрока {gamer}')