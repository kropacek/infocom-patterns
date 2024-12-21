from datetime import datetime


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Log(metaclass=SingletonMeta):

    def __init__(self):
        if not hasattr(self, "log_file"):
            self.log_file = "log.txt"

    def log_execution(self, message):
        with open(self.log_file, "a") as f:
            log_message = f"[{datetime.now()}] {message}\n"
            f.write(log_message)


class Operation:

    @staticmethod
    def run(operation_code, operand, current_value=0):
        log = Log()
        if operation_code == "+":
            result = current_value + operand
            log.log_execution(f"Сложение {operand}. Результат: {result}")
        elif operation_code == "-":
            result = current_value - operand
            log.log_execution(f"Вычитание {operand}. Результат: {result}")
        elif operation_code == "*":
            result = current_value * operand
            log.log_execution(f"Умножение на {operand}. Результат: {result}")
        elif operation_code in ["/", ":"]:
            result = current_value / operand if operand != 0 else "Ошибка деления"
            log.log_execution(f"Деление на {operand}. Результат: {result}")
        else:
            result = "Неизвестная операция"
            log.log_execution(f"Неизвестная операция: {operation_code}")
        return result


if __name__ == "__main__":
    log = Log()
    log.log_execution("Запуск программы")

    result = Operation.run("+", 30)
    print(f"Результат: {result}")

    result = Operation.run("-", 10, current_value=result)
    print(f"Результат: {result}")

    result = Operation.run("*", 2, current_value=result)
    print(f"Результат: {result}")

    result = Operation.run("/", 0, current_value=result)
    print(f"Результат: {result}")
