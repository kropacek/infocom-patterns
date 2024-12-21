from abc import ABC, abstractmethod


class ArithmeticUnit:
    def __init__(self):
        self.register = 0

    def run(self, operation: str, operand: int):
        if operation == "+":
            self.register += operand
        elif operation == "-":
            self.register -= operand
        elif operation == "*":
            self.register *= operand
        elif operation == "/":
            self.register /= operand


class Command(ABC):
    def __init__(self, unit: ArithmeticUnit, operand: int) -> None:
        self.unit = unit
        self.operand = operand

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def unexecute(self) -> None:
        raise NotImplementedError


class AddCommand(Command):
    def execute(self):
        self.unit.run("+", self.operand)

    def unexecute(self):
        self.unit.run("-", self.operand)


class ControlUnit:
    def __init__(self):
        self.commands = []
        self.current = 0

    def store_command(self, command: Command) -> None:
        self.commands.append(command)

    def execute_command(self) -> None:
        if self.current < len(self.commands):
            self.commands[self.current].execute()
            self.current += 1

    def undo(self, step=1) -> None:
        self.commands[self.current - step].unexecute()

    def redo(self, step=1) -> None:
        self.commands[self.current - step].execute()


class Calculator:
    def __init__(self):
        self.unit = ArithmeticUnit()
        self.control_unit = ControlUnit()

    def add(self, operand: int) -> float:
        command = AddCommand(self.unit, operand)
        self.control_unit.store_command(command)
        self.control_unit.execute_command()
        return self.unit.register

    def undo(self) -> float:
        self.control_unit.undo()
        return self.unit.register

    def redo(self) -> float:
        self.control_unit.redo()
        return self.unit.register

# Точка входа
if __name__ == "__main__":
    calc = Calculator()

    print("Добавляем 5:", calc.add(5))  # Результат: 5
    print("Добавляем 10:", calc.add(10))  # Результат: 15
    print("Отменяем:", calc.undo())  # Результат: 5
    print("Повторяем:", calc.redo())  # Результат: 15
