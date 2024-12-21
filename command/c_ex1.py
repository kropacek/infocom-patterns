from ex_1 import Command, ArithmeticUnit, ControlUnit, AddCommand


class SubtractCommand(Command):
    def execute(self):
        self.unit.run("-", self.operand)

    def unexecute(self):
        self.unit.run("+", self.operand)


class MultiplyCommand(Command):
    def execute(self):
        self.unit.run("*", self.operand)

    def unexecute(self):
        self.unit.run("/", self.operand)


class DivideCommand(Command):
    def execute(self):
        self.unit.run("/", self.operand)

    def unexecute(self):
        self.unit.run("*", self.operand)


class Calculator:
    def __init__(self):
        self.unit = ArithmeticUnit()
        self.control_unit = ControlUnit()

    def add_command(self, command):
        self.control_unit.store_command(command)
        self.control_unit.execute_command()

    def add(self, operand):
        command = AddCommand(self.unit, operand)
        self.add_command(command)
        return self.unit.register

    def subtract(self, operand):
        command = SubtractCommand(self.unit, operand)
        self.add_command(command)
        return self.unit.register

    def multiply(self, operand):
        command = MultiplyCommand(self.unit, operand)
        self.add_command(command)
        return self.unit.register

    def divide(self, operand):
        command = DivideCommand(self.unit, operand)
        self.add_command(command)
        return self.unit.register

    def undo(self, steps=1):
        for step in range(steps):
            self.control_unit.undo(step + 1)
        return self.unit.register

    def redo(self, steps=1):
        for step in reversed(range(steps)):
            self.control_unit.redo(step + 1)
        return self.unit.register

# Точка входа
if __name__ == "__main__":
    calc = Calculator()

    print("Добавляем 5:", calc.add(5))  # 5
    print("Умножаем на 2:", calc.multiply(2))  # 10
    print("Вычитаем 3:", calc.subtract(3))  # 7
    print("Делим на 2:", calc.divide(2))  # 3.5
    print("Отменяем два шага:", calc.undo(2))  # 10
    print("Повторяем два шага:", calc.redo(2))  # 3.5
