from abc import ABC, abstractmethod

class Progression(ABC):

    def __init__(self, first: int, last: int, step: int) -> None:
        self.first = first
        self.last = last
        self.step = step
        self.prog_list = []

    def template_method(self) -> None:
        self.initialize_progression()
        self.generate_progression()
        self.print_progression()

    def initialize_progression(self) -> None:
        print(f"Инициализация: начало = {self.first}, конец = {self.last}, шаг = {self.step}")

    def print_progression(self) -> None:
        print(f"Последовательность: {self.prog_list}")

    @abstractmethod
    def generate_progression(self) -> None:
        raise NotImplementedError


class ArithmeticProgression(Progression):
    def generate_progression(self) -> None:
        value = self.first
        while value < self.last:
            self.prog_list.append(value)
            value += self.step


class GeometricProgression(Progression):
    def generate_progression(self) -> None:
        value = self.first
        while value < self.last:
            self.prog_list.append(value)
            value *= self.step


if __name__ == "__main__":
    # Арифметическая прогрессия
    arithmetic_prog = ArithmeticProgression(1, 10, 2)
    arithmetic_prog.template_method()

    # Геометрическая прогрессия
    geometric_prog = GeometricProgression(1, 100, 2)
    geometric_prog.template_method()
